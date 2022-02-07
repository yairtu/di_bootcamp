import random


def get_random_temp(season):
	if season.lower() == "winter":
		return random.randint(-10, 10)
	if season.lower() == "spring":
		return random.randint(10, 20)
	if season.lower() == "summer":
		return random.randint(20, 40)
	if season.lower() == "spring":
		return random.randint(10, 20)


def main():
	season = input("Enter a season(Spring, Summer, Fall, Winter): ")
	temp = get_random_temp(season)
	print(f"The temperature right now is {temp} Celsius")
	if temp < 0:
		print("Brrr, that’s freezing! Wear some extra layers today")
		return
	elif temp < 17:
		print("Quite chilly! Don’t forget your coat")
		return
	elif temp < 24:
		print("It's nice out! I hope it's sunny so you can enjoy the day outside.")
		return
	elif temp < 33:
		print("Beach weather!")
		return
	elif temp < 40:
		print("Its HOT! Remember to drink lots of water.")


main()
