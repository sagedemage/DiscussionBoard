""" Testing authentication pages """
import pytest


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_register_request(client):
    """ Test register page response """
    response = client.get("/register")
    assert response.status_code == 200


def test_login_request(client):
    """ Test login page response """
    response = client.get("/login")
    assert response.status_code == 200


def test_dashboard_request(client):
    """ Test dashboard page response """
    response = client.get("/dashboard")
    assert response.status_code == 302


def test_register_email_and_password_format(client):
    """ Ensure that the registration page has right the format
    for email, password, and confirm inputs """

    # Register
    response = client.get("/register")
    # check that input validates email requirement
    assert b"id=\"email\" name=\"email\" required type=\"email\"" in response.data
    # check that input validates password requirement,
    # and it has the right password constraints
    assert b"id=\"password\" maxlength=\"35\" minlength=\"6\" " \
           b"name=\"password\" required type=\"password\"" in response.data
    # check the input takes password confirmation
    assert b"id=\"confirm\" name=\"confirm\" type=\"password\"" in response.data


def test_login_email_and_password_format(client):
    """ Ensure that the login page has right the format
    for email and password inputs """

    # Login
    response = client.get("/login")
    # check that input validates email requirement
    assert b"id=\"email\" name=\"email\" required type=\"email\"" in response.data
    # check that input validates password requirement,
    # and it has the right password constraints
    assert b"id=\"password\" maxlength=\"35\" minlength=\"6\" " \
           b"name=\"password\" required type=\"password\"" in response.data


def test_register_redirection(client):
    """ Test registration redirects to the login page """
    response = client.post("/register", data={"email": "test1000@gmail.com",
                                              "password": "test1000", "confirm": "test1000"})
    assert response.headers["Location"] == "/login"


def test_login_redirection(client):
    """ Test login redirects to the dashboard """
    response = client.post("/login", data={"email": "test1000@gmail.com", "password": "test1000"})
    assert response.headers["Location"] == "/dashboard"


def test_registration_success(client):
    """ Test registration success """
    # Test successful registration
    response = client.post("/register", data={"email": "test2000@gmail.com", "password": "test2000",
                                              "confirm": "test2000"}, follow_redirects=True)
    assert b"Congratulations, you are a registered user!" in response.data


def test_registration_failure(client):
    """ Test registration failures """
    # Test registration fails if the passwords do not match
    response = client.post("/register", data={"email": "test2000@gmail.com", "password": "test2000",
                                              "confirm": "test2001"}, follow_redirects=True)
    assert b"Passwords must match" in response.data

    # Test registration fails if the account is already registered
    response = client.post("/register", data={"email": "test2000@gmail.com", "password": "test2000",
                                              "confirm": "test2000"}, follow_redirects=True)
    assert b"Already Registered" in response.data


def test_login_success(client):
    """ Test login success """
    # Successful login
    response = client.post("/login", data={"email": "test2000@gmail.com", "password": "test2000"},
                           follow_redirects=True)
    assert b"Welcome to the dashboard" in response.data


def test_login_failures(client):
    """ Test login failures """
    # Bad email
    response = client.post("/login", data={"email": "test9000@gmail.com", "password": "test1000"},
                           follow_redirects=True)
    assert b"Invalid email or password" in response.data

    # Bad password
    response = client.post("/login", data={"email": "test2000@gmail.com", "password": "test9000"},
                           follow_redirects=True)
    assert b"Invalid email or password" in response.data


def test_logout(client):
    """ Test logout response """
    response = client.get("/logout", follow_redirects=True)
    assert len(response.history) == 1
    assert response.request.path == "/login"


def test_deny_access_to_dashboard(client):
    """ Deny Access to the Dashboard """
    # denying access to the dashboard for users not logged
    response = client.get("/dashboard", follow_redirects=True)
    assert b"Please log in to access this page." in response.data


def test_allow_access_to_dashboard(client):
    # allowing access to the dashboard for logged in users (Test 10)
    response = client.post("/login", data={"email": "test1000@gmail.com",
                                              "password": "test1000", "confirm": "test1000"})
    assert response.headers["Location"] == "/dashboard"
