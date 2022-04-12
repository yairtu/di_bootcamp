from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()


def create_app():
	flask_app = Flask(__name__)

	flask_app.config.from_object(Config)
	migrate = Migrate(flask_app, db)
	db.init_app(flask_app)

	from app import models
	from app.films.routes import films

	flask_app.register_blueprint(films)

	return flask_app
