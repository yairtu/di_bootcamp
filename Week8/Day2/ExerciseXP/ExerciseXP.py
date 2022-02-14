# # Ex 1
#
# class Cat:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
#
# gertrude = Cat("Gertude", 1)
# relle = Cat("Relle", 2)
# belle = Cat("Belle", 3)
#
# catList = [gertrude, relle, belle]
#
#
# def find_oldest_cat():
# 	age = 0
# 	oldest_cat = ""
# 	for cat in catList:
# 		if cat.age > age:
# 			oldest_cat = cat.name
# 			age = cat.age
# 	return f"The oldest cat is {oldest_cat}, and is {age} years old."
#
#
# print(find_oldest_cat())

# # Ex 2
#
# class Dog:
# 	def __init__(self, name, height):
# 		self.name = name
# 		self.height = height
#
# 	def bark(self):
# 		print(f"{self.name} goes woof!")
#
# 	def jump(self):
# 		print(f"{self.name} jumps {self.height * 2} cm high!")
#
#
# davids_dog = Dog("Rex", 50)
#
# print(davids_dog.name, davids_dog.height)
#
# davids_dog.bark()
# davids_dog.jump()
#
# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.name, sarahs_dog.height)
#
# sarahs_dog.bark()
# sarahs_dog.jump()
#
# if sarahs_dog.height > davids_dog.height:
# 	print(sarahs_dog.name)
# else:
# 	print(davids_dog.name)

# # Ex 3
# class Song:
# 	def __init__(self, lyrics):
# 		self.lyrics = lyrics
#
# 	def sing_me_a_song(self):
# 		for lyrics in self.lyrics:
# 			print(lyrics)
#
#
# stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
#
# stairway.sing_me_a_song()

# Ex 4

class Zoo:
	def __init__(self, zoo_name):
		self.name = zoo_name
		self.animals = []

	def add_animal(self, new_animal):
		if new_animal in self.animals:
			return
		self.animals.append(new_animal)

	def get_animals(self):
		for animal in self.animals:
			print(animal)

	def sell_animal(self, animal_sold):
		if animal_sold in self.animals:
			self.animals.remove(animal_sold)

	def sort_animals(self):
		self.animals.sort()
		animal_dict = {}
		for animal in self.animals:
			animal_dict.setdefault(ord(animal[0]) - 64, []).append(animal)
		return animal_dict

	def get_groups(self):
		self.animals.sort()
		animal_dict = {}
		for animal in self.animals:
			animal_dict.setdefault(ord(animal[0]) - 64, []).append(animal)
		for e in animal_dict:
			print(f"Group {e} animals: {animal_dict.get(e)}")


ramat_gan_safari = Zoo("Ramat Gan Safari")

ramat_gan_safari.add_animal(input("Which animal should we add to the zoo? "))
