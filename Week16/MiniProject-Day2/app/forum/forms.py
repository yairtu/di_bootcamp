from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired
from wtforms_sqlalchemy.fields import QuerySelectField


def choice_query():
    return current_user.card


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    card = QuerySelectField('Card to sell', query_factory=choice_query, get_label='name', allow_blank=True)
    submit = SubmitField('Submit Post')


class CommentForm(FlaskForm):
    content = StringField('Content', validators=[InputRequired()])
    submit = SubmitField('Submit Comment')
