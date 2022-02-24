class Temperature:

	def __int__(self, temp):
		self.temp = temp


class Celcius(Temperature):
	def __init__(self, temp):
		super().__init__(temp)

	@staticmethod
	def convert(self, other):
		if isinstance(other, Kelvin):
			return


class Kelvin(Temperature):
	def __init__(self, temp):
		super().__init__(temp)


class Fahrenheit(Temperature):
	def __init__(self, temp):
		super().__init__(temp)
