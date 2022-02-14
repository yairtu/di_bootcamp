# class Computer():
#
# 	def description(self, name):
# 		"""
# 		This is a totally useless function
# 		"""
# 		print("I am a computer, my name is", name)
# 		# Analyse the line below
# 		print(self)
#
#
# mac_computer = Computer()
# # mac_computer.brand = "Apple"
# # print(mac_computer.brand)
# #
# # dell_computer = Computer()
# #
# # Computer.description(dell_computer, "Mark")
# # # IS THE SAME AS:
# # dell_computer.description("Mark")
#
# mac_computer.type_of_pc = "mac"
#
# print(mac_computer.t)

class BankAccount:

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append("View Balance")
        print(f"Balance for account {self.account_number}: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount < 100:
            print("Minimum deposit is 100")
        else:
            self.balance += amount
            self.transactions.append(f"Deposit: {amount}")
            print("Deposit Succcessful")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: {amount}")
            print("Withdraw Approved")
            return amount

    def view_transactions(self):
        print("Transactions:")
        print("-------------")
        for transaction in self.transactions:
            print(transaction)


myAccount = BankAccount(123456789, 1000000000)

print(myAccount.view_balance())