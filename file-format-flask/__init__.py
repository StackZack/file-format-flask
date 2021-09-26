from flask import Flask
from .json_reader.reader import json_reader_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(json_reader_bp, url_prefix="/json")

    return app
