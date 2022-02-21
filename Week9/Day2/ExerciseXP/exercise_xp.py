# # Ex 1
#
# my_num = 5
#
#
# def print_functions(func):
# 	'''Prints functions.'''
# 	print(func)
#
#
# print_functions(my_num.__int__())
# print_functions(abs(my_num))
# print_functions(input(my_num))

# Ex 2

class Currency:
	def __init__(self, currency, value):
		self.currency = currency
		self.value = value

	def __add__(self, other):
		if type(other) is int:
			return Currency(self.currency, self.value + other)

		try:
			if self.currency != other.currency and type(other) != type(int):
				raise TypeError
			else:
				return Currency(self.currency, self.value + other.value)
		except TypeError:
			return print(f"Cannot add between Currency type {self.currency} and {other.currency}")

	def __str__(self):
		return f"{self.value} {self.currency}{'s' if self.value > 1 else ''}"

	def __int__(self):
		return self.value

	def __repr__(self):
		return f"{self.value} {self.currency}{'s' if self.value > 1 else ''}"

	def __iadd__(self, other):
		if type(other) is int:
			return Currency(self.currency, self.value + other)

		try:
			if self.currency != other.currency and type(other) != type(int):
				raise TypeError
			else:
				return Currency(self.currency, self.value + other.value)
		except TypeError:
			print("Cannot add different currency types")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
print(c1 + c3)  # my error handler returns none too, and im not sure why
