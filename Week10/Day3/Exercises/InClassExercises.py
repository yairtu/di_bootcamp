from collections import Counter
import json

# # Read the file line by line
# with open("nameslist.txt") as f:
# 	print(f.readlines())

# # Read only the 5th line of the file
# with open("nameslist.txt") as f:
# 	for i, line in enumerate(f):
# 		if i == 4:
# 			print(line)

# # another way to read 5th line:
# with open("nameslist.txt") as f:
# 	print(f.readline(5))

# # Read only the 5th first characters of the file
# with open("nameslist.txt") as f:
# 	f.seek(4)
# 	print(f.readline())

# # Read all the file and return it as a list of strings. Then split each word
# with open("nameslist.txt") as f:
# 	word_list = f.readlines()
# 	print(word_list)
# 	for word in word_list:
# 		word.split('\n')

# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file


# with open("nameslist.txt") as f:
# 	word_list = f.read().split('\n')
# 	print(f"Lea occurrences: {word_list.count('Lea')}")
# 	print(f"Darth occurrences: {word_list.count('Darth')}")
# 	print(f"Luke occurrences: {word_list.count('Luke')}")
# 	print(Counter(word_list))

# # append your name to the end of the file
# with open("nameslist.txt", "a+") as f:
# 	f.write("\nYair")
# 	f.seek(0)
# 	print(f.readlines())

# # append skywalker to each luke
# with open('nameslist.txt', 'a+') as f:
# 	l = f.read().split('\n')
#
# 	for index, word in enumerate(l):
# 		if word == 'Luke':
# 			l[index] = 'Luke Skywalker'
# 	new_content = '\n'.join(l)
# 	f.write(new_content)
# 	f.seek(0)

