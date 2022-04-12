from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import InputRequired, Length
from app.models import Film

from app import db

categories = [
	'', 'Action and Adventure', 'Animation', 'Comedy', 'Drama', 'Fantasy', 'Historical', 'Historical Fiction',
	'Horror', 'Romance', 'Science Fiction', 'Western'
]


class AddFilmForm(FlaskForm):
	title = StringField('Title', validators=[InputRequired()])
	release_date = DateField('Release date', validators=[InputRequired()])
	category = SelectField('Category', choices=categories)
	submit = SubmitField('Submit')


def choice_query():
	return Film.query


class AddDirectorForm(FlaskForm):
	first_name = StringField('First name', validators=[InputRequired()])
	last_name = StringField('Last name', validators=[InputRequired()])
	film = QuerySelectField('Film', query_factory=choice_query, get_label='title', allow_blank=True)
	submit = SubmitField('Submit')
