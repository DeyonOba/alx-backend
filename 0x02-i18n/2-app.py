#!/usr/bin/env python3
"""
Ensure that Babel Flask extension is installed:
`pip3 install flask_babel==2.0.0`

Then instantiate the `Babel` object in your app. Store it in a
module-level variable named `babel`.

In order to confifure available languages in our app, you will create
a `Config` class that has a `LANGUAGES` class attribute equal to
['en', 'fr'].

Use that class as config for your Flask app.
"""
from flask import (
    Flask,
    request,
    render_template,
)
from flask_babel import Babel


class Config:
    """Babel Configurations."""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """Set up a single / route."""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
