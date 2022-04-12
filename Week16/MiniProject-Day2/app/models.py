import json
from datetime import datetime

import requests

from app import db, login_manager
from flask_login import UserMixin


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
	credits = db.Column(db.Integer, default=100)
	card = db.relationship('Card', secondary=user_cards, backref='cards')
	date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	card_id = db.Column(db.Integer, unique=True, nullable=False)
	name = db.Column(db.String(30))
	type = db.Column(db.String(20))
	rarity = db.Column(db.String(15))
	price = db.Column(db.String(15))


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


def add_cards_db():
	file = 'app/static/all_cards.json'
	with open(file, 'r') as f:
		all_cards = json.load(f)
		for card in all_cards['data']:
			card = Card(card_id=card['id'], name=card['name'], type=card['type'],
						price=card['card_prices'][0]['amazon_price'])
			db.session.add(card)
			db.session.commit()


def get_random_card():
	random_card = requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php').json()['id']
	return random_card