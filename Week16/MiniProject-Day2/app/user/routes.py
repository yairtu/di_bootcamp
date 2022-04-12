import requests
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.sql.expression import func, select
from app import db, bcrypt
from app.models import Card, User, add_cards_db, get_random_card
from app.user.forms import Register, Login

user = Blueprint('user', __name__)


@user.route('/register', methods=['GET', 'POST'])
def register():
	User.query.filter(User.id == 1).delete()
	db.session.commit()
	form = Register()
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	if form.validate_on_submit():
		enc_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		new_user = User(username=form.username.data, email=form.email.data, password=enc_pw, type=form.profile.data)
		db.session.add(new_user)
		db.session.commit()
		print(new_user)
		for i in range(41):
			card = Card.query.filter_by(card_id=get_random_card()).first()
			new_user.card.append(card)
			db.session.commit()
		flash('Your account has been created!', 'success')
		return redirect(url_for('user.login'))
	return render_template('user/register.html', form=form)


@user.route('/login', methods=['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
			return redirect(url_for('main.home'))
	return render_template('user/login.html', form=form)


@user.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.home'))
