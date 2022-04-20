import json
from datetime import datetime

import requests
from flask import abort
from flask_admin.contrib.sqla import ModelView
from flask_security import RoleMixin

from app import db, login_manager
from flask_login import UserMixin, current_user


# @login_manager.user_loader
# def load_user(user_id):
# 	return User.query.get(int(user_id))
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


user_cards = db.Table('user_cards',
					  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
					  db.Column('card_id', db.Integer, db.ForeignKey('card.id'))
					  )


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	username = db.Column(db.String(25), unique=True, nullable=False)
	email = db.Column(db.String(40), unique=True, nullable=False)
	password = db.Column(db.String(100))
	type = db.Column(db.String(25), nullable=False)
	image_url = db.Column(db.String(100))
	credits = db.Column(db.Float, default=100.0)
	points = db.Column(db.Integer, default=0)
	card = db.relationship('Card', secondary=user_cards, backref='cards')
	posts = db.relationship('Post', backref='user')
	comments = db.relationship('Comment', backref='user')
	admin = db.Column(db.Boolean, default=False)
	date_created = db.Column(db.Date, nullable=False, default=datetime.utcnow)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	card = db.Column(db.String(100))
	price = db.Column(db.Integer)
	sold = db.Column(db.Boolean, default=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	comments = db.relationship('Comment', backref='post')

	def delete_post(self):
		db.session.delete(self)
		db.session.commit()


class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	content = db.Column(db.String(500), nullable=False)
	date_posted = db.Column(db.DateTime, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

	def delete_comment(self):
		db.session.delete(self)
		db.session.commit()


class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	card_id = db.Column(db.Integer, unique=True, nullable=False)
	name = db.Column(db.String(30))
	type = db.Column(db.String(20))
	rarity = db.Column(db.String(15))
	image_url = db.Column(db.String(50))
	price = db.Column(db.String(15))


def add_cards_db():
	file = 'app/static/all_cards.json'
	with open(file, 'r') as f:
		all_cards = json.load(f)
		for card in all_cards['data']:
			card = Card(card_id=card['id'], name=card['name'], type=card['type'],
						price=card['card_prices'][0]['amazon_price'])
			db.session.add(card)
			db.session.commit()


class SecureModelView(ModelView):
	def is_accessible(self):
		try:
			if current_user.admin:
				return True
		except AttributeError:
			return abort(403)


def get_random_card():
	random_card = requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php').json()['id']
	return random_card
