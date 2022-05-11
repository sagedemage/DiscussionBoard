import click
from flask.cli import with_appcontext
from app.db import db


@click.command(name='create-db')
@with_appcontext
def create_database():
    db.create_all()


@click.command(name='drop-db')
@with_appcontext
def drop_database():
    db.drop_all()

