import flask

app = flask.Flask(__name__)

app.secret_key = 'super secret key'

from app import routes

