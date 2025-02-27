#!/usr/bin/python3
"""
A Script that starts a Flask web application
"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    """
    Remove current SQLAlchemy Session after each request
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def filters():
    """
    Display a HTML page like 8-index.html
    """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    sorted_states = sorted(states, key=lambda x: x.name)
    sorted_cities = sorted(cities, key=lambda x: x.name)
    sorted_amenities = sorted(amenities, key=lambda x: x.name)
    sorted_places = sorted(places, key=lambda x: x.name)

    return render_template('100-hbnb.html', states=sorted_states,
                           cities=sorted_cities, amenities=sorted_amenities,
                           places=sorted_places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
