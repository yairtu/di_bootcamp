from anagram_checker import AnagramChecker

print("Welcome to the Anagram Checker!")
print("The rules are as follows\n"
	  "- You can only check one word at a time\n"
	  "- Only alphabetic characters are allowed. No numbers or special characters.\n"
	  "- Enjoy\n")

while True:
	user_input = input("Please enter a word you would like to check, or 'exit' if you would like to quit the "
					   "program: ").lower()
	if user_input.strip() == "exit":
		break
	elif len(user_input.split()) > 1:
		print("You cannot enter more than one word, try again.")
		continue
	else:
		anagrams = "Anagrams for your word: "
		anagram_checker = AnagramChecker("sowpods.txt")
		anagrams_list = anagram_checker.get_anagrams(user_input.lower())
		if len(anagrams_list) == 0:
			print("No anagrams for your word!\n")
		else:
			count = 0
			for word in anagrams_list:
				anagrams += f"{word}{', ' if count < len(anagrams_list )-1 else '.'}"
				count += 1
			print(f'YOUR WORD: "{user_input.upper()}"\n'
				  f'this is a valid English word')
			print(f"{anagrams}\n")