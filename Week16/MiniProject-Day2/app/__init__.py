from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'


def create_app():
	flask_app = Flask(__name__)
	flask_app.config.from_object(Config)

	from app.user.routes import user
	from app.forum.routes import forum
	from app.main.routes import main
	db.init_app(flask_app)
	migrate.init_app(flask_app, db)

	login_manager.init_app(flask_app)
	
	flask_app.register_blueprint(main)
	flask_app.register_blueprint(user)
	flask_app.register_blueprint(forum)

	return flask_app
