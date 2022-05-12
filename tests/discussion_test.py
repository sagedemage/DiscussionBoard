""" Testing discussion pages """


def test_discussion_request(client):
    """ Test discussion page response """
    response = client.get("/discussions")
    assert response.status_code == 302


def test_deny_access_to_discussion(client):
    """ Deny Access to the Discussion board """
    # test denying access to the dashboard for users not logged
    response = client.get("/discussions", follow_redirects=True)
    assert b"Please log in to access this page." in response.data


def test_allow_access_to_discussion(client):
    # test allowing access to the dashboard for users logged in
    client.post("/login", data={"email": "test1000@gmail.com", "password": "test1000"})
    response = client.get("/discussions")
    assert response.status_code == 200

