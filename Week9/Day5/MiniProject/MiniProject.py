from typing import Set


class Human:
	def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str, family=Set):
		self.id_number = id_number
		self.name = name
		self.age = age
		self.priority = priority
		self.blood_type = blood_type
		self.family = set([])

	def add_family_member(self, person):
		self.family.add(person)
		person.family.add(self)

	def __str__(self):
		return f"{self.name}:{self.age}"


class Queue:
	def __init__(self, humans=[]):
		self.humans = humans

	def add_person(self, person):
		if person.age > 60 or person.priority:
			self.humans.insert(0, person)
		else:
			self.humans.append(person)

	def find_in_queue(self, person):
		index = self.humans.index(person)
		print(f"{person.name} is #{index} in line")
		return index

	def swap(self, person1, person2):
		print(f"Swapping places of {person1.name} and {person2.name}\n")
		index_person1 = self.humans.index(person1)
		index_person2 = self.humans.index(person2)
		self.humans[index_person1], self.humans[index_person2] = self.humans[index_person2], self.humans[index_person1]

	def get_next(self):
		if len(self.humans) == 0:
			return None
		next_human = self.humans[0]
		print(f"Next person in line is {self.humans[0].name}")
		self.humans.pop()
		return next_human

	def get_next_blood_type(self, blood_type):
		if len(self.humans) == 0:
			return None
		for human in self.humans:
			if human.blood_type == blood_type:
				print(f"first person with blood type {blood_type} at index: {self.humans.index(human)}")
				self.humans.remove(human)
				return human
		print("No one with that blood type in line")

	def sort_by_age(self):
		if len(self.humans) > 1:
			self.humans.sort(key=lambda human: human.age, reverse=True)

	def rearrange_queue(self):
		if len(self.humans) < 3:
			return
		for person in self.humans:
			if self.humans.index(person) == len(self.humans) - 1:
				return
			if person in self.humans[self.humans.index(person) + 1].family:
				self.humans.insert(len(self.humans) - 1, self.humans.pop(self.humans.index(person)))


bob = Human(id_number="1234", name="Bob", age=68, priority=True, blood_type="A")
alice = Human(id_number="1235", name="Alice", age=62, priority=True, blood_type="B")
tim = Human(id_number="1236", name="Tim", age=65, priority=True, blood_type="AB")

q = Queue([bob, alice, tim])

print()
for human in q.humans:
	print(human)

print()
q.sort_by_age()
for human in q.humans:
	print(human)

print(q.humans.index(bob))
print()

tim.add_family_member(alice)

print(q.rearrange_queue())
for human in q.humans:
	print(human)