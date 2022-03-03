class AnagramChecker:

	@staticmethod
	def is_anagram(word1, word2):
		if len(word1) == len(word2):
			sorted_word1 = sorted(word1)
			sorted_word2 = sorted(word2)

			return sorted_word1 == sorted_word2
		return False

	def __init__(self, text_file):
		words = []
		try:
			with open(text_file) as f:
				words = f.read().lower().split('\n')
		except FileNotFoundError:
			print("Sorry file not found")
		self.words = words

	def is_valid_word(self, word):
		return word in self.words

	def get_anagrams(self, word):
		anagrams = []
		for wrd in self.words:
			if self.is_anagram(word, wrd):
				anagrams.append(wrd)
		if word in anagrams:
			anagrams.remove(word)
		return anagrams

# checker = AnagramChecker("sowpods.txt")
# print(checker.get_anagrams("meat"))
