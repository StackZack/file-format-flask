"""Creates Avro reader blueprint and adds URL rules from
Avro MethodView implementation.
"""

from flask import Blueprint
from .views import AvroReaderAPI

avro_reader_bp = Blueprint("avro_reader_bp", __name__)

reader_view = AvroReaderAPI.as_view("avro_reader_api")

avro_reader_bp.add_url_rule(
    "/read",
    view_func=reader_view,
    methods=[
        "GET",
    ],
)
