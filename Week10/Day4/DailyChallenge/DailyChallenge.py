from collections import Counter
import re


class Text:
	def __init__(self, file):
		self.file = file

	@staticmethod
	def most_common_word(counter_dictionary):
		try:
			print(counter_dictionary.most_common(1))
		except NameError:
			print("Unable to check most common word")

	def get_words_from_file(self):
		try:
			with open(self.file) as f:
				words_in_file = re.split('; |,\|\*|\n| ', f.read().lower())
				word_count = Counter(words_in_file)
				print(f"Each word occurrence: {word_count}")
				return word_count
		except FileNotFoundError as e:
			print("File not found")

	def get_unique_words(self):
		try:
			with open(self.file) as f:
				words_in_file = re.split("; |,\|\*|\n| |'|", f.read().lower())
				unique_words = []
				for word in words_in_file:
					if word not in unique_words:
						unique_words.append(word)
				return unique_words
		except FileNotFoundError:
			print("File not found")

	# a class method that returns a Text instance but with a text file: >>> Text.from_file('the_stranger.txt')
	# not sure what to do here?
	@classmethod
	def from_file(cls, file):
		return cls.from_file(file)


class TextModification(Text):
	def __init__(self, file):
		super().__init__(file)

	def no_punctuation(self):
		with open(self.file) as f:
			words_in_file = re.split(r'[^\w\s]', f.read())
			not_punctuated = ""
			for word in words_in_file:
				not_punctuated += f"{word.lower()} "
			return not_punctuated.strip()

	def stop_words_list(self):
		with open("stop_words.txt", encoding="utf8") as f:
			stop_words_list = f.read().split('\n')
			return stop_words_list

	def remove_stop_words(self):
		no_stop_words_list = []
		with open("the_stranger.txt") as f:
			words_in_file = re.split('; |,\|\*|\n| ', f.read().lower())
		for word in words_in_file:
			if word not in self.stop_words_list():
				if word != "":
					no_stop_words_list.append(word)
		no_stop_words_story = ""
		for word in no_stop_words_list:
			no_stop_words_story += f"{word} "
		return no_stop_words_story.strip()


# my_file = Text("the_stranger.txt")
#
# my_file.get_words_from_file()
# my_file.most_common_word(my_file.get_words_from_file())
#
mod = TextModification("the_stranger.txt")
# # print(mod.no_punctuation())
print(mod.remove_stop_words())

