import json

# # Ex 1 Random sentence generator
# import random
#
#
# def main():
# 	print("This program will create a randomly generated sentence, according to how many words you want the"
# 		  " sentence to be.\n")
#
#
# def get_words_from_file(file):
# 	try:
# 		with open(file) as f:
# 			return f.read().split('\n')
# 	except FileNotFoundError as e:
# 		print("Invalid file")
#
#
# def get_random_sentence(how_many_words: int):
# 	try:
# 		word_collection = get_words_from_file("words.txt")
# 		sentence = ""
# 		for i in range(how_many_words):
# 			sentence += f"{random.choice(word_collection)} "
# 		return sentence.lower().strip()
# 	except TypeError:
# 		return ""
#
#
# main()
#
# while True:
# 	sentence_length = int(input("How long do you want your sentence to be (between 2 and 20 words long)? "))
# 	try:
# 		if 1 < sentence_length < 21:
# 			print(get_random_sentence(sentence_length))
# 			break
# 		else:
# 			raise ValueError
# 	except ValueError:
# 		print("Please choose a valid length\n")

# Exercise 2

sampleJson = {
	"company": {
		"employee": {
			"name": "emma",
			"payable": {
				"salary": 7000,
				"bonus": 800
			}
		}
	}
}

print(sampleJson["company"]["employee"]["payable"]["salary"])
sampleJson["company"]["employee"]["birth_date"] = "1/1/2000"
print(sampleJson)

with open("sampleJson.json", "w") as f:
	json.dump(sampleJson, f, indent=4, sort_keys=True)
