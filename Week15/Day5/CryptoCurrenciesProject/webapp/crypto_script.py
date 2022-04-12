# from requests import Request, Session
# from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
# import json
# import os
# # from models import Crypto
# from webapp import db
# from webapp.models import Crypto
#
#
# def get_coin_data_by_id(id):
# 	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
#
# 	parameters = {
# 		'id': f"{id}"
# 	}
# 	headers = {
# 		'Accepts': 'application/json',
# 		'X-CMC_PRO_API_KEY': '15daef1e-3fcc-46e5-8dcb-694f950ab633'
# 	}
#
# 	session = Session()
# 	session.headers.update(headers)
#
# 	try:
# 		response = session.get(url, params=parameters)
# 		data = json.loads(response.text)
# 		return data
# 	except (ConnectionError, Timeout, TooManyRedirects) as e:
# 		return e
#
#
# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
# parameters = {
# 	'start': '1',
# 	'limit': '20',
# }
# headers = {
# 	'Accepts': 'application/json',
# 	'X-CMC_PRO_API_KEY': os.environ['API_KEY'],
# }
#
# session = Session()
# session.headers.update(headers)
#
# # try:
# # 	response = session.get(url, params=parameters)
# # 	data = json.loads(response.text)
# # 	print(data)
# # except (ConnectionError, Timeout, TooManyRedirects) as e:
# # 	print(e)
#
#
import json

from webapp import db
from webapp.models import Crypto

file = 'static/map_data.json'

with open(file, 'r') as f:
	data = json.load(f)
	for item in data['data']:
		new_coin = Crypto(crypto_id=item.get("id"),
						  name=item.get('name'),
						  symbol=item.get('symbol'),
						  slug=item.get('slug'),
						  first_historical_data=item.get('first_historical_data'),
						  last_historical_data=item.get('last_historical_data'),
						  is_active=item.get('is_active'),
						  rank=item.get('rank')
						  )
		db.session.add(new_coin)
		db.session.commit()
