from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class add_post_form(FlaskForm):
    title = StringField('Title', [
        validators.DataRequired(),
    ], description="Add title for the post")

    description = TextAreaField('Post', [
        validators.DataRequired(),
    ], description="Add the description of the post")
    submit = SubmitField()


class edit_post_form(FlaskForm):
    title = StringField('Title', [
        validators.DataRequired(),
        validators.length(min=6, max=35)
    ], description="Add title for the post")
    description = TextAreaField('Post', [
        validators.DataRequired(),
    ], description="Add the description of the post")
    submit = SubmitField()
