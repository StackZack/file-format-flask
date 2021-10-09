"""Creates Parquet reader blueprint and adds URL rules from
Parquet MethodView implementation.
"""

from flask import Blueprint
from .views import ParquetReaderAPI

parquet_reader_bp = Blueprint("parquet_reader_bp", __name__)

reader_view = ParquetReaderAPI.as_view("parquet_reader_api")

parquet_reader_bp.add_url_rule(
    "/read",
    view_func=reader_view,
    methods=[
        "GET",
    ],
)
