from flask import Flask, make_response

app = Flask(__name__)

name = "Dave"

@app.route('/user/<name>')
def hello(name):
    return '<h1> Hello, %s!</h1>' % name


@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

if __name__ == '__main__':
    app.run(debug=True)