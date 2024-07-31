#!/usr/bin/env python3
"""a module that initializes and configures babel"""
from flask_babel import Babel
from flask import Flask, render_template


app = Flask(__name__)


class Config:
    """class Config that defines the babel configuration on our app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


babel = Babel(app)
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def home():
    """home route func definition"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
