#!/usr/bin/env python3
"""a module that instantiates and configures a babel extension"""
from flask_babel import Babel, _
from flask import Flask, request, render_template


app = Flask(__name__)


class Config:
    """class that defines our app's babel configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """gets the locale language"""
    return request.accept_languages.best_match(app.Config[LANGUAGES])


@app.route('/', strict_slashes=False)
def index():
    """returns the home page of our app"""
    home_title = _("home_title")
    home_header = _("home_header")
    return render_template(
            '3-index.html',
            home_title=home_title,
            home_header=home_header
            )


if __name__ == '__main__':
    app.run()
