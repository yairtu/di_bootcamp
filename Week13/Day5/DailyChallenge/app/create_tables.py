from random import choices, choice

from faker import Faker

from app import db
from app.models import PhoneNumber, Person, Nationality

fake = Faker()

# Only run once to create a database of people and numbers

# def create_fake_data():
# 	new_person = Person(name=fake.name(), email=fake.email(), address=fake.address())
# 	new_person_number = PhoneNumber(number=fake.phone_number(), person=new_person)
# 	db.session.add(new_person)
# 	db.session.add(new_person_number)
# 	db.session.commit()
# 	return 'Made 100 users and numbers'
#
#
# for _ in range(100):
# 	create_fake_data()

# japanese = Nationality(name='Japanese')
# moroccan = Nationality(name='Moroccan')
#
# db.session.add_all([japanese, moroccan])
# db.session.commit()
#
# db.create_all()

# people = Person.query.all()
# print(people)
# print(people[0].nationalities)
# nationalities = Nationality.query.all()
# print(nationalities)
# print(nationalities[0].name)
#
# for person in people:
# 	for nationality in choices(nationalities):
# 		person.nationalities.append(nationality)
# 		db.session.commit()

# info = Person.query.filter_by(name='Donna').first()
#
# nationality = info.nationality.first().nationatlity
# print(nationality)
