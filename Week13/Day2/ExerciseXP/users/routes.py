from flask import flash, render_template
from users import flask_app
from users.modules import User
from users import db


@flask_app.route('/', methods=['GET', 'POST'])
def index():
	all_users = User.query.all()
	print(all_users[1])
	return render_template('index.html', all_users=all_users)
