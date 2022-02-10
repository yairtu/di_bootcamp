# Ex 1

current_year = 2022
current_month = 2

while True:
	try:
		birth_year = int(input("Enter your birth year: "))
		birth_month = int(input("Enter your birth month: "))
		birth_day = int(input("Enter your birth day: "))
		break
	except:
		print("Enter a valid number")

user_gender = input("What is your gender (M or F)? ").lower()
dob = f"{birth_year}/{birth_month}/{birth_day}"


def get_age(year, month, day):
	while True:
		try:
			if current_year - year < 0:
				print("Enter a valid year")
				continue
			elif current_month < month:
				year -= 1
			return current_year - year
		except:
			print("Something went wrong")


def can_retire(gender, date_of_birth):
	if gender == "f":
		return get_age(birth_year, birth_month, birth_day) >= 62
	elif gender == "m":
		return get_age(birth_year, birth_month, birth_day) >= 67


print(can_retire(user_gender, dob))

# Ex 2
def add_multiples(x):
	x = str(x)
	return int(x) + int(x*2) + int(x*3) + int(x*4)


print(add_multiples(3))
