from faker import Faker

from app import db
from app.models import PhoneNumber, Person

fake = Faker()


# Only run once to create a database of people and numbers

def create_fake_data():
	new_person = Person(name=fake.name(), email=fake.email(), address=fake.address())
	new_person_number = PhoneNumber(number=fake.phone_number(), person=new_person)
	db.session.add(new_person)
	db.session.add(new_person_number)
	db.session.commit()
	return 'Made 100 users and numbers'


for _ in range(100):
	create_fake_data()

db.create_all()
