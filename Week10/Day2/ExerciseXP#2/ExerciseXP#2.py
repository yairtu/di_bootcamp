import datetime
from faker import Faker

# # Ex 1 Create a function that displays the current date.
# def today():
# 	print(datetime.datetime.today())
#
#
# today()
#
#
# # Ex 2 Create a function that displays the amount of time left from now until January 1st.
# def time_til_jan1():
# 	today = datetime.datetime.now()
# 	jan1 = datetime.datetime(datetime.datetime.today().year + 1, 1, 1, 0, 0, 0)
# 	print(f"January first is in {str((jan1 - today)).replace(',', ' and')} hours")
#
#
# time_til_jan1()

# # Ex 3 Create a function that accepts a birthdate as an argument (in the format of your choice), then display a
# message stating how many minutes the user has been alive.

# def alive_for():
# 	try:
# 		birthday = datetime.datetime.strptime(input("Enter your birthday (day/month/year): "), "%d/%m/%Y")
# 		now = datetime.datetime.now()
# 		alive_time = now - birthday
# 		print(alive_time)
# 		print(f"You have been alive for {(alive_time.days * 24 * 60)} minutes")
# 	except ValueError:
# 		print("Enter your birthday in the valid format (day/month/year)")
#
#
# alive_for()

# # Ex 4 Print when the next holiday is
# purim = datetime.datetime(2022, 3, 15)
#
#
# def next_holiday():
# 	today = datetime.datetime.now()
# 	print(f"Purim is in {str((purim - today)).replace(',', ' and')} hours")
#
#
# next_holiday()

# # Ex 5 How old are you on jupiter?
# age = int(input("How old are you? "))
# print(f"On Jupiter you are {age / 11.862615} years old")


fake = Faker()


def create_users(how_many: int):
	users = []
	for i in range(how_many):
		new_user = {}
		new_user["name"] = fake.name()
		new_user["address"] = fake.address()
		new_user["language_code"] = fake.language_code()
		users.append(new_user)
	return users


print(create_users(5))
