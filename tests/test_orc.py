"""Tests ORC reader blueprint endpoints.
"""


def test_orc(client):
    """Tests output of reading ORC sample file.
    Expects 200 status code and list has length 100.

    :param client: Flask test client fixture
    :type client: Flask client
    """
    res = client.get('/orc/read')
    assert res.status_code == 200
    assert len(res.json['data']) == 100
