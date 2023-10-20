#!/usr/bin/python3
"""Hello HBNB from Flask."""
from flask import Flask, render_template

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
    """C route."""
    text_fix = f'{text}'.replace('_', ' ')
    return f'C {text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_page(text="is cool"):
    """Python route"""
    text_fix = f'{text}'.replace('_', ' ')
    return f'Python {text_fix}'


@app.route('/number/<int:n>', strict_slashes=False)
def number_page(n):
    """Number route"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_page(n):
    """Number template route"""
    return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odven_page(n):
    """Check if the number is odd or even

    Args:
        n (int): the number to check
    """
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
