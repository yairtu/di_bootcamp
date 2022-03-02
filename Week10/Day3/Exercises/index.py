import json


def print_child(child):
	print("name: ", child["firstName"])
	print("age: ", child["age"])


with open("file.json", "r+") as file:
	family = json.load(file)

	children = family["children"]
	for child in children:
		print_child(child)

	for i in range(len(children)):
		children[i]["favorite_color"] = "white"

	file.seek(0)
	json.dump(family, file, indent=2)