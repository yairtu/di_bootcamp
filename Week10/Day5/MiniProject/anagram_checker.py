class AnagramChecker:

	@staticmethod
	def is_anagram(word1, word2):
		if len(word1) == len(word2):
			sorted_word1 = sorted(word1)
			sorted_word2 = sorted(word2)

			if sorted_word1 == sorted_word2:
				return True
			else:
				return False

	def __init__(self, text_file):
		try:
			with open(text_file) as f:
				words = f.read().lower().split('\n')
		except FileNotFoundError:
			print("Sorry file not found")
		self.words = words

	def is_valid_word(self, word):
		if word in self.words:
			return True
		else:
			return False

	def get_anagrams(self, word):
		anagrams = []
		for wrd in self.words:
			if self.is_anagram(word, wrd):
				anagrams.append(wrd)
		try:
			anagrams.remove(word)
		except ValueError:
			print("This is not a valid english word")
		return anagrams


# checker = AnagramChecker("sowpods.txt")
# print(checker.get_anagrams("meat"))