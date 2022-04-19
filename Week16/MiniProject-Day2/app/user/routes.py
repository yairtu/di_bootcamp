import json

import requests
from random import randint
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.sql.expression import func, select
from app import db, bcrypt
from app.api import get_img_url
from app.models import Card, User, add_cards_db, get_random_card
from app.user.forms import Register, Login

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
	# all_cards = Card.query.all()
	# for card in all_cards:
	# 	card.image_url = f'https://storage.googleapis.com/ygoprodeck.com/pics/{card.card_id}.jpg'
	# 	db.session.commit()
	form = Register()
	if current_user.is_authenticated:
		return redirect(url_for('main.home'))
	if form.validate_on_submit():
		enc_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		new_user = User(username=form.username.data, email=form.email.data, password=enc_pw, type=form.profile.data)
		db.session.add(new_user)
		db.session.commit()
		print(new_user)
		for i in range(40):
			card = Card.query.filter_by(id=randint(1, 11282)).first()
			new_user.card.append(card)
			db.session.commit()
		flash('Your account has been created!', 'success')
		return redirect(url_for('user.login'))
	return render_template('user/register.html', form=form)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			flash('Login Successful', 'success')
			return redirect(url_for('user_bp.profile'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')
	if current_user.is_authenticated:
		return redirect(url_for('user_bp.profile'))
	return render_template('user/login.html', form=form)


@user_bp.route('/profile')
@login_required
def profile():
	cards = current_user.card
	if current_user.type == "Yugi":
		img = 'yugi.png'
	elif current_user.type == "Kaiba":
		img = 'kaiba.png'
	elif current_user.type == "Tea":
		img = 'tea.jpg'
	else:
		img = 'joey.jpg'
	return render_template('user/profile.html', cards=cards,img=img, user=current_user)


@user_bp.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('main.home'))
