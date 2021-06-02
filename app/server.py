#!/usr/bin/env python3

"""
Main app server.
"""

import sqlite3
import traceback

import evaluator
import reporting

import bottle

bottle.BaseRequest.MAX_PARAMS = 10000
app = bottle.Bottle()
CFG = {'DB': None}

@app.route('/')
def ipipneo120():
    """
    Show the 'homepage'.
    """

    return bottle.template('index')


@app.route('/shortipipneo', method='POST')
def shortipipneo():
    """
    Show the 'short test'.
    """
    # print(bottle.request.body.readlines())
    return bottle.template('shortipipneo')


@app.route('/results', method='POST')
def results():
    """
    Generate and display the 'results' page.
    """
    # print(bottle.request.body.readlines())
    return evaluator.evaluate(bottle.request, CFG['DB'])

@app.route('/reporting', method='GET')
def show():
    """
    Historial reporting page
    """
    # print(bottle.request.body.readlines())
    return reporting.show(bottle.request, CFG['DB'])

@app.route('/results_api', method='POST')
def results_api():
    """
    The "results API".
    """
    return evaluator.evaluate_api(bottle.request)


@app.route('/graph', method='GET')
def graph():
    """
    Displays 'graph'.
    """
    return bottle.template("graph")


# Static Routes
@app.get(r'/js/<filename:re:.*\.js>')
def javascripts(filename):
    """
    Static handler for JS files.
    """
    return bottle.static_file(filename, root='static/js')

@app.get(r'/favicon.ico')
def favicon():
    """
    Static handler for favicon.
    """

    return bottle.static_file("favicon.ico", root='static')

@app.get(r'/css/<filename:re:.*\.css>')
def stylesheets(filename):
    """
    Static handler for CSS files.
    """
    return bottle.static_file(filename, root='static/css')


@app.get(r'/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    """
    Handler for images.
    """
    return bottle.static_file(filename, root='static/images')


@app.get(r'/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    """
    Handler for fonts.
    """
    return bottle.static_file(filename, root='static/fonts')


def main():
    """
    Program starts here.
    """
    # setup database
    dbfile = "results.db"
    start = True
    table_create_sql = """CREATE TABLE IF NOT EXISTS RESULTS (
        TIMESTAMP   TIMESTAMP  NOT NULL,
        Gender      TEXT       NOT NULL,
        Age         INT        NOT NULL,
        Nick        TEXT       NOT NULL,
        Country     TEXT       NOT NULL,
        Responses   TEXT       NOT NULL);"""
    try:
        CFG['DB'] = sqlite3.connect(dbfile)
        CFG['DB'].execute(table_create_sql)
    except sqlite3.DatabaseError:
        start = False
        traceback.print_exc()

    except sqlite3.OperationalError:
        start = False
        traceback.print_exc()

    if start:
        bottle.run(app=app, host='localhost', port=8888,
                   debug=True, reloader=True)

if __name__ == "__main__":
    main()
