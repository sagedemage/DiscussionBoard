"""Test Configuration Setup"""
# pylint: disable=redefined-outer-name

import pytest
from app import create_app


@pytest.fixture()
def web_app():
    """This makes the app"""
    web_app = create_app()
    web_app.config.update({
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,
    })
    yield web_app


@pytest.fixture()
def client(web_app):
    """This makes the http client"""
    return web_app.test_client()


@pytest.fixture()
def runner(web_app):
    """This makes the task runner"""
    return web_app.test_cli_runner()
