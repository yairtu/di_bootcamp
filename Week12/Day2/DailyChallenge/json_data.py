import json


def load_data():
	with open('./static/form_data.json', 'r') as f:
		form_info = json.load(f)
	return form_info
