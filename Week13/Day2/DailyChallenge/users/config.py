import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = "45jh3kjhvbjf23456jkva009"
	SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'robots.db')}"
	PROJECT_ROOT = os.path.dirname(os.path.dirname(basedir))
	STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
