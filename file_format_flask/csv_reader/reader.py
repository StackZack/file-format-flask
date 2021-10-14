"""Creates CSV reader blueprint and adds URL rules from
CSV MethodView implementation.
"""

from flask import Blueprint
from .views import CsvReaderAPI

csv_reader_bp = Blueprint("csv_reader_bp", __name__)

reader_view = CsvReaderAPI.as_view("csv_reader_api")

csv_reader_bp.add_url_rule(
    "/read",
    view_func=reader_view,
    methods=[
        "GET",
    ],
)
