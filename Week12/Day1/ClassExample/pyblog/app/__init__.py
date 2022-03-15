import flask


flask_app = flask.Flask(__name__)  # Remember: __name__ is the name of the file where the code is written


flask_app.config['SECRET_KEY'] = 'you-will-never-guess'


