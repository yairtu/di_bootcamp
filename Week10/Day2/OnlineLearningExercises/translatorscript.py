from translate import Translator

translator = Translator(to_lang='ru')

try:
	with open("text.txt", mode="r") as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		print(translation)
except FileNotFoundError as e:
	print("File not found sorry")


