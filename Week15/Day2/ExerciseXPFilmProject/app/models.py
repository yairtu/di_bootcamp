from app import db
from datetime import date

film_countries = db.Table('film_countries',
						  db.Column('country_id', db.Integer, db.ForeignKey('country.id')),
						  db.Column('film_id', db.Integer, db.ForeignKey('film.id'))
						  )

film_categories = db.Table('film_categories',
						   db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
						   db.Column('film_id', db.Integer, db.ForeignKey('film.id'))
						   )

film_directors = db.Table('film_directors',
						  db.Column('directors_id', db.Integer, db.ForeignKey('director.id')),
						  db.Column('film_id', db.Integer, db.ForeignKey('film.id'))
						  )


class Country(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	name = db.Column(db.String(30))


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	name = db.Column(db.String(20))


class Film(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	title = db.Column(db.String(20))
	date = db.Column(db.String(25), default=date.today().strftime('%b/%d/%Y'))
	# available_in_countries : Many to Many relationship with Country
	available_in_countries = db.relationship('Country', secondary=film_countries, backref='countries')
	# category: Many to Many relationship with Category
	category = db.relationship('Category', secondary=film_categories, backref='categories')
	# director : Many to Many relationship with Director
	director = db.relationship('Director', secondary=film_directors, backref='directors')


class Director(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
	first_name = db.Column(db.String(20))
	last_name = db.Column(db.String(20))
