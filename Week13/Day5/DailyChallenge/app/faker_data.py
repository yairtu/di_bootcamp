from faker import Faker
from app.models import Person, PhoneNumber
from app import db



fake = Faker()

# for i in range(100):
# new_person = Person(name="Bob Alice", email="bob@alice.com", number=fake.phone_number())
#
#
# db.session.add(new_person)
#
# db.session.commit()
#
# print(fake.name())
# print(fake.email())
# print(fake.phone_number())
