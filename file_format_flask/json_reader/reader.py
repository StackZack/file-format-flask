"""Creates JSON reader blueprint and adds URL rules from
JSON MethodView implementation.
"""

from flask import Blueprint
from .views import JsonReaderAPI

json_reader_bp = Blueprint("json_reader_bp", __name__)

reader_view = JsonReaderAPI.as_view("json_reader_api")

json_reader_bp.add_url_rule(
    "/read",
    view_func=reader_view,
    methods=[
        "GET",
    ],
)
