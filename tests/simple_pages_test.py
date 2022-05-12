""" Testing simple pages """


def test_index_request(client):
    """ Test index page response """
    response = client.get("/")
    assert response.status_code == 200


def test_about_request(client):
    """ Test about page response """
    response = client.get("/about")
    assert response.status_code == 200


def test_welcome_request(client):
    """ Test welcome page response """
    response = client.get("/welcome")
    assert response.status_code == 200


def test_page_not_found_request(client):
    response = client.get("/webpage")
    assert response.status_code == 404
