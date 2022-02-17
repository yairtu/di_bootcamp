from game import *


def get_user_menu_choice():
	print("\tMenu:")
	print("\t(g) Play a new game")
	print("\t(x) Show scores and exit")
	user_input = input("\t :  ")
	return user_input


def print_results(results):
	print("\nThanks for playing!")
	for key in results:
		print(f"{key} : {results[key]}")

def main():
	new_game = Game()
	user_input = get_user_menu_choice()
	while user_input != "x":
		new_game.play()
		user_input = get_user_menu_choice()
	print_results(new_game.show_outcomes())

main()