"""Tests Avro reader blueprint endpoints.
"""


def test_avro(client):
    """Tests output of reading Avro sample file.
    Expects 200 status code and list has length 100.

    :param client: Flask test client fixture
    :type client: Flask client
    """
    res = client.get('/avro/read')
    assert res.status_code == 200
    assert len(res.json['data']) == 100
