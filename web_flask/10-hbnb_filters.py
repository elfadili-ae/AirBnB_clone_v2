#!/usr/bin/python3
"""Flask web app."""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(exception):
    """Close storage when teardown"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """Cities by states list

    Returns:
        template: cities template
    """
    states = storage.all("State")
    cities = storage.all("City")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           states=states,
                           cities=cities,
                           amenities=amenities)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
