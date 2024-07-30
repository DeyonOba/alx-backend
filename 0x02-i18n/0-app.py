#!/usr/bin/env python3
"""
Setup a basic Flask app. Create a single / route and an index.html
template that simply outputs "Welcome to Holberton" as page title
(<title>) and "Hello world"(<h1>).
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """Set up a single / route."""
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run(debug=True)
