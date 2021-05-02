#!/usr/bin/python3
""" Flask web application """
from flask import Flask

app = Flask('web_flask')
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    """Default route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    """Return 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    """ Return text from URL """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python/', defaults={'text': 'is cool'})
def python_route(text):
    """Return 'Python ' followed by text from html request with
    default text 'is cool'"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_route(n):
    """Return last part of html request formatted as a number if
    it can be converted to an int"""
    return '{:d} is a number'.format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
