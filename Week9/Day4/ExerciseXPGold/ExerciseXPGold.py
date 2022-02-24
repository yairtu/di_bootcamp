class Door:
	objs = 0

	def __init__(self, locked):
		Door.objs += 1
		self.id = Door.objs
		self.locked = locked
		self.next = []

	def next_doors(self):
		if self.id < Door.objs:
			for num in range(self.id + 1, Door.objs):
				self.next.append(num)

	def can_go_to(self, other_door):
		self.next_doors()
		if self.id < other_door.id and not other_door.locked:
			return True
		elif self.id > other_door.id:
			return False
		else:
			return False


door1 = Door(False)
door2 = Door(False)
door3 = Door(False)
door4 = Door(True)
door5 = Door(False)
door6 = Door(False)
door7 = Door(False)

print(door5.can_go_to(door1))


