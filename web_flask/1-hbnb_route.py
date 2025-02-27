#!/usr/bin/python3
""" Flask web application """
from flask import Flask

app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def hello_route():
    """Default route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Return 'HBNB'"""
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
