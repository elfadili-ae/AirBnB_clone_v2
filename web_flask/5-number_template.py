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
    """c is fun"""
    text_fix = f'{text}'.replace('_', ' ')
    return f'C {text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_page(text="is cool"):
    """python is magic."""
    text_fix = f'{text}'.replace('_', ' ')
    return f'Python {text_fix}'


@app.route('/number/<n>', strict_slashes=False)
def number_page(n):
    """random freaking number"""
    try:
        num = int(n)
        return f'{num} is a number'
    except Exception:
        abort(404)

@app.route('/number_template/<n>', strict_slashes=False)
def template_page(n):
    try:
        num = int(n)
        return render_template("5-number.html", num=n)
    except Exception:
        abort(404)


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
