#!/usr/bin/python3
"""defining a flask app."""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"


if __name__ == "__main__":
    """command line"""
    app.run('0.0.0.0', 5000)
