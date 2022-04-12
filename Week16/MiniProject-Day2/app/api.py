import json

from app import db, create_app
from models import Card
import requests

# with open(file, 'w+') as f:
# 	json.dump(request, f, indent=4)


file = './static/all_cards.json'
request = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php?id=37478723').json()

# for item in request['data']:
# 	card = Card(card_id=item.get('id'))
# 	db.session.add(card)
# 	db.session.commit()


print(requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php').json()['id'])