#!/usr/bin/env python3

"""Extracts contents of results.db into results.csv file."""

import sqlite3
import csv


con = sqlite3.connect('results.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM RESULTS")

    rows = cur.fetchall()

    with open("results.csv", "a") as f:
        writer = csv.writer(f, delimiter=',')
        for row in rows:
            timestamp, gender, age, nick, country, answers = row
            output = [nick, gender, age, country, timestamp, answers]
            writer.writerow(output)
