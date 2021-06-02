#!/usr/bin/env python3

"""
Historial reporting module.
"""

import json
import datetime
import collections

import bottle


def show(request, db=None):
    """API endpoint."""

    results = db.execute("SELECT * from RESULTS").fetchall()

    return bottle.template('reporting', rows=results)


def evaluate(request, db=None):

    """Personality evaluation logic."""

    SEP, SEFP, LO, HI, SE, SAP, SAFP, SA, SC, SCP, SCFP, flev, SOP, SOFP, SO, \
            Nick, Country, SNP, SNFP, Category, SN, Sex, Age, Q = evaluate_api(request)

    # Check sex and age
    if Sex != "Male" and Sex != "Female":
        return """You did not indicate your sex at the beginning of the
    inventory. Your answers cannot be normed properly unless you indicate
    whether you are male or female. Please return to the inventory and indicate
    your sex."""

    if Age < 10:
        return """You did not indicate how old you are at the beginning of the
    inventory, or you typed in an age that is too young. Your answers cannot be
    normed properly unless type in a valid age. Please return to the inventory
    and change your response."""

    # Save Data
    if db:
        responses = " ".join([str(i) for i in Q[1:121]])

        db.execute('insert into RESULTS values(?, ?, ?, ?, ?, ?)',
                   (datetime.datetime.now(), Sex, Age, Nick, Country,
                    responses))
        db.commit()

    return bottle.template(
        'results', SEP=SEP, SEFP=SEFP,
        LO=45, HI=55, SE=SE, SAP=SAP, SAFP=SAFP, SA=SA,
        SC=SC, SCP=SCP, SCFP=SCFP, flev=flev,
        SOP=SOP, SOFP=SOFP,
        SO=SO, Nick=Nick, Country=Country,
        SNP=SNP, SNFP=SNFP, Category=Category,
        SN=SN)
