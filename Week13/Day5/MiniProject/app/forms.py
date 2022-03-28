from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length


class AddTodo(FlaskForm):
	todo = StringField(label='Enter a task for your to-do list', validators=[InputRequired()])
	submit = SubmitField(label='Submit')


class MarkCompleted(FlaskForm):
	mark_c = SubmitField(label='Mark completed')
	mark_u = SubmitField(label="Mark uncompleted")
