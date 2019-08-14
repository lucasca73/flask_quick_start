from flask import Flask, escape, render_template, url_for

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

@app.route('/render/<name>')
def render(name=None):
    return render_template('hello.html', name=name)
