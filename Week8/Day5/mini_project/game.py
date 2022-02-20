import random


class Game:
	def __init__(self):
		self.items = ["rock", "paper", "scissors"]
		self.game_outcomes = {"win": 0, "lose": 0, "draw": 0}

	def get_user_item(self):
		# answer = ["rock", "papers", "scissors"]
		user_input = ""
		while user_input not in self.items:
			user_input = input(f"Choose {self.items}\n").lower().strip()
		return user_input

	def get_computer_item(self):
		return random.choice(self.items)

	def get_game_result(self, user_item, computer_item):
		if user_item == computer_item:
			return "draw"
		if (user_item == "rock" and computer_item == "scissors") or (
				user_item == "paper" and computer_item == "rock") or (
				user_item == "scissors" and computer_item == "paper"):
			return "win"
		else:
			return "lose"

	def play(self):
		user_item = self.get_user_item()
		computer_item = self.get_computer_item()
		result = self.get_game_result(user_item, computer_item)
		print(f"You selected {user_item}. The computer selected {computer_item}. You {'drew' if result == 'draw' else result}")
		self.game_outcomes[result] += 1
		return result

	def show_outcomes(self):
		return self.game_outcomes

