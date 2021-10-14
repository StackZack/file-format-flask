"""Tests JSON reader blueprint endpoints.
"""


def test_json(client):
    """Tests output of reading JSON sample file.
    Expects 200 status code.

    :param client: Flask test client fixture
    :type client: Flask client
    """
    res = client.get('/json/read')
    assert res.status_code == 200
