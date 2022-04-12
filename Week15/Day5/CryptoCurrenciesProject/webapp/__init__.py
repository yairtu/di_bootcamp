from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
from webapp.config import Config

db = SQLAlchemy()


def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	with app.app_context():
		db.init_app(app)
		from webapp.models import User, Crypto
		from webapp import routes
	migrate = Migrate(app, db)
	# login_manager = LoginManager()
	# login_manager.login_view = 'auth.login'
	# login_manager.init_app(webapp)
	# from .models import User
	# @login_manager.user_loader
	# def load_user(user_id):
	# 	# since the user_id is just the primary key of our user table, use it in the query for the user
	# 	return User.query.get(int(user_id))

	# blueprint for auth routes in our webapp
	from webapp.site.routes import site
	app.register_blueprint(site)

	# blueprint for non-auth parts of webapp
	# from project.main.main import main as main_blueprint
	# webapp.register_blueprint(main_blueprint)

	return app
