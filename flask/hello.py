# coding=utf-8
from flask import Flask, jsonify, session, url_for, Response
from flask import request
from flask import render_template
from pykml import parser
import xml.etree.ElementTree as ET
from lxml import etree
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
def showMap(name=None):
    return render_template('bmap.html', name=name)



@app.route('/showmap2')
def showMap2():
    return render_template('breal.html')

@app.route('/search')
def ShowHistory():
    keyvalue = str(request.args.get('search'))
    a = SqliteOperator('../database/2018-4-15.db', 'ident', keyvalue, '', '')
    aa = a.get_message()
    return jsonify(aa)

@app.route('/message')
def showMessage():
    return render_template('message.html')


@app.route('/parse')
def parseKML():
    filename = str(request.args.get('filename'))
    print(filename)
    filename = '../gr-air-modes/apps/test0416.kml'
    #filename = '../../out.kml'
    tree = ET.parse(filename)
    root = tree.getroot()
    planes = []
    for Document in root:
        for Style in Document:
            print(Style)
            if Style.tag.split('}')[1] == 'Folder':
                for Folder in Style:

                    if Folder.tag.split('}')[1] == 'Placemark':
                        plane = []
                        for msg in Folder:

                            # name
                            if msg.tag.split('}')[1] == 'name':
                                name = msg.text
                                plane.append(name)

                            # heading
                            elif msg.tag.split('}')[1] == 'Style':
                                for IconStyle in msg:
                                    for heading in IconStyle:
                                        #print(heading.text)
                                        heading = heading.text
                                        plane.append(heading)

                            # Point
                            elif msg.tag.split('}')[1] == 'Point':
                                for coordinates in msg:
                                    if coordinates.tag.split('}')[1] == 'coordinates':
                                        #print(coordinates.text)
                                        coordinates = coordinates.text
                                        plane.append(coordinates)

                            # description
                            elif msg.tag.split('}')[1] == 'description':
                                #print(msg.text)
                                description = msg.text
                                plane.append(description)

                            if (len(plane) != 0 and len(plane) == 4):
                                planes.append(plane)

                            # styleUrl tracking 轨迹
    print (planes)
    return jsonify(planes)



if __name__ == '__main__':

    app.debug = True
    app.run(port=5003)
