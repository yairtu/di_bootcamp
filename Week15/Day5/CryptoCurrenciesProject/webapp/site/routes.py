import json

from flask import Blueprint, render_template
from sqlalchemy import desc, asc
from webapp import db
from webapp.models import Crypto

site = Blueprint('site', __name__)


@site.route('/')
def home():
	all_crypto = Crypto.query.order_by(asc(Crypto.rank))
	return render_template('index.html', cryptos=all_crypto)




	# file = 'webapp/static/map_data.json'
	#
	# with open(file, 'r') as f:
	# 	data = json.load(f)
	# 	for item in data['data']:
	# 		new_coin = Crypto(crypto_id=item.get("id"),
	# 						  name=item.get('name'),
	# 						  symbol=item.get('symbol'),
	# 						  slug=item.get('slug'),
	# 						  first_historical_data=item.get('first_historical_data'),
	# 						  last_historical_data=item.get('last_historical_data'),
	# 						  is_active=item.get('is_active'),
	# 						  rank=item.get('rank')
	# 						  )
	# 		db.session.add(new_coin)
	# 		db.session.commit()