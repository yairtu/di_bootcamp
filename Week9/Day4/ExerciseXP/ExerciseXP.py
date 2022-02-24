class Human:
	def __init__(self, name: str, age: int, living_place=None):
		self.name = name
		self.age = age
		self.living_place = living_place

	def move(self, building):
		self.living_place = building
		Building.inhabitants.append(self)


class Building:
	inhabitants = []

	def __init__(self, address: str):
		self.address = address


class City:
	buildings = []

	def __init__(self, name):
		self.name = name

	def construct(self, address):
		self.buildings.append(Building(address))

	def info(self, address):
		age = 0
		buildings = 0
		for building in self.buildings:
			if building.address == address:
				buildings += 1
				for inhabitants in address.inhabitants:
					age += inhabitants.age
				age = age / len(address.inhabitants)
				print(f"Average age: {age}\nBuldings: {buildings}")


per = Human("Per", 18)

tower1 = Building("1 random st, tel_aviv")
per.move(tower1)
tel_aviv = City("tel_aviv")
tel_aviv.construct(tower1)

print(tower1.inhabitants)
tel_aviv.info(tower1)
