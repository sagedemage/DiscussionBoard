from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class add_post_form(FlaskForm):
    title = StringField('Title', [
        validators.DataRequired(),
    ], description="Add title for the post")
    description = StringField('Post', [
        validators.DataRequired(),
    ], description="Add the description of the post")
    submit = SubmitField()


class edit_post_form(FlaskForm):
    title = StringField('Title', [
        validators.DataRequired(),
    ], description="Add title for the post")
    description = StringField('Post', [
        validators.DataRequired(),
    ], description="Add the description of the post")
    submit = SubmitField()