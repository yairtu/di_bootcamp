import math


class Circle:

	def __init__(self, radius):
		self.radius = radius

	def __pow__(self, power=2, modulo=None):
		return math.pi * self.radius ** power

	def __add__(self, other):
		return self.__pow__() + other.__pow__()

	def print_circle(self):
		print(f"You have a very nice circle with an area of {self.__pow__()}")

	def compare(self, other):
		'''returns boolean of if self is greater than other.'''
		if isinstance(other, Circle):
			if self.__pow__() == other.__pow__():
				return "Equal"
			else:
				return self.__pow__() > other.__pow__()

	# def sort_circle_list(self, ls):
	# 	for circle in ls:
	# 		if circle


circle1 = Circle(2)
circle2 = Circle(5)
circle3 = Circle(3)
circle4 = Circle(1)

print(circle1.__add__(circle2))
circle2.print_circle()
print(circle2.compare(circle1))

# circles_list = [circle1, circle2, circle3, circle4]
# for circles in circles_list:
# 	if circles_list.__pow__()