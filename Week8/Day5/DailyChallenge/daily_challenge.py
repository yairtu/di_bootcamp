# Part 1 : Quizz :
# Answer the following questions
#
# What is a class? an object that allows us to make a template of anything
# What is an instance? a copy of a class with the values filled in to identify that instance from another instance of the same class
# What is encapsulation? making certain things private like methods inside of a class to avoid something from changing or overriding a variable unknowingly
# What is abstraction? abstraction is hiding the nitty gritty programming from the input/user
# What is inheritance? inheritance is when one class gets the properties of another class/object
# What is multiple inheritance? When an object inherits multiple parent objects (they are passed to the object as parameters)
# What is polymorphism? Polymorphism is the ability to inherit methods from the parent class but override/change them in the child class
# What is method resolution order or MRO? In multiple inheritence, the order of which python checks the method value

import random


class Deck:
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
			for num in range(1, 14):
				if num == 1:
					self.cards.append(f"A of {suit}")
				elif num == 11:
					self.cards.append(f"J of {suit}")
				elif num == 12:
					self.cards.append(f"Q of {suit}")
				elif num == 13:
					self.cards.append(f"K of {suit}")
				else:
					self.cards.append(f"{num} of {suit}")

	def show(self):
		for card in self.cards:
			print(card)

	def shuffle(self):
		random.shuffle(self.cards)
		return self.cards

	def deal(self):
		return self.cards.pop()


class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def show(self):
		print(f"{self.value} of {self.suit}")


card = Card("Clubs", 5)
card.show()
deck = Deck()
deck.build()
print(deck.shuffle())
print(deck.deal())
print(deck.shuffle())

