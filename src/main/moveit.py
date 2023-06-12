import os

from flask import Flask


def static_folder() -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../static')


def template_folder() -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../templates')


def create_app(config):
    app: Flask = Flask(__name__)

    app.template_folder = template_folder()
    app.static_folder = static_folder()

    app.config['SECRET_KEY'] = config.SECRET_KEY

    return app
