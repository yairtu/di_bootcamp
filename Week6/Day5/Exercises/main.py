sample_dict = {
	"name": "Kelly",
	"age": 25,
	"salary": 8000,
	"city": "New york"

}

keys_to_remove = ["name", "salary"]

for k in keys_to_remove:
	# sample_dict.pop(k, None)
	del sample_dict[k]

print(sample_dict)