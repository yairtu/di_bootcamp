from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_login import LoginManager
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin


db = SQLAlchemy()

migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
admin = Admin()
login_manager.login_view = 'user_bp.login'
login_manager.login_message_category = 'info'
from app.models import User, Post, Comment, Card, SecureModelView


def create_app():
	flask_app = Flask(__name__)
	flask_app.config.from_object(Config)

	from app.user.routes import user_bp
	from app.forum.routes import forum
	from app.main.routes import main
	# from app.admin.routes import admin
	db.init_app(flask_app)

	migrate.init_app(flask_app, db, render_as_batch=True)

	login_manager.init_app(flask_app)
	admin.init_app(flask_app)

	admin.add_view(SecureModelView(Post, db.session))
	admin.add_view(SecureModelView(Comment, db.session))
	admin.add_view(SecureModelView(User, db.session))
	admin.add_view(SecureModelView(Card, db.session))

	flask_app.register_blueprint(main)
	flask_app.register_blueprint(user_bp)
	flask_app.register_blueprint(forum)
	# from app.api import get_img
	# flask_app.jinja_env.globals.update(get_img=get_img)

	return flask_app
