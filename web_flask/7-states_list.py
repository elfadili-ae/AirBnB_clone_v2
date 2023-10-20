#!/usr/bin/python3
"""Flask web app."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_context(exception):
    """Close storage when teardown"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    """States list

    Returns:
        template: states template
    """
    return render_template("7-states_list.html", states=storage.all("State"))


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
