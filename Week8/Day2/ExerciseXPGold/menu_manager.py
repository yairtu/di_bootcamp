class MenuManager:
	def __init__(self):
		self.menu = []

	def add_item(self, name, price, spice, gluten):
		self.menu.append({name, price, spice, gluten})

	def update_item(self, name, price, spice, gluten):
		for index in range(len(self.menu)):
			if name in self.menu[index]:
				del self.menu[index]
				self.menu.append({name, price, spice, gluten})
			else:
				print("The dish is not in the menu")

	def remove_item(self, name):
		for index in range(len(self.menu)):
			if name in self.menu[index]:
				del self.menu[index]
				# print(self.menu)
				return self.menu
			else:
				print("The dish is not in the menu")


menu = MenuManager()

menu.add_item("Soup", 10, "B", False)
menu.add_item("Hamburger", 15, "A", True)

menu.update_item("Soup", 10, "5", True)
#
print(menu.remove_item("Hamburger"))