from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, InputRequired, Email


class CvDetails(FlaskForm):
	first_name = StringField('First name', validators=[InputRequired(), Length(min=2, max=15)])
	last_name = StringField('Last name', validators=[InputRequired(), Length(min=2, max=20)])
	age = IntegerField('Age', validators=[InputRequired()])
	experience = StringField('Experience (Years)', validators=[InputRequired(), Length(min=1, max=1000)])
	phone_number = StringField('Phone number', validators=[InputRequired()])
	about_me = StringField('About me', validators=[InputRequired()])
	profession = StringField('Profession', validators=[InputRequired()])
	email = StringField('Email', validators=[InputRequired(), Email()])
	personal_experience1 = StringField('Personal Experience 1', validators=[InputRequired()])
	personal_experience2 = StringField('Personal Experience 2 (If you have)')
	personal_experience3 = StringField('Personal Experience 3 (If you have)')
	personal_experience4 = StringField('Personal Experience 4 (If you have)')
	location = StringField('Address', validators=[InputRequired()])
	submit = SubmitField('Submit')
