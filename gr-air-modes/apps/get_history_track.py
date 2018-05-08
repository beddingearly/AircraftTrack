#coding=utf-8

import sqlite3
import argparse
import csv
import logging
from lxml import etree
from pykml.parser import Schema
from pykml.factory import KML_ElementMaker as KML
from pykml.factory import GX_ElementMaker as GX


class SqliteOperator(object):

    def __init__(self, database, table, ident, csvfile, kmlfile):
        self.database = database
        self.table = table
        self.ident = ident
        self.csvfile = csvfile
        self.kmlfile = kmlfile

        self.c = self.connect_database()
        self.icao = self.get_icao()
        self.message = self.get_message()


    def connect_database(self):
        conn = sqlite3.connect(self.database)
        return conn.cursor()

    def get_icao(self):
        sql = "SELECT icao from " + self.table +" where ident like '%"+self.ident+"%'"

        ident = self.c.execute(sql)

        icao = ident.fetchone()[0]
        return icao

    def get_message(self):

        sql1 = "SELECT seen, speed, heading, vertical from vectors where icao="+str(self.icao)
        v = self.c.execute(sql1)

        # [(u'2018-04-15 11:30:04', 513.0, 27.0, 0.0), (u'2018-04-15 11:30:06', 513.0, 27.0, 0.0),
        self.vectors = v.fetchall()


        sql2 = "SELECT seen, alt, lat, lon from positions where icao="+str(self.icao)
        p = self.c.execute(sql2)

        # [(u'2018-04-15 11:30:05', 24600, 30.545763, 114.129108), (u'2018-04-15 11:30:06', 24600, 30.54702, 114.129822),
        self.positions = p.fetchall()

        message = []
        for vector in self.vectors:
            for position in self.positions:
                if vector[0] == position[0]:
                    msg = (vector[0],
                           self.ident,
                           self.get_icao(),
                           position[1],
                           position[2],
                           position[3],
                           vector[1],
                           vector[2],
                           vector[3])
                    message.append(msg)

                    break

        return message

    def write_to_csv(self):
        csvFile = open(self.csvfile, 'wb')
        writer = csv.writer(csvFile)
        head = ['UTC','航班号','识别码', '海拔', '经度', '纬度', '速度', '方向','垂直速度']
        writer.writerow(head)

        for msg in self.message:
            writer.writerow(msg)

        csvFile.close()

    def write_to_kml(self):
        retstr = """<?xml version="1.0" encoding="UTF-8"?>\n"""

        doc = KML.kml(
            KML.Document(
                KML.Style({"id": "airplane"},
                          KML.IconStyle(
                              KML.Icon(
                                  KML.href("airports.png")
                              )
                          )
                          ),
                KML.Style({"id": "rangering"},
                          KML.LineStyle(
                              KML.color("9f4f4faf"),
                              KML.width(2)
                          )
                          ),
                KML.Style({"id": "track"},
                          KML.LineStyle(
                              KML.color("5fff8f8f"),
                              KML.width(4)
                          )
                          ),
                KML.Folder(
                    KML.name("Aircraft locations"),
                    KML.open(0),
                    KML.Placemark(
                        KML.name("CCA1360"),
                        KML.Style(
                            KML.IconStyle(
                                KML.heading(90)
                            )
                        ),
                        KML.styleUrl("#airplane"),
                        KML.description(
                            "Altitude: {}<br/>Heading: {} <br/>Speed: {}<br/>Vertical speed:{}<br/>ICAO: {}<br/>Last seen: {} <img src='../../CCA.jpg' width='300px' height='200px'/>".format(1,2,3,4,5,6)

                        ),

                        KML.Point(
                            KML.altitudeMode("absolute"),
                            KML.extrude(1),
                            KML.coordinates(114.566668, 30.455795, 8869)
                        )
                    ),
                    KML.Placemark(
                        KML.styleUrl("#track"),
                        KML.LineString(
                            KML.extrude(0),
                            KML.altitudeMode("absolute"),
                            KML.coordinates(114.566668, 30.455795, 8869.680000)
                        )
                    )

                )
            )

        )

        outfile = open('out.kml', 'wb')
        outfile.write(retstr)
        outfile.write(etree.tostring(doc, pretty_print=True))



    def update_kml(self):
        pass


def parse_arge():
    parser = argparse.ArgumentParser(description='history track look back')

    parser.add_argument('--database', type=str, help='choose a database to operate')
    parser.add_argument('--table', type=str, help='choose a table to operate')
    parser.add_argument('--plane', type=str, help='choose a plane')
    parser.add_argument('--csvfile', type=str, help='create a csv file')
    parser.add_argument('--kmlfile', type=str, help='create a kml file')

if __name__ == '__main__':
    database = "2018-4-15.db"
    table = "ident"
    ident = "CES2738" # missing two space
    csvfile = 'output.csv'
    kmlfile = 'output.kml'
    a = SqliteOperator(database, table, ident, csvfile, kmlfile)
    a.write_to_kml()