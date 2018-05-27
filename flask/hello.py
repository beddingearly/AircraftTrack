# codeing=utf-8
from flask import Flask, jsonify, session, url_for, Response
from flask import request
from flask import render_template

import time
import sqlite3
import argparse
import csv
import logging
import sys
sys.path.append('../gr-air-modes/apps')
from get_history_track import SqliteOperator

app = Flask(__name__)


@app.route('/')
def hello():
    #a = SqliteOperator('../database/2018-4-15.db', 'ident', 'CCA102', '', '')
    #a.test()

    return render_template('front.html')


@app.route('/showmap')
def ShowMap(name=None):
    return render_template('track.html', name=name)


@app.route('/ddd')
def ShowHistory():
    keyvalue = str(request.args.get('ddd'))
    a = SqliteOperator('../database/2018-4-15.db', 'ident', keyvalue, '', '')
    aa = a.get_message()

    return jsonify(aa)


# return render_template('pass.html', name=a)

def database(dbname):
    pass


if __name__ == '__main__':

    app.debug = True
    app.run(port=5000)
