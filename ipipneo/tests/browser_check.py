#!/usr/bin/env python3
"""
Renders the results page in a real (headless) Chrome and checks that the
jqPlot charts draw with the right scores, i.e. that jqPlot still works with
the bundled jQuery. Uses the locally installed Chrome, so unlike the other
tests this one is NOT hermetic.

Usage: browser_check.py <program> [chrome binary]
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request

PORT = 8941
# tests/reference.dat: a 28-year-old man; official EXTRAVERSION graph values.
ANSWERS = ("455454245414355144252442444444435454354214445435053442424254"
           "455453415314242354554251515543245452445414245444452135425154")
WANT = ["76", "82", "64", "63", "88", "26", "84"]

CHROMES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
]


def main():
    program = sys.argv[1]
    chrome = sys.argv[2] if len(sys.argv) > 2 else next(
        (c for c in CHROMES if shutil.which(c) or os.path.exists(c)), None)
    if not chrome:
        sys.exit("no Chrome/Chromium found; pass its path as the second argument")

    work = tempfile.mkdtemp()
    server = subprocess.Popen([program, "-no-browser", "-port", str(PORT),
                               "-data", os.path.join(work, "results.csv")],
                              stdout=subprocess.DEVNULL)
    try:
        for _ in range(50):
            try:
                urllib.request.urlopen("http://127.0.0.1:%d/ping" % PORT, timeout=1)
                break
            except OSError:
                time.sleep(0.1)

        # Chrome can only GET from the command line, so a local page posts the form.
        fields = {"Nick": "browsertest", "Sex": "1", "Gender": "8", "Age": "28", "Country": "India"}
        fields.update(("Q%d" % (i + 1), c) for i, c in enumerate(ANSWERS))
        inputs = "".join('<input type="hidden" name="%s" value="%s">' % kv for kv in fields.items())
        page = os.path.join(work, "submit.html")
        with open(page, "w") as f:
            f.write('<html><body onload="document.forms[0].submit()">'
                    '<form method="post" action="http://127.0.0.1:%d/results">%s</form>'
                    '</body></html>' % (PORT, inputs))

        dom = subprocess.run(
            [chrome, "--headless=new", "--disable-gpu", "--no-first-run",
             "--user-data-dir=" + os.path.join(work, "profile"),
             "--virtual-time-budget=8000", "--dump-dom", "file://" + page],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, timeout=120).stdout.decode()
    finally:
        server.kill()
        shutil.rmtree(work, ignore_errors=True)

    labels = re.findall(r'jqplot-point-label[^>]*>(\d+)', dom)
    if len(labels) != 35 or labels[:7] != WANT:
        sys.exit("FAIL: expected 35 chart labels starting %s, got %s" % (WANT, labels))
    print("browser check OK: 5 charts, 35 scores, EXTRAVERSION = %s" % " ".join(labels[:7]))


if __name__ == "__main__":
    main()
