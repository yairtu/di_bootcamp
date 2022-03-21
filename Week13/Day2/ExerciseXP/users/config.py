import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = "45jh3kjhvbjf23456jkva009"
	SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'robots.db')}"
