#!/usr/bin/python3
"""Flask web app."""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(exception):
    """Close storage when teardown"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities():
    """Cities by states list

    Returns:
        template: cities template
    """
    states = storage.all("State")
    citites = storage.all("City")
    return render_template("8-cities_by_states.html", states=states, cities=citites)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
