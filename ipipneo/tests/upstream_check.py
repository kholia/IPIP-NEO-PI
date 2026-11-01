#!/usr/bin/env python3
"""
Verifies our scoring against Dr. Johnson's official IPIP-NEO-120 scripts.

The live site (drj60472.virtualave.net) stores every completed test in Dr.
Johnson's research database, so this script never contacts it. Instead, run
a local copy of his CGI scripts (shortipipneo1.cgi, 2.cgi, 3.cgi; ask him
for the current version) in any CGI-capable web server, e.g. a Perl
container, and point this script at it.

1. record: walk the official test (1.cgi -> 2.cgi -> 3.cgi) on the local copy
   with random answers and save each request + results page as a fixture.

       python3 upstream_check.py record --official http://127.0.0.1:8080/cgi-bin/ -n 500

2. check: replay every fixture against our server (Go or Python) and compare
   all 35 percentile scores plus the norm group.

       python3 upstream_check.py check --local http://127.0.0.1:8888/
       python3 upstream_check.py check --program dist/macos/IPIP-NEO-PI-macOS-AppleSilicon

Standard library only; runs on Python 3.5+.
"""

import argparse
import glob
import html
import json
import os
import random
import re
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser

# Hosts that feed Dr. Johnson's research database: never submit to these.
LIVE_HOSTS = ("virtualave.net", "psu.edu")
FIXTURES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "upstream_fixtures")
NICK = "Testing Please Ignore"
USER_AGENT = "IPIP-NEO-PI verification (https://github.com/kholia/IPIP-NEO-PI)"

# Upstream "sex assigned at birth" codes -> our port's values. Upstream also
# has 3 = intersex, which the 2021 scoring code does not support.
SEX_CODES = {"1": "Male", "2": "Female"}

AGES = [18, 20, 21, 30, 40, 41, 50, 60, 61, 75]


class FormParser(HTMLParser):
    """Collects the <input>s of the first <form>, in document order."""

    def __init__(self):
        HTMLParser.__init__(self)
        self.action = None
        self.fields = []  # (name, type, value)
        self.in_form = False

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag == "form" and self.action is None:
            self.action, self.in_form = a.get("action"), True
        elif tag == "input" and self.in_form and a.get("name"):
            self.fields.append((a["name"], a.get("type", "text").lower(), a.get("value", "")))
        elif tag == "select" and self.in_form and a.get("name"):
            self.fields.append((a["name"], "select", ""))

    def handle_endtag(self, tag):
        if tag == "form":
            self.in_form = False


def parse_form(page):
    p = FormParser()
    p.feed(page)
    return p


def fill(form, answers):
    """Builds the POST body the way a browser would: fields in document
    order (the official CGI scripts depend on the order), one entry per
    radio group, unchecked radios omitted."""
    body, seen = [], set()
    for name, typ, value in form.fields:
        if name in seen:
            continue
        if typ == "hidden":
            body.append((name, value))
        elif name in answers:
            body.append((name, answers[name]))
            seen.add(name)
        elif typ in ("text", "select"):
            body.append((name, ""))
        elif typ == "submit":
            body.append((name, value))
        if typ != "radio":
            seen.add(name)
    return body


