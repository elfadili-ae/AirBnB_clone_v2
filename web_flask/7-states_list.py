#!/usr/bin/python3
"""Flask web app."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list")
def states():
    return "states"


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
