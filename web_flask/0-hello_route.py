#!/usr/bin/python3
"""Hello HBNB from Flask."""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Hello Home."""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
