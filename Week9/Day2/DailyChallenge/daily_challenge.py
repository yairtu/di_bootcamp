import math

class Circle:

	def __init__(self, radius):
		self.radius = radius

	def __pow__(self, power=2, modulo=None):
		return math.pi * self.radius ** power

	def __add__(self, other):
		return self.__pow__() + other.__pow__()


circle = Circle(5)
circle2 = Circle(2)

print(circle.__add__(circle2))