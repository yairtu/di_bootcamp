# Ex 1

birthday = {
	"talia": "1960/02/27",
	"yair": "1992/12/20",
	"moti": "1987/09/08",
	"ilana": "1989/02/07",
	"igor": "1956/03/28"
}

print("Welcome! You can look up the birthdays of the people on the list!")
userInput = input("Enter a a person's name who's birthday you want to get: ")

print(f"{userInput}'s birthday is {birthday.get(userInput, 'not available')}")

