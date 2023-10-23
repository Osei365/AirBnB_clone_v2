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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = storage.all(State).values()
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
