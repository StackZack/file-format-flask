"""Creates ORC reader blueprint and adds URL rules from
ORC MethodView implementation.
"""

from flask import Blueprint
from .views import OrcReaderAPI

orc_reader_bp = Blueprint("orc_reader_bp", __name__)

reader_view = OrcReaderAPI.as_view("orc_reader_api")

orc_reader_bp.add_url_rule(
    "/read",
    view_func=reader_view,
    methods=[
        "GET",
    ],
)
