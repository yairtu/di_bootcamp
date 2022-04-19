import json

from flask import Blueprint, render_template
from flask_login import current_user
from sqlalchemy import asc, desc

from app import db
from app.api import get_card_rarity
from app.models import Card, User

main = Blueprint('main', __name__)


@main.route('/')
def home():
	return render_template('main/index.html')


@main.route('/leaderboard')
def leaderboard():
	users = User.query.order_by(desc(User.points)).all()
	return render_template('main/leaderboard.html', users=users)
