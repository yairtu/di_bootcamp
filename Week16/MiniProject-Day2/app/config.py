import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = 'secret-key-goes-here'
	SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'cards.db') }"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	# SECURITY_PASSWORD_SALT = "123f5sd4af632asdf"
	# SECURITY_PASSWORD_HASH = "sha512_crypt"