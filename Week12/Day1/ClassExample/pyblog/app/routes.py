import flask

from __init__ import flask_app
from app.forms import Form, PersonForm


@flask_app.route('/')
def index():
	return flask.render_template("index.html"), 200

@flask_app.route('/create_user')
def create_user():
	# create user at the database, 500
	return flask.render_template("index.html"), 201

@flask_app.route('/myform', methods=("GET", "POST"))
def myform():
	form = Form()
	if form.validate_on_submit():
		username = form.username.data
		password = form.password.data
		bio = form.bio.data

		# do something with this values
		print("username:", username)
		print("password:", password)
		print("bio:", bio)

		return flask.redirect('/')

	return flask.render_template("my_from.html", form=form)


@flask_app.route('/person', methods=("GET", "POST"))
def peron_form():
	person_form = PersonForm()
	if person_form.validate_on_submit():
		first_name = person_form.firstName.data
		last_name = person_form.lastName.data
		age = person_form.age.data

		print("first_name: ", first_name)
		print("last_name: ", last_name)
		print("age: ", age)

		return flask.redirect('/')
	return flask.render_template("person.html", form=person_form)
