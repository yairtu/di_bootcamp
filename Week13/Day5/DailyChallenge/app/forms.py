from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class PersonSearch(FlaskForm):
	name = StringField('Enter a name to search', validators=[InputRequired(), Length(min=2)])
	submit = SubmitField('Submit')


class PhoneSearch(FlaskForm):
	number = StringField('Enter a phone number to search', validators=[InputRequired(), Length(min=7)])
	submit = SubmitField('Submit')


class NationalitySearch(FlaskForm):
	nationality = StringField('Enter a nationality to search for', validators=[InputRequired(), Length(min=3)])
	submit = SubmitField('Submit')
