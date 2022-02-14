class Farm:

	def __init__(self, farmer):
		self.farmer = farmer
		self.animals = {}

	def add_animal(self, animal, count=1):
		if animal in self.animals.keys():
			self.animals[animal] = count + self.animals.get(animal)
		else:
			self.animals[animal] = count

	def get_info(self):
		print(f"{self.farmer}'s farm")
		print("")
		for animal in self.animals:
			print(f"{animal} : {self.animals.get(animal)}")
		print("")
		return "\tE-I-E-I-O"

	def get_short_info(self):
		sent = f"{self.farmer}'s farm has"
		if len(self.animals) == 1:
			return f"{self.farmer}'s farm has no animals"
		else:
			count = 1
			for key in self.animals.keys():
				sent += f"{' and ' if count == len(self.animals) else ' '}{key if key == 'sheep' else f'{key}s'}" \
						f"{'' if count == len(self.animals) else ','}"
				count += 1
		return sent


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print()
print(macdonald.get_short_info())
