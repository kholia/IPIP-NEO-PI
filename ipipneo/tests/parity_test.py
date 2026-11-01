#!/usr/bin/env python3
"""
Parity test: the original Python/Bottle app vs. the Go builds.

Posts the same randomized test submissions to every server and checks that
/results_api JSON is byte-identical, /results HTML matches (ignoring
whitespace and HTML comments), and the saved rows agree.

Run via run_parity.sh (inside a pinned python:3.8 container).

Usage: parity_test.py <python app dir> <go binary>...
"""

import csv
import html
import os
import random
import re
import sqlite3
import subprocess
import sys
import tempfile
import time
import urllib.parse
import urllib.request

API_ROUNDS = 3000
HTML_ROUNDS = 300

SEX_CODES = {"Male": "1", "Female": "2"}
GENDERS = ["Male", "Female", "Nonbinary", "Gender Fluid", "Gender Queer", "Gender Neutral",
           "Questioning/Exploring", "Prefer not to answer"]

AGES = [10, 11, 19, 20, 21, 22, 39, 40, 41, 42, 59, 60, 61, 62, 99]
COUNTRIES = ["India", "United States", "Cote d'Ivoire", "Trinidad & Tobago"]


def post(url, form):
    data = urllib.parse.urlencode(form).encode()
    with urllib.request.urlopen(url, data, timeout=30) as r:
        return r.read().decode("utf-8")


def wait_up(base):
    for _ in range(100):
        try:
            urllib.request.urlopen(base, timeout=1).read()
            return
        except Exception:
            time.sleep(0.2)
    sys.exit("server did not start: " + base)


def random_form(rng):
    form = {
        "Nick": rng.choice(["", "hello", "Nick %d" % rng.randint(0, 999), "x<y>&\"z'"]),
        "Sex": rng.choice(["Male", "Female"]),
        "Age": str(rng.choice(AGES + [rng.randint(10, 100)])),
        "Country": rng.choice(COUNTRIES),
        "Gender": str(rng.randint(1, 8)),
    }
    mode = rng.random()
    for i in range(1, 121):
        if mode < 0.05 and rng.random() < 0.3:
            continue  # unanswered item
        if mode < 0.15:
            form["Q%d" % i] = str(rng.choice([1, 5]))  # extreme scores
        elif mode < 0.25:
            form["Q%d" % i] = "3"
        else:
            form["Q%d" % i] = str(rng.randint(1, 5))
    return form


def norm_html(s):
    # Only the report itself: the <head> (stylesheets, script versions)
    # differs on purpose.
    s = s[s.index("<body>"):]
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = s.replace("&#039;", "&#39;").replace("&#34;", "&quot;")
    return re.sub(r"\s+", "", s)


def main():
    app_src, go_bins = sys.argv[1], sys.argv[2:]
    work = tempfile.mkdtemp()
    subprocess.check_call(["cp", "-r", app_src, work + "/app"])

    procs = [subprocess.Popen([sys.executable, "server.py"], cwd=work + "/app",
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)]
    servers = {"python": "http://localhost:8888/"}
    csvs = {}
    for n, b in enumerate(go_bins):
        port = 8901 + n
        csvs[b] = os.path.join(work, "go%d.csv" % n)
        procs.append(subprocess.Popen([b, "-no-browser", "-port", str(port), "-data", csvs[b]],
                                      stdout=subprocess.DEVNULL))
        servers[os.path.basename(b)] = "http://127.0.0.1:%d/" % port

    failures = 0
    try:
        for base in servers.values():
            wait_up(base)

        rng = random.Random(1234)
        for rnd in range(API_ROUNDS + HTML_ROUNDS):
            form = random_form(rng)
            endpoint = "results_api" if rnd < API_ROUNDS else "results"
            # The Go version takes the official site's numeric sex codes; the
            # 2021 Python version only knows "Male" / "Female".
            go_form = dict(form, Sex=SEX_CODES[form["Sex"]])
            out = {name: post(base + endpoint, form if name == "python" else go_form)
                   for name, base in servers.items()}
            if endpoint == "results":
                out = {k: norm_html(v) for k, v in out.items()}
            ref = out.pop("python")
            for name, got in out.items():
                if got != ref:
                    failures += 1
                    print("MISMATCH %s %s form=%r\n  python=%s\n  go    =%s"
                          % (name, endpoint, form, ref[:300], got[:300]))

        # Compare saved rows from the /results submissions (first six columns
        # match the old database; the Go version adds gender identity).
        db = sqlite3.connect(work + "/app/results.db")
        want = [list(map(str, r[1:])) for r in db.execute("SELECT * FROM RESULTS")]
        rng = random.Random(1234)
        genders = [GENDERS[int(random_form(rng)["Gender"]) - 1]
                   for _ in range(API_ROUNDS + HTML_ROUNDS)][API_ROUNDS:]
        for b, path in csvs.items():
            with open(path, encoding="utf-8-sig", newline="") as f:
                rows = list(csv.reader(f))
            got = [[c.lstrip("'") for c in r[1:6]] for r in rows[1:]]
            if [r[6] for r in rows[1:]] != genders or got != want:
                failures += 1
                print("MISMATCH saved rows %s (%d vs %d rows)" % (b, len(got), len(want)))
                for g, w in zip(got, want):
                    if g != w:
                        print("  python=%r\n  go    =%r" % (w, g))
                        break

        # Go-only behavior: validation pages, intersex, the items page.
        for b, base in list(servers.items())[1:]:
            msg = post(base + "results", {"Sex": "", "Gender": "1", "Age": "30"})
            assert "did not indicate your sex assigned at birth" in msg, msg
            msg = post(base + "results", {"Sex": "1", "Age": "30"})
            assert "did not indicate your gender identity" in msg, msg
            msg = post(base + "results", {"Sex": "1", "Gender": "1", "Age": "abc"})
            assert "did not indicate how old" in msg, msg
            msg = post(base + "results", {"Sex": "3", "Gender": "9", "OtherGender": "Two-Spirit",
                                          "Age": "30", "Nick": "inter", "Q1": "4"})
            assert "Your responses have been saved" in msg, msg
            page = urllib.request.urlopen(base + "reporting").read().decode()
            assert "GenderIdentity" in page and "Two-Spirit" in page, page[:500]
            for p in ["css/site.css", "js/jquery-3.7.1.min.js", "js/jquery.jqplot.js", "favicon.ico"]:
                urllib.request.urlopen(base + p).read()
            page = post(base + "shortipipneo", {})
            assert "Failure to Acknowledge" in page, page[:300]
            page = post(base + "shortipipneo", {"Accuracy": "Yes"})
            assert page.count('NAME="Q') == 600 and 'NAME="Gender"' in page, page[:300]
    finally:
        for p in procs:
            p.kill()

    total = (API_ROUNDS + HTML_ROUNDS) * len(go_bins)
    print("%d comparisons against Python, %d failures" % (total, failures))
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
