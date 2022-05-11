""" Authentication Forms """
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class login_form(FlaskForm):
    """ Login form """
    email = EmailField('Email Address', [
        validators.DataRequired(),
    ])

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=6, max=35)
    ])

    submit = SubmitField()


class register_form(FlaskForm):
    """ Registration form """
    email = EmailField('Email Address', [
        validators.DataRequired(),

    ], description="Signup with an email")

    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.length(min=6, max=35),
        validators.EqualTo('confirm', message='Password must match'),

    ], description="Create a password ")

    confirm = PasswordField('Repeat Password', description="please retype your password")
    submit = SubmitField()
