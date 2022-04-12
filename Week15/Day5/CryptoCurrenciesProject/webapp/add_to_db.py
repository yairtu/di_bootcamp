# import json
#
# from flask import app
#
# from webapp import db
# from webapp.models import Crypto
#
# file = 'static/map_data.json'
#
# with open(file, 'r') as f:
# 	data = json.load(f)
# 	for item in data['data']:
# 		new_coin = Crypto(id=item.get("id"),
# 						  name=item.get('name'),
# 						  symbol=item.get('symbol'),
# 						  slug=item.get('slug'),
# 						  first_historical_data=item.get('first_historical_data'),
# 						  last_historical_data=item.get('last_historical_data'),
# 						  is_active=item.get('is_active')
# 						  )
# 		db.session.add(new_coin)
# 		db.session.commit()
