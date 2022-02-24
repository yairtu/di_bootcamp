class Character:

	def __init__(self, name, attack):
		self.name = name
		self.attack = attack
		self.life = 20

	def basic_attack(self, other):
		other.life -= self.attack
		return other

	def __str__(self):
		return f"Character: {self.name}, Life: {self.life}, Attack: {self.attack}"


class Druid(Character):

	def __init__(self, name, attack):
		super().__init__(name, attack)
		print("Keepers of Nature")

	def meditate(self):
		self.life += 10
		self.attack += 2
		return self

	def animal_help(self):
		self.attack += 5
		return self

	def fight(self, other):
		other.life -= (0.75 * self.life + 0.75 * self.attack)
		return other


class Warrior(Character):

	def __init__(self, name, attack):
		super().__init__(name, attack)
		print("A warrior never worries about his fear.")

	def brawl(self, other):
		other.life -= (2 * self.attack)
		self.life += (0.5 * self.attack)
		return other

	@staticmethod
	def roar(other):
		other.attack -= 3
		return other


class Mage(Character):
	def __init__(self, name, attack):
		super().__init__(name, attack)
		print("Abra Kadabra!")

	@staticmethod
	def curse(other):
		other.attack -= 2
		return other

	def summon(self):
		self.attack += 3
		return self

	def cast_spell(self, other):
		other.life -= (self.attack / self.life)
		return other


druid = Druid("Rey", 4)
war = Warrior("Tar", 6)
gandalf = Mage("Gandalf", 8)

print(druid.meditate())
print(gandalf.cast_spell(war))
