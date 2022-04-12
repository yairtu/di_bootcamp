from webapp import db
# from webapp.crypto_script import get_coin_data_by_id


user_crypto = db.Table('user_crypto',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('crypto_id', db.Integer, db.ForeignKey('crypto.id'))
)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	username = db.Column(db.String(25), unique=True, nullable=False)
	email = db.Column(db.String(40), unique=True, nullable=False)
	password = db.Column(db.String(100))
	cryptos = db.relationship('Crypto', secondary=user_crypto, backref='coins')


class Crypto(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	crypto_id = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(30))
	symbol = db.Column(db.String(10))
	slug = db.Column(db.String(20))
	first_historical_data = db.Column(db.String(50))
	last_historical_data = db.Column(db.String(50))
	rank = db.Column(db.Integer)
	is_active = db.Column(db.Integer)


# def get_info(crypto_id):
# 	return get_coin_data_by_id(crypto_id)