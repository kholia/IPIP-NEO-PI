#!/usr/bin/env python3
# pylint: disable=C0103,R0912,R0914,R0915,W0613

"""
Randomly compares the output of the upstream website against the local website.
"""

import sys
import random
import signal

import requests
from pyquery import PyQuery as pq

stats = {"pass_count": 0, "fail_count": 0}


def signal_handler(sig, frame):
    """
    Ctrl+C handler"
    """
    print('\n')
    print("[+] Total PASS count is (%s)", stats["pass_count"])
    print("[!] Total FAIL count is (%s)", stats["fail_count"])
    sys.exit(0)


def run():
    """
    Run one random test case.

    Returns True for PASS.

    Returns False for FAIL.
    """

    nick = "Testing Please Ignore"
    age = "28"

    N = 120  # 120 questions
    answers = []
    for i in range(0, N):
        answers.append(random.randint(1, 5))
        # answers.append(3)

    # Common data
    data = {"Nick": nick, "Sex": "Male", "Age": age, "Country": "Afghanistan"}
    for i in range(0, N):
        data["Q%s" % (i+1)] = answers[i]

    # Test upstream first
    m = {}
    # base_url = "http://www.personal.psu.edu/cgi-bin/users/j/5/j5j/IPIP/shortipipneo3.cgi"
    base_url = "http://localhost/cgi-bin/shortipipneo3.cgi"
    r = requests.post(base_url, data=data)
    d = pq(r.text)
    for table in d("table"):
        trs = list(pq(table)("tr"))
        trs = trs[1:]  # skip over table header ("DOMAIN/Facet")
        for tr in trs:
            ds = pq(tr)
            tds = list(ds("td"))
            label, score = tds[0:2]
            score = score.text
            label = label.text.lstrip("..")
            m[label] = int(score)

    # Test local now
    base_url = "http://localhost:8888/results_api"
    n = {}
    r = requests.post(base_url, data=data)
    n = r.json()

    failed = False
    for k, v in n.items():
        if v != m.get(k, None):
            # print("[!] FAILED for (Local, %s, %s) vs (Upstream, %s)" % (k, v, m.get(k, None)))
            failed = True

    if not failed:
        stats["pass_count"] = stats["pass_count"] + 1
    else:
        stats["fail_count"] = stats["fail_count"] + 1
        L = 150
        print("-" * L)
        print(data)
        print("Upstream:", m)
        print("Local:", n)
        for k, v in n.items():
            if v == m.get(k, None):
                print("[!] FAILED for (Local, %s, %s) vs (Upstream, %s)" % (k, v, m.get(k, None)))
        print("-" * L, "\n")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to stop testing and print stats...')
    while True:
        run()
