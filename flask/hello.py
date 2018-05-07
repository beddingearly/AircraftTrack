# codeing=utf-8
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/showmap')
def ShowMap(name=None):
    return render_template('test1.html', name=name)


def database(dbname):
    pass


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)
