from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Length, InputRequired, Email


class LoginForm(FlaskForm):
	name = StringField('Name', validators=[InputRequired(), Length(min=2, max=15)])
	city = StringField('City', validators=[InputRequired(), Length(min=2, max=25)])
	submit = SubmitField('Submit')
