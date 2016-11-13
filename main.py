from flask import Flask
from flask import redirect
from flask import render_template
from flask import url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongodb0.example.net:27017")

@app.route('/')
def hello_world():
    return '<H1>Hello World!</h1>'


@app.route('/mongo')
def hello_mongo():
    print url_for('hello_mongo')
    return render_template('other.html')

@app.route('/show_entries')
def hello_entires():
    print url_for('show_entries')
    return render_template('other.html')


if __name__ == '__main__':
    app.run()
