class BankAccount:
	def __init__(self, username, password):
		self.balance = 0
		self.username = username
		self.password = password
		self.authenticated = False

	def deposit(self, amount):
		# increase account balance
		if self.authenticated:
			try:
				if amount < 0:
					raise ValueError
				else:
					self.balance += amount
			except ValueError:
				print("You cannot deposit a negative amount")

	def withdraw(self, amount):
		if self.authenticated:
			try:
				if amount < 0:
					raise ValueError
				elif self.balance - amount < 0:
					raise ValueError
				else:
					self.balance -= amount
					print(f"Withdrawal successful. Current balance: {self.balance}")
			except ValueError:
				print("You cannot withdraw that amount")

	def authenticate(self, username, password):
		self.authenticated = self.username == username and self.password == password
		return self.authenticated


class MinimumBalanceAccount(BankAccount):
	def __init__(self, username, password):
		super().__init__(username, password)
		self.minimum_balance = 0

	def withdraw(self, amount):
		try:
			if self.minimum_balance > self.balance - amount:
				raise ValueError
			else:
				self.balance -= amount
		except ValueError:
			print(f"Balance not enough, the maximum you can withdraw is {self.balance}")


class ATM:
	def __init__(self, account_list, try_limit):
		for account in account_list:
			if isinstance(account, (BankAccount, MinimumBalanceAccount)):
				self.account_list = account_list
			else:
				raise Exception("Invalid accounts")
		try:
			assert try_limit > 0
		except AssertionError:
			print("Try limit cannot be negative")
			self.try_limit = 2
		else:
			self.try_limit = try_limit
		self.current_tries = 0
		self.show_main_menu()

	def show_main_menu(self):
		while True:
			username = str(input("Enter your username or exit: "))
			if username == "exit":
				print("Goodbye")
				break
			password = str(input("Enter your password: "))
			self.log_in(username, password)
			if self.current_tries >= self.try_limit:
				return print("You are out of tries")

	def log_in(self, username, password):
		for account in self.account_list:
			if account.authenticate(username, password):
				return self.show_account_menu(account)
			else:
				self.current_tries += 1

	def show_account_menu(self, account):
		print("Welcome to your account")
		while True:
			user_input = input("Would you like to withdraw, deposit or exit? ")
			if user_input == "exit":
				break
			elif user_input == "withdraw":
				amount = int(input("How much would you like to withdraw? "))
				account.withdraw(amount)
			elif user_input == "deposit":
				account.deposit(int(input("How much would you like to deposit? ")))
				print(f"Deposit successful. Current balance: {account.balance}")
		return print("Hope to see you again soon!")


boa = ATM([BankAccount('test', 'test'), MinimumBalanceAccount('test', 'test')], 2)