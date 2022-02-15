class Phone:
	def __init__(self, phone_number):
		self.phone_number = phone_number
		self.call_history = []
		self.messages = []

	def call(self, other_phone):
		last_call = f"{self.phone_number} called {other_phone.phone_number}"
		print(last_call)
		self.call_history.append(last_call)

	def show_call_history(self):
		print(self.call_history)

	def send_message(self, other_phone, content):
		self.messages.append({"to": other_phone.phone_number, "from": self.phone_number, "content": content})
		other_phone.messages.append({"to": "", "from": self.phone_number, "content": content})

	def show_outgoing_messages(self):
		for dictionary in self.messages:
			if dictionary.get("from") == self.phone_number:
				print(dictionary)

	def show_incoming_messages(self):
		for dictionary in self.messages:
			if dictionary.get("to") == "":
				print(dictionary)

	def show_messages_from(self, number):
		for dictionary in self.messages:
			if dictionary.get("from") == number:
				print(dictionary)
	#
	# def receive_message(self):


my_phone = Phone(111111111)
other_phone1 = Phone(222222222)

my_phone.send_message(other_phone1, "Hello")
my_phone.send_message(other_phone1, "Bye")
my_phone.send_message(other_phone1, "Sup")

# my_phone.show_outgoing_messages()
# my_phone.show_outgoing_messages()
other_phone1.show_incoming_messages()
print()
other_phone1.show_messages_from(111111111)

# my_num = 111111111
# list_dictionary = [{"to": 111111111, "from": 222222222, "content": "Hello"},
# 				   {"to": 222222222, "from": 111111111, "content": "Hello"}]
#
# for dictionary in list_dictionary:
# 	if dictionary.get("from") == my_num:
# 		print(dictionary)

