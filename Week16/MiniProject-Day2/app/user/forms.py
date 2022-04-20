from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length, DataRequired, EqualTo, ValidationError
from app.models import User

profile_type = ['Yugi', 'Kaiba', 'Joey', 'Tea']


class Login(FlaskForm):
	username = StringField("Username",
						   validators=[InputRequired(message="Please enter your username"),
									   Length(min=3, max=12)])
	password = PasswordField("Password",
							 validators=[InputRequired(message="Please enter your password"),
										 Length(min=4, max=14)])
	remember = BooleanField("Remember me")
	login = SubmitField('Login')


class Register(FlaskForm):
	email = StringField('Email')
	username = StringField("Username",
						   validators=[InputRequired(message="Please choose a username"),
									   Length(min=3, max=12)])
	password = PasswordField("Password",
							 validators=[DataRequired(Length(min=4, max=14))])
	confirm_password = PasswordField("Password",
									 validators=[DataRequired(Length(min=4, max=14)), EqualTo('password')])
	profile = SelectField('Profile', choices=profile_type)
	register = SubmitField('Sign up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')