def post(url, body):
    req = urllib.request.Request(url, urllib.parse.urlencode(body).encode(),
                                 {"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("latin-1")


def title(page):
    m = re.search(r"<title>(.*?)</title>", page, re.S | re.I)
    return m.group(1).strip() if m else "?"


def random_case(rng):
    case = {
        "Nick": NICK,
        "Sex": rng.choice(sorted(SEX_CODES)),
        "Gender": "8",  # "prefer not to answer"
        "Age": str(rng.choice(AGES)),
        "Country": "USA",
    }
    style = rng.random()
    for i in range(1, 121):
        if style < 0.1:
            case["Q%d" % i] = str(rng.choice([1, 5]))
        else:
            case["Q%d" % i] = str(rng.randint(1, 5))
    return case


def record(args):
    official = args.official.rstrip("/") + "/"
    host = urllib.parse.urlsplit(official).hostname or ""
    if any(host == h or host.endswith("." + h) for h in LIVE_HOSTS):
        sys.exit("Refusing to submit to the live site %s: it stores every test in "
                 "Dr. Johnson's research database. Use a local copy of the scripts." % host)
    os.makedirs(FIXTURES, exist_ok=True)
    rng = random.Random(args.seed)

    for n in range(args.n):
        case = random_case(rng)
        page1 = post(official + "shortipipneo1.cgi", [("Accuracy", "Yes")])
        form1 = parse_form(page1)
        page2 = post(official + form1.action, fill(form1, case))
        form2 = parse_form(page2)
        if not form2.action:
            sys.exit("page 2 failed: %s" % title(page2))
        body3 = fill(form2, case)
        results = post(official + form2.action, body3)

        scores = parse_results(results)
        if len(scores) != 35:
            sys.exit("could not parse results page (%s); got %r" % (title(results), scores))

        stamp = time.strftime("%Y%m%d-%H%M%S")
        path = os.path.join(FIXTURES, "%s-%02d.json" % (stamp, n))
        with open(path, "w") as f:
            json.dump({"request": body3, "results_html": results,
                       "recorded": time.strftime("%Y-%m-%d %H:%M:%S %z")}, f, indent=1)
        print("recorded %s (%s, age %s)" % (os.path.basename(path), case["Sex"], case["Age"]))
        if n + 1 < args.n:
            time.sleep(args.delay)


class ResultsParser(HTMLParser):
    """Collects every <table> row as a list of cell texts."""

    def __init__(self):
        HTMLParser.__init__(self)
        self.rows, self.row, self.cell = [], None, None

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.row = []
        elif tag in ("td", "th") and self.row is not None:
            self.cell = []

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self.cell is not None:
            self.row.append(" ".join("".join(self.cell).split()))
            self.cell = None
        elif tag == "tr" and self.row is not None:
            self.rows.append(self.row)
            self.row = None

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)


def parse_results(page):
    """Returns {label: percentile} from the official results page tables,
    whose rows look like ("..Friendliness", "82")."""
    p = ResultsParser()
    p.feed(page)
    scores = {}
    for row in p.rows:
        if len(row) >= 2 and re.fullmatch(r"\d+", row[1]):
            scores[row[0].lstrip(".").strip()] = int(row[1])
    return scores


def parse_category(page):
    text = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", page)).split())
    m = re.search(r"compares .*? to other (.*?)\. \(", text)
    return m.group(1) if m else None


def start_program(program, port=8951):
    """Starts our program with a throwaway results file; returns (process, base URL)."""
    import subprocess, tempfile
    data = os.path.join(tempfile.mkdtemp(), "results.csv")
    proc = subprocess.Popen([program, "-no-browser", "-port", str(port), "-data", data],
                            stdout=subprocess.DEVNULL)
    base = "http://127.0.0.1:%d/" % port
    for _ in range(50):
        try:
            urllib.request.urlopen(base + "ping", timeout=1)
            return proc, base
        except OSError:
            time.sleep(0.1)
    proc.kill()
    sys.exit("could not start " + program)


def check(args):
    paths = sorted(glob.glob(os.path.join(FIXTURES, "*.json")))
    if not paths:
        sys.exit("no fixtures in %s; run 'record' first" % FIXTURES)
    proc = None
    if args.program:
        proc, local = start_program(args.program)
    else:
        local = args.local.rstrip("/") + "/"
    try:
        _check(paths, local, args.verbose)
    finally:
        if proc:
            proc.kill()


def _check(paths, local, verbose):
    failures = skipped = 0

    for path in paths:
        with open(path) as f:
            fx = json.load(f)
        form = dict(fx["request"])
        sex = SEX_CODES.get(form.get("Sex"))
        if sex is None:
            skipped += 1
            print("SKIP %s: sex code %r not supported locally" % (os.path.basename(path), form.get("Sex")))
            continue
        form["Sex"] = sex
        want = parse_results(fx["results_html"])
        got = json.loads(post(local + "results_api", sorted(form.items())))

        bad = ["%s: official=%s ours=%s" % (k, want.get(k), got.get(k))
               for k in sorted(set(want) | set(got)) if want.get(k) != got.get(k)]

        # The norm group ("men between 21 and 40 years of age") must match too.
        want_cat = parse_category(fx["results_html"])
        got_cat = parse_category(post(local + "results", sorted(form.items())))
        if want_cat != got_cat:
            bad.append("norm group: official=%r ours=%r" % (want_cat, got_cat))

        if bad:
            failures += 1
            print("FAIL %s (%s, age %s)\n  %s" % (os.path.basename(path), sex, form["Age"],
                                                 "\n  ".join(bad)))
        elif verbose:
            print("ok   %s" % os.path.basename(path))

    checked = len(paths) - skipped
    print("%d fixtures checked, %d failed, %d skipped" % (checked, failures, skipped))
    sys.exit(1 if failures else 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    r = sub.add_parser("record", help="run random cases through a local copy of the official scripts")
    r.add_argument("--official", required=True,
                   help="base URL of the local copy, e.g. http://127.0.0.1:8080/cgi-bin/")
    r.add_argument("-n", type=int, default=100, help="number of cases (default 100)")
    r.add_argument("--delay", type=float, default=0, help="seconds between cases")
    r.add_argument("--seed", type=int, default=None, help="random seed")
    c = sub.add_parser("check", help="compare saved fixtures against a local server (offline)")
    c.add_argument("--local", default="http://127.0.0.1:8888/", help="local server base URL")
    c.add_argument("--program", help="start this program (e.g. dist/linux/...) instead of using --local")
    c.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()
    if args.cmd == "record":
        record(args)
    elif args.cmd == "check":
        check(args)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
