from flask import Flask, render_template, redirect, url_for, request
from flask import flash
from app.forms import PersonSearch, PhoneSearch
from app import flask_app, db
from app.models import Person, PhoneNumber


@flask_app.route('/')
def index():
	all_people = Person.query.paginate(page=1, per_page=14, error_out=False)

	return render_template('index.html', people=all_people)

@flask_app.route('/page/<int:page_number>')
def pagination(page_number):
	all_people = Person.query.paginate(page=page_number, per_page=14, error_out=False)

	return render_template('index.html', people=all_people)

@flask_app.route('/person', methods=['GET', 'POST'])
def person():
	form = PersonSearch()
	all_people = Person.query.all()
	if form.validate_on_submit():
		name = form.name.data
		for pers in all_people:
			if pers.name == name:
				return redirect(url_for('person_name', name=name))
		else:
			flash("This person is not in our records")
	return render_template('person.html', form=form)


@flask_app.route('/number', methods=['GET', 'POST'])
def number():
	form = PhoneSearch()
	all_numbers = PhoneNumber.query.all()
	if form.validate_on_submit():
		number = form.number.data
		for num in all_numbers:
			if num.number == number:
				return redirect(url_for('phone_number', phone_number=number))
		else:
			flash('This number is not in our records')
	return render_template('number.html', form=form)


@flask_app.route('/person/num-<phone_number>')
def phone_number(phone_number):
	number_info = PhoneNumber.query.filter_by(number=phone_number).first()
	person_id = number_info.person_id
	user = Person.query.filter_by(id=person_id).first()
	return render_template('searched_number.html', number=phone_number, user=user)


@flask_app.route('/person/name-<name>')
def person_name(name):
	info = Person.query.filter_by(name=name).first()
	number = info.phonenumbers.first().number
	return render_template('searched_person.html', info=info, name=name, number=number)
