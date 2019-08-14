from flask import Flask, escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hey cara!'

@app.route('/user/<username>')
def user(username):
    return 'Hello %s' % escape(username)