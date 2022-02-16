# # Ex 1
# class Pets:
# 	def __init__(self, animals):
# 		self.animals = animals
#
# 	def walk(self):
# 		for animal in self.animals:
# 			print(animal.walk())
#
#
# class Cat:
# 	is_lazy = True
#
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def walk(self):
# 		return f'{self.name} is just walking around'
#
#
# class Bengal(Cat):
# 	def sing(self, sounds):
# 		return f'{sounds}'
#
#
# class Chartreux(Cat):
# 	def sing(self, sounds):
# 		return f'{sounds}'
#
#
# class Leopard(Cat):
# 	def sing(self, sounds):
# 		return f"{sounds}"
#
#
# jungle_leo = Leopard("Leopard", 5)
# chart = Chartreux("Chart", 3)
# benji = Bengal("benji", 1)
#
# my_cats = [jungle_leo, chart, benji]
#
# my_pets = Pets(my_cats)
#
# my_pets.walk()

# Ex 2
class Dog:
	def __init__(self, name, age, weight):
		self.name = name
		self.age = age
		self.weight = weight

	def bark(self):
		return f"{self.name} is barking"

	def run_speed(self):
		return f"{self.name}'s running speed is {self.weight * self.age / 10}"

	def fight(self, other_dog):
		if (self.weight * 2 * self.age / 10) > (other_dog.weight * 2 * other_dog.age / 10):
			return f"{self.name} won the fight"
		else:
			return f"{other_dog.name} won the fight"


hallie = Dog("Hallie", 1.5, 50)
izzie = Dog("Isabella", 2, 95)
pops = Dog("Pops", 3, 110)

print(hallie.bark())
print(izzie.fight(pops))