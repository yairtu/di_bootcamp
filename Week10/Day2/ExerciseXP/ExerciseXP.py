from func import make_great as m
# How do I import a file from a different directory?
import random
import string


#
# magicians = ["Merlin", "Harry Potter", "Houdini"]
# m(magicians)
# print(magicians)


def roll(x: int):
	random_num = random.randint(1, 100)
	if x == random_num:
		print("Success!")


roll(1)


def random_string(length: int):
	letters = string.ascii_letters
	result = ''.join(random.choice(letters) for i in range(length))
	print(result)


random_string(5)
