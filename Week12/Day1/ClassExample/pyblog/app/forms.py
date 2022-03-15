import flask_wtf
import wtforms


def validate_max_size(max_size):
	def my_length_check(form, field):
		if len(field.data) > max_size:
			raise wtforms.ValidationError(field.gettext("Field must be less than 50 characters"))

	return my_length_check


class Form(flask_wtf.FlaskForm):
	username = wtforms.StringField(label="Name", validators=[
		wtforms.validators.Length(min=4, max=25, message="invalid length it must be between 4 and 25")])
	password = wtforms.PasswordField(label="Password",
									 validators=[wtforms.validators.DataRequired(message="ops"), validate_max_size(10)])
	bio = wtforms.StringField(label="Bio")

	submit = wtforms.SubmitField(label="Submit")


class PersonForm(flask_wtf.FlaskForm):
	firstName = wtforms.StringField(label="First Name")
	lastName = wtforms.StringField(label="Last Name")
	age = wtforms.StringField(label="Age")

	submit = wtforms.SubmitField(label="Submit")
