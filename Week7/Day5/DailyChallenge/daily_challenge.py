words = input("Enter words you want to sort alphabetically split by a comma: ")

words_to_organize = words.strip().split(",")
words_to_organize.sort()

print(",".join(words_to_organize))