from datetime import datetime

from app import db, flask_app

nationality_table = db.Table('nationalities_person',
							 db.Column('person_id', db.Integer, db.ForeignKey('person.id')),
							 db.Column('nationality_id', db.Integer, db.ForeignKey('nationality.id'))
							 )


class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(20))
	email = db.Column(db.String(30), unique=True)
	address = db.Column(db.String(100))
	phonenumbers = db.relationship('PhoneNumber', backref='person', lazy='dynamic')
	nationalities = db.relationship("Nationality", secondary=nationality_table, back_populates="people")


class PhoneNumber(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	number = db.Column(db.String(20))
	person_id = db.Column(db.Integer, db.ForeignKey('person.id'))


class Nationality(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(16), index=True, unique=True)
	people = db.relationship("Person", secondary=nationality_table, back_populates="nationalities")


def get_persons():
	people = Person.query.all()
	return people
