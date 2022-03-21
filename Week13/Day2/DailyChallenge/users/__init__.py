from flask import Flask
import flask_migrate
import flask_sqlalchemy
from users.config import Config
import json

flask_app = Flask(__name__)

flask_app.config.from_object(Config)

db = flask_sqlalchemy.SQLAlchemy(flask_app)
migrate = flask_migrate.Migrate(flask_app, db)

from users import routes
from users.modules import User


def populate():
	with open('users/static/users.json', 'r') as f:
		data = json.load(f)
	for user in data:
		new_user = User(
			id=user['id'],
			name=user['name'],
			street=user['address']['street'],
			city=user['address']['city'],
			zipcode=user['address']['zipcode']
		)
		db.session.add(new_user)
	db.session.commit()
	return


# populate()
# db.create_all()

# db.drop_all()