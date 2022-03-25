import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = "3ibjnf3ih5bbf36808f"
	SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'phone_lookup.db')}"
	SQLALCHEMY_TRACK_MODIFICATIONS = False