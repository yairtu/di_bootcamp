# # Ex 1

# class Circle:
# 	color = "red"
#
# 	def __init__(self, diameter):
# 		self.diameter = diameter
#
# 	def grow(self, factor=2):
# 		self.diameter = self.diameter * factor
#
# 	def get_color(self):
# 		return Circle.color
#
#
# circle1 = Circle(2)
# print(circle1.color) # output: red
# print(Circle.color) # output: red
# print(circle1.get_color()) # output: red
# circle1.grow(3)
# print(circle1.diameter) # output: 6

# # Ex 2
#
# class MyClass(object):
# 	count = 0
#
# 	def __init__(self, val):
# 		self.val = val
# 		MyClass.count += 1
#
# 	def set_val(self, newval):
# 		self.val = newval
#
# 	def get_val(self):
# 		return self.val
#
# 	@classmethod
# 	def get_count(cls):
# 		return cls.count
#
#
# object_1 = MyClass(10)
# print("\nValue of object : %s" % object_1.get_val()) # value 10
# print(MyClass.get_count()) # count 1
#
# object_2 = MyClass(20)
# print("\nValue of object : %s" % object_2.get_val()) # value 20
# print(MyClass.get_count()) # count 2

# # Ex 3
#
# class MyClass(object):
# 	count = 0
#
# 	def __init__(self, val):
# 		self.val = self.filterint(val)
# 		MyClass.count += 1
#
# 	@staticmethod
# 	def filterint(value):
# 		if not isinstance(value, int):
# 			print("Entered value is not an INT, value set to 0")
# 			return 0
# 		else:
# 			return value
#
#
# a = MyClass(5)
# b = MyClass(10)
# c = MyClass(15)
#
# print(a.val)
# print(b.val)
# print(c.val)
# print(a.filterint(100))

class PrintList(object):

    def __init__(self, my_list):
        self.mylist = my_list

    def __repr__(self):
        return str(self.mylist)


printlist = PrintList(["a", "b", "c"])
print(printlist.__repr__())