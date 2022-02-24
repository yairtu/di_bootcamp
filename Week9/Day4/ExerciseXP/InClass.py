from typing import List


class Building:
	def __init__(self, address: str, inhabitants: List = []):
		self.address = address
		self.inhabitants = inhabitants

	def get_info(self):
		return f"Address: {self.address}"

	def get_inhabitants_mean_age(self):
		age_sum = 0
		for inhabitant in self.inhabitants:
			age_sum += inhabitant.age

		return age_sum / len(self.inhabitants)

	def __str__(self):
		return f"{'-' * 20} \nAddress: {self.address} \nInhabitants number: {len(self.inhabitants)} \n{'-' * 20}"


class Human:
	def __init__(self, name: str, age: int, living_place: Building = None):
		self.name = name
		self.age = age
		self.living_place = living_place
		self.__add_to_building_inhabitants()

	def move(self, building: Building):
		self.__remove_from_building_inhabitants()
		self.living_place = building
		self.__add_to_building_inhabitants()

	def __add_to_building_inhabitants(self):
		if self.living_place:
			print(f"adding the human {self.name} to the living place {self.living_place.address}")
			self.living_place.inhabitants.append(self)

	def __remove_from_building_inhabitants(self):
		if self.living_place:  # self.living_place != None
			print(f"removing the human {self.name} from the current living place {self.living_place.address}")
			self.living_place.inhabitants.remove(self)
		else:
			print(f"the human {self.name} has no living place")

	def get_info(self):
		return f"Name: {self.name} Age: {self.age} Living place: {self.living_place.get_info() if self.living_place else None}"

	def __str__(self):
		return self.get_info()


class City:
	def __init__(self, name: str, buildings: List[Building] = None):
		self.name = name
		self.buildings = buildings

	def construct(self, address):
		new_building = Building(address)
		self.buildings.append(new_building)

	def info(self, address):
		for building in self.buildings:
			if building.address == address:
				print(building.get_inhabitants_mean_age())
				return

		print(f"there is no building at the address {address}")


tlv_building = Building("TLV")
print(str(tlv_building))

bob = Human(name="Bob", age=10)
print(str(bob))

alice = Human(name="Alice", age=20)
print(str(bob))

bob.move(tlv_building)
alice.move(tlv_building)

print(str(tlv_building))

tlv = City("tkv", [tlv_building])
tlv.info("TLV")