#!/usr/bin/env python

"""Extracts contents of results.db into results.csv file."""

import sqlite3
import csv


con = sqlite3.connect('results.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM RESULTS")

    rows = cur.fetchall()

    with open("results.csv", "ab") as f:
        writer = csv.writer(f, delimiter=',')
        for row in rows:
            timestamp, gender, age, nick, country, answers = row
            answers = list(map(int, answers.split()))
            output = [nick, gender, age, country, timestamp]
            output.extend(answers)
            writer.writerow(output)
