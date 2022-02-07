import string
import re  # import regular expression

# imported lower and uppercase alphabet to check array items
lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase

matrix = [
	[7, "i", 3],
	["T", "s", "i"],
	["h", "%", "x"],
	["i", " ", "#"],
	["s", "M", " "],
	["$", "a", " "],
	["#", "t", "%"],
	["^", "r", "!"]
]

# Num array to check for numbers and replace with empty string
numArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

combined_matrix = []

i = 0
while i < len(matrix[i]):
	if i == 0:
		for x in matrix:
			combined_matrix.append(x[i])
	if i == 1:
		for x in matrix:
			combined_matrix.append(x[i])
	if i == 2:
		for x in matrix:
			combined_matrix.append(x[i])
	i += 1

secret_message = ""

for e in combined_matrix:
	if f"{e}" in lower_alphabet:
		secret_message += e
	elif f"{e}" in upper_alphabet:
		secret_message += e
	elif e in numArr:
		secret_message += ""
	else:
		secret_message += " "

print(re.sub(' +', ' ', secret_message))

"""
Converted into methods, still need to figure how to optimize methods though. Any feedback?

import string
import re  # import regular expression

# imported lower and uppercase alphabet to check array items
lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase

matrix = [
	[7, "i", 3],
	["T", "s", "i"],
	["h", "%", "x"],
	["i", " ", "#"],
	["s", "M", " "],
	["$", "a", " "],
	["#", "t", "%"],
	["^", "r", "!"]
]

# Num array to check for numbers and replace with empty string
numArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def matrix_iterate(mat):
	combined_matrix = []
	i = 0
	while i < len(matrix[i]):
		if i == 0:
			for x in matrix:
				combined_matrix.append(x[i])
		if i == 1:
			for x in matrix:
				combined_matrix.append(x[i])
		if i == 2:
			for x in matrix:
				combined_matrix.append(x[i])
		i += 1
	return combined_matrix


def array_checker_to_string(arr):
	secret_message = ""
	for e in arr:
		if f"{e}" in lower_alphabet:
			secret_message += e
		elif f"{e}" in upper_alphabet:
			secret_message += e
		elif e in numArr:
			secret_message += ""
		else:
			secret_message += " "
	return secret_message


print(re.sub(' +', ' ', array_checker_to_string(matrix_iterate(matrix))))
"""