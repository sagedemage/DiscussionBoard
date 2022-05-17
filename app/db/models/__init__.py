from datetime import datetime

from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import db
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False, unique=True)
    about = db.Column(db.String(300), nullable=True, unique=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column('registered_on', db.DateTime)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    is_admin = db.Column('is_admin', db.Boolean(), nullable=False, server_default='0')
    posts = relationship('Posts', backref='users', lazy=True)

    # `roles` and `groups` are reserved words that *must* be defined
    # on the `User` model to use group- or role-based authorization.

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        self.registered_on = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.email


class Posts(db.Model, SerializerMixin):
    __tablename__ = 'discussions'
    serialize_only = ('title', 'post')
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    username = db.Column(db.Integer, db.ForeignKey('users.username'))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def serialize(self):
        return {
            'title': self.title,
            'post': self.post
        }

    def __repr__(self):
        return '<Title %r>' % self.title
