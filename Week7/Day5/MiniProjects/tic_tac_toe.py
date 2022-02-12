board = [
	[" ", " ", " "],  # [00] [01] [02]
	[" ", " ", " "],  # [10] [11] [12]
	[" ", " ", " "]  # [20] [21] [22]
]

current_player = "X"


def display_board():
	print("TIC TAC TOE")
	print("*****************")
	print(f"*   {board[0][0]} | {board[0][1]} | {board[0][2]}   *")
	print("*  ---|---|---  *")
	print(f"*   {board[1][0]} | {board[1][1]} | {board[1][2]}   *")
	print("*  ---|---|---  *")
	print(f"*   {board[2][0]} | {board[2][1]} | {board[2][2]}   *")
	print("*****************")


#
#
def player_input(player):
	try:
		row = int(input("Enter row between 1 and 3: "))
		column = int(input("Enter row between 1 and 3: "))
		if board[row - 1][column - 1] == " ":
			board[row - 1][column - 1] = player
			switch_player()
		else:
			print("Oops that spot is taken")
		print()
	except IndexError:
		print("Please enter a valid number between 1 and 3")


#
def check_win():
	if board[0][0] == board[0][1] == board[0][2] != " ":
		return True
	elif board[1][0] == board[1][1] == board[1][2] != " ":
		return True
	elif board[2][0] == board[2][1] == board[2][2] != " ":
		return True
	elif board[0][0] == board[1][0] == board[2][0] != " ":
		return True
	elif board[0][1] == board[1][1] == board[2][1] != " ":
		return True
	elif board[0][2] == board[1][2] == board[2][2] != " ":
		return True
	elif board[0][0] == board[1][1] == board[2][2] != " ":
		return True
	elif board[2][0] == board[1][1] == board[0][2] != " ":
		return True
	else:
		return False


def switch_player():
	global current_player
	if current_player == "X":
		current_player = "O"
	else:
		current_player = "X"


# def play():
while True:
	if not check_win():
		player_input(current_player)
		display_board()
	else:
		print("We have a winner!")
		break
