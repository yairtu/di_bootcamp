import json


def load_data():
	with open('./products.json', 'r') as f:
		all_products = json.load(f)
	return all_products


def retrieve_requested_product(product_id):
	for item in load_data():
		if item["ProductId"] == product_id:
			return item
