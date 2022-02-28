# from translate import Translator
from deep_translator import GoogleTranslator

# https://deep-translator.readthedocs.io/en/latest/README.html#quick-start

# https://www.delftstack.com/howto/python/python-convert-list-into-dictionary/

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]


def translate_word_list_to_dict(word_list: list):
	list_to_append = []
	for word in word_list:
		translated = GoogleTranslator(source='fr', target='en').translate(word)
		list_to_append.append(translated)
		translation_dict = dict(zip(word_list, list_to_append))
	return translation_dict


print(translate_word_list_to_dict(french_words))

# Doesn't work because translation limit is reached, so I used Googletranslate package instead
# # https://www.delftstack.com/howto/python/python-convert-list-into-dictionary/
#
# french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
#
# translator = Translator(to_lang='en')
# en_translation = []
#
# for word in french_words:
# 	translation = translator.translate(word)
# 	print(translation)
# 	en_translation.append(translation)
#
# translation_dict = dict(zip(french_words, en_translation))
#
# print(translation_dict)
