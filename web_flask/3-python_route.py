#!/usr/bin/python3
"""defining a flask app."""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    text = text.replace('_', ' ')
    return 'python {}'.format(escape(text))


if __name__ == "__main__":
    """command line"""
    app.run('0.0.0.0', 5000)
