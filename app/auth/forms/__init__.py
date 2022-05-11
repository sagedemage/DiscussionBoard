""" Authentication Forms """
from flask_wtf import FlaskForm, csrf
from wtforms import StringField, PasswordField, SubmitField, validators


class RegisterForm(FlaskForm):
    """ Registration form """
    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.Length(min=6, max=40)
    ])
    password = PasswordField ('New Password', [
        validators.DataRequired(),
        validators.Length(min=6, max=40),
        validators.EqualTo('confirm', message='Password must match')
    ])
    confirm = PasswordField('Repeat Password', [
        validators.DataRequired()
    ])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField('Email Address', [
        validators.DataRequired()
    ])
    password = PasswordField('Password'), [
        validators.DataRequired()
    ]
