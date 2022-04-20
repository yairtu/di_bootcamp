import json
# from app import db, create_app
# from models import Card
import requests

# file = './static/all_cards.json'
# request = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php').json()
# with open(file, 'w+') as f:
# 	json.dump(request, f, indent=4)
#




# for item in request['data']:
# 	card = Card(card_id=item.get('id'))
# 	db.session.add(card)
# 	db.session.commit()


# print(requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php').json()['id'])


def get_img_url(card_id):
	return \
		requests.get(f'https://db.ygoprodeck.com/api/v7/cardinfo.php?id={card_id}').json()['data'][0]['card_images'][0][
			'image_url']


def get_card_rarity(card_id):
	return \
		requests.get(f'https://db.ygoprodeck.com/api/v7/cardinfo.php?id={card_id}').json()['data'][0]['card_sets'][0][
			'set_rarity']


# add all to db
# file = 'app/static/all_cards.json'
# 	with open(file, 'r') as f:
# 		data = json.load(f)
# 		for card in data['data']:
# 			try:
# 				new_card = Card(card_id=card['id'], name=card['name'], type=card['type'],
# 							rarity=card['card_sets'][0]['set_rarity'],
# 							image_url=card['card_images'][0]['image_url'],
# 							price=card['card_prices'][0]['amazon_price'])
# 				db.session.add(new_card)
# 				db.session.commit()
# 			except KeyError:
# 				print(card['id'])