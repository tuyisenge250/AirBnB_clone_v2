#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
    /hbnb: Displays 'HBNB'
    /c/<text>: Display 'C' followed by the value of the text variable
    /python/<text>: Display "python" followed by the value of text variable(if contain _ replace by space)
"""

from flask import Flask

app = Flask(__name__)

@app.route('/',strict_slashes=False)
def hello_hbnb():
    """display hello HBNB"""
    return  "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display 'C' followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f'C {text}'
@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Display "python" followed by the value of text variable(if contain _ replace by space)"""
    text = text.replace("_", " ")
    return f"python {text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0")