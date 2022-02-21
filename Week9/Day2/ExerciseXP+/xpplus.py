# Ex 1

class Family:
	members = [
		{'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
		{'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
	]
	last_name = str

	def __int__(self, name, age, gender, is_child):
		self.name = name
		self.age = age
		self.gender = gender
		self.is_child = is_child
		Family.members.append({"name": self.name, "age": self.age, "gender": self.gender, is_child: self.is_child})

	@classmethod
	def born(cls, **kwargs):
		kwargs.setdefault("age", 0)
		kwargs.setdefault("is_child", True)
		cls.members.append(kwargs)

	@classmethod
	def is_18(cls, name):
		for person in cls.members:
			if person["name"].lower() == name.lower():
				return person["is_child"]


class TheIncredibles(Family):
	members = []
	last_name = "Parr"

	def __init__(self, name, age, gender, is_child, incredible_name, power):
		super().__int__(name, age, gender, is_child)
		self.incredible_name = incredible_name
		self.power = power
		TheIncredibles.members.append(({"name": self.name,
										"age": self.age,
										"gender": self.gender,
										is_child: self.is_child,
										"incredible_name": self.incredible_name,
										"power": self.power}))

	@classmethod
	def use_power(cls, name):
		for person in cls.members:
			if person["name"].lower() == name.lower():
				if person["is_child"]:
					print("Learn to harness your power first")
				else:
					print(f"{person['power']}")

	@classmethod
	def incredible_presentation(cls):
		for incredible in cls.members:
			print(f"{incredible['incredible_name']}: {incredible['power']}")


bob = TheIncredibles("Bob", 35, "Male", False, "Mr. Incredible", "superhuman strength")
helen = TheIncredibles("Helen", 32, "Female", False, "Elastigirl", "super strechy body")
violet = TheIncredibles("violet", 14, "Female", True, "Invisigirl", "force fields")
dash = TheIncredibles("Dashiell", 12, "Male", True, "Dash", "super speed")
john = TheIncredibles("John Jackson", 2, "Male", True, "Jack Jack", "undisclosed")

TheIncredibles.born(name="Baby Jack", gender="Male",incredible_name="JackJack", power="Unknown power")

TheIncredibles.incredible_presentation()
