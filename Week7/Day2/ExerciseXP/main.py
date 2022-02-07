# import random
#
#
# # Ex 1
# def display_message():
# 	print("I am learning python!")
#
#
# display_message()
#
#
# # Ex 2
# def favorite_book(title):
# 	print(f"One of my favorite books is {title}.")
#
#
# favorite_book("Alice in Wonderland")
#
#
# # Ex 3
# def describe_city(city, country="Iceland"):
# 	print(f"{city} is in {country}")
#
#
# describe_city("Reykjavik")
#
#
# # Ex 4
# def random_num():
# 	num1 = int(input("Enter a number between 1 and 100: "))
# 	if num1 < 1 or num1 > 100:
# 		print("Sorry number out of bounds")
# 	num2 = random.randint(1, 100)
# 	if num1 == num2:
# 		print("Success!")
# 	else:
# 		print(f"Fail\nNum1: {num1}\nNum2: {num2}")
#
#
# random_num()


# # Ex 5
# def make_shirt(size="L", text="I love python"):
# 	print(f"Shirt size is: {size}, the text that will be printed on the shirt: {text}")
#
#
# make_shirt("M", "We will rock you!")
# make_shirt("L")
# make_shirt("M")
# make_shirt("any", "Helloooooooooo")
# make_shirt(size="M", text="Keyword Arguments!!!")


# Ex 6
magicians = ["Merlin", "Harry Potter", "Houdini"]


def show_magicians(list_to_print):
	for e in list_to_print:
		print(e)


show_magicians(magicians)


def make_great(list_to_make_great):
	for e in list_to_make_great:
		index = list_to_make_great.index(e)
		magicians[index] = e + " the great"


make_great(magicians)


def show_magicians(list_to_print):
	print(list_to_print)


show_magicians(magicians)
