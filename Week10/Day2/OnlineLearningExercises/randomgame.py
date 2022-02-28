import sys
from random import randint


comp_num = randint(int(sys.argv[1]), int(sys.argv[2]))

# while True:
# 	try:
# 		user_num = int(input("Guess a random number between 1 and 10: "))
# 		if user_num < 1 or user_num > 10 or type(user_num) != int:
# 			raise ValueError
# 		elif comp_num == user_num:
# 			print("You're a genius!")
# 			break
# 		else:
# 			print("Sorry guess again!")
# 	except ValueError:
# 		print("Enter a number in the range of 1 - 10")


while True:
	try:
		user_num = int(input("Guess a random number between 1 and 10: "))
		if 0 < user_num < 11:
			if comp_num == user_num:
				print("You're a genius!")
				break
			print("Sorry guess again!")
		else:
			print("Enter a number in the range of 1 - 10")
	except ValueError:
		print("Print a valid number")