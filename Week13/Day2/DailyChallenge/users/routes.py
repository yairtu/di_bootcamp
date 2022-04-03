import json

from flask import flash, render_template, redirect, url_for, request
from users import flask_app
from users.modules import User

from users.forms import LoginForm


def get_all_users_db():
	return User.query.all()


@flask_app.route('/', methods=['GET', 'POST'])
def index():
	all_users = get_all_users_db()
	print(all_users[1])
	return render_template('index.html', all_users=all_users)


@flask_app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		I am getting FileNotFoundError with the below commented, cannot figure out why
		file = "./static/form_data.json"
		with open(file, 'w') as f:
			json.dump(form.data, f, indent=4)
		result = request.form.to_dict(flat=False)
		print(result)
		for user in get_all_users_db():
			if result['name'][0] == user.name and result['city'][0] == user.city:
				flash(f"You have successfully logged in {user.name}", "success")
				return redirect(url_for('logged_in'))
	return render_template('login.html', form=form)


@flask_app.route('/logged_in')
def logged_in():
	return render_template('logged_in.html')