# codeing=utf-8
from flask import Flask, jsonify, session, url_for, Response
from flask import request
from flask import render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/showmap')
def ShowMap(name=None):
    return render_template('track.html', name=name)

@app.route('/ddd')
def Showpass(name=None):
	a = ['111','222',5]
	b = 222
	c = 333
	#return jsonify(a, b, c)
	return render_template('pass.html', name=a)

def database(dbname):
    pass


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
