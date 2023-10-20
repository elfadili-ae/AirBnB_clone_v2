#!/usr/bin/python3
"""Hello HBNB from Flask."""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Hello Home."""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """Hbnb route."""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_page(text):
    text_fix = f'{text}'.replace('_', ' ')
    return f'C {text}'

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_page(text="is cool"):
    text_fix = f'{text}'.replace('_', ' ')
    return f'Python {text_fix}'

@app.route('/number/<n>', strict_slashes=False)
def number_page(n):
    try:
        num = int(n)
        return f'{n} is a number'
    except Exception:
        abort(404)
