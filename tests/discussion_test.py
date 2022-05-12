""" Testing discussion pages """


def test_discussion_request(client):
    """ Test discussion page response """
    response = client.get("/discussion")
    assert response.status_code == 404