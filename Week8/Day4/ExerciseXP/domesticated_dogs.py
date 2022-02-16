from exercise_xp import Dog
import random


class PetDog(Dog):
	def __init__(self, name, age, weight, trained=False):
		super().__init__(name, age, weight)
		self.trained = trained

	def train(self):
		print(self.bark())
		self.trained = True

	def play(self, **args):
		dogs = ""
		if len(args) > 0:
			for arg in args:
				dogs += f" {arg}"
		print(f"{dogs} all play together")

	def do_a_trick(self):
		tricks = [f"{self.name} does a barrel roll", f"{self.name} stands on his back legs",
				  f"{self.name} shakes your hand", f"{self.name} plays dead"]
		if self.trained:
			print(tricks[random.randint(0, len(tricks) - 1)])


hallie = PetDog("Hallie", 1.5, 50)
izzie = PetDog("Isabella", 2, 95)
pops = PetDog("Pops", 3, 11)

hallie.train()
hallie.do_a_trick()