from flask import Blueprint

json_reader_bp = Blueprint("json_reader_bp", __name__, url_prefix="/read-json")


@json_reader_bp.get('/')
def read():
    test = {
        "test": "test message",
    }
    return test
