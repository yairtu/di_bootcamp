import requests
from flask import Blueprint, render_template
from app import db
from app.models import Card

forum = Blueprint('forum', __name__)


@forum.route('/forum')
def forum_home():
	return render_template('forum.html')


@forum.route('/forum/post')
def post():
	return
