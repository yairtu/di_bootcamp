from datetime import datetime

from app import db, flask_app


class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(20))
	email = db.Column(db.String(30), unique=True)
	address = db.Column(db.String(100))
	phonenumbers = db.relationship('PhoneNumber', backref='person', lazy='dynamic')


class PhoneNumber(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	number = db.Column(db.String(20))
	person_id = db.Column(db.Integer, db.ForeignKey('person.id'))


def get_persons():
	people = Person.query.all()
	return people
