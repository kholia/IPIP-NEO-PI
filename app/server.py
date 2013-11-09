#!/usr/bin/env python

import bottle
import evaluator
import sqlite3
import traceback

bottle.BaseRequest.MAX_PARAMS = 10000
app = bottle.Bottle()


@app.route('/static/<filename>')
def server_static(filename):
    return bottle.static_file(filename, root='/path/to/your/static/files')


@app.route('/')
def ipipneo120():
    return bottle.template('index')


@app.route('/shortipipneo', method='POST')
def shortipipneo():
    # print(bottle.request.body.readlines())
    return bottle.template('shortipipneo')


@app.route('/results', method='POST')
def results():
    # print(bottle.request.body.readlines())
    return evaluator.evaluate(bottle.request, db)


@app.route('/graph', method='GET')
def graph():
    return bottle.template("graph")


# Static Routes
@app.get(r'/js/<filename:re:.*\.js>')
def javascripts(filename):
    return bottle.static_file(filename, root='static/js')


@app.get(r'/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return bottle.static_file(filename, root='static/css')


@app.get(r'/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return bottle.static_file(filename, root='static/images')


@app.get(r'/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return bottle.static_file(filename, root='static/fonts')


table_create_sql = """ CREATE TABLE IF NOT EXISTS RESULTS (
    TIMESTAMP   TIMESTAMP  NOT NULL,
    Gender      TEXT       NOT NULL,
    Age         INT        NOT NULL,
    Nick        TEXT       NOT NULL,
    Country     TEXT       NOT NULL,
    Responses   TEXT       NOT NULL); """


if __name__ == "__main__":
    # setup database
    dbfile = "results.db"
    start = True

    try:
        db = sqlite3.connect(dbfile)

        db.execute(table_create_sql)

    except sqlite3.DatabaseError:
        start = False
        traceback.print_exc()

    except sqlite3.OperationalError as e:
        start = False
        traceback.print_exc()

    if start:
        bottle.run(app=app, host='localhost', port=8888,
                   debug=True, reloader=True)
