class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def set_left(self, node):
		self.left = node

	def set_right(self, node):
		self.right = node

	def set_value(self, value):
		self.value = value

	def get_value(self):
		return self.value

	def add_node(self, node):
		if not self.value:
			self.value = node
			return
		if node == self.value:
			return
		if node < self.value:
			if self.left:
				self.left.add_node(node)
				return
			self.left = Node(node)
			return
		if self.right:
			self.right.add_node(node)
			return
		self.right = Node(node)

	def search(self, value):
		if value < self.value:
			if self.left is None:
				return f"{value} Not found"
			return self.left.search(value)
		elif value > self.value:
			if self.right is None:
				return f"{value} Not found"
			return self.right.search(value)
		else:
			print(f"{self.value} is found")

	def print_tree(self):
		if self.left:
			self.left.print_tree()
		print(self.value)
		if self.right:
			self.right.print_tree()


root = Node(11)
root.add_node(7)
root.add_node(14)
root.add_node(4)
root.add_node(16)
root.add_node(-1)
root.add_node(21)
root.search(7)
root.print_tree()
