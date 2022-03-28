import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = "lkj4HFKJHbfb43kjkjh684631F"
	SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'schedule.db')}"
	SQLALCHEMY_TRACK_MODIFICATION = False
