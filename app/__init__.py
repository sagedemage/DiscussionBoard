"""A simple flask web app"""
import logging
import os
from logging.handlers import RotatingFileHandler

import flask_login
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
# from flask_mail import Mail

from app.db import db
from app.db.models import User
from app.cli import create_database, drop_database
from app.logging_config import log_con, LOGGING_CONFIG

from app.simple_pages import simple_pages
from app.auth import auth
from app.discussion import discussion
from app.db import database

from app.error_handlers import error_handlers
from app.context_processors import utility_text_processors

# mail = Mail()
login_manager = flask_login.LoginManager()


def create_app():
    """Create and configure an instance of the Flask application."""
    # Flask app
    app = Flask(__name__)

    # CSRF protection of form submissions
    csrf = CSRFProtect(app)

    app.config["ENV"] = "production"

    if app.config["ENV"] == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif app.config["ENV"] == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("app.config.TestingConfig")

    """
    if os.environ.get("FLASK_ENV") == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif os.environ.get("FLASK_ENV") == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif os.environ.get("FLASK_ENV") == "testing":
        app.config.from_object("app.config.TestingConfig")
    """

    # Flask Mail
    # app.mail = Mail(app)

    # login manager
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Flask Bootstrap
    boootstrap = Bootstrap5(app)

    # load functions with web interfaces
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)
    app.register_blueprint(discussion)
    app.register_blueprint(database)

    # load functionality without a web interfaces
    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)
    app.context_processor(utility_text_processors)
    
    # add command function to cli commands
    app.cli.add_command(create_database)
    app.cli.add_command(drop_database)

    db.init_app(app)

    api_v1_cors_config = {
        "methods": ["OPTIONS", "GET", "POST"],
    }
    CORS(app, resources={"/api/*": api_v1_cors_config})

    # start app once at startup
    return app


@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None
