"""Base Flask application that registers all required components.
"""

from flask import Flask
from .json_reader.reader import json_reader_bp


def create_app():
    """Initializes Flask app and registers Flask application blueprints."""
    app = Flask(__name__)

    app.register_blueprint(json_reader_bp, url_prefix="/json")

    return app
