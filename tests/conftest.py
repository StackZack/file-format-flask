"""Sets up and configured pytest fixtures
"""
import pytest
from file_format_flask import create_app


@pytest.fixture
def client():
    """Creates test client for use in pytests.

    :yield: Flask test client
    :rtype: Flask client
    """
    app = create_app()
    with app.test_client() as client:
        yield client
