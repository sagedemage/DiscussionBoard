""" Testing discussion pages """


def test_discussion_request(client):
    """ Test discussion page response """
    response = client.get("/discussions")
    assert response.status_code == 302


def test_deny_access_to_discussion(client):
    """ Deny Access to the Discussion board """
    # denying access to the dashboard for users not logged
    response = client.get("/discussions", follow_redirects=True)
    assert b"Please log in to access this page." in response.data

