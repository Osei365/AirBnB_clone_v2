#!/usr/bin/python3
"""flask app to handle state, amenities, cities"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def handle_teardown(exception):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display():
    states = storage.all(State)
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states, am=amenities)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
