import string

alphabet = string.ascii_lowercase

# letter = "a"
# print(ord(letter))

cipher_text = input("Enter a sentence  you want to encrypt or decrypt: ")
answer = input("Do you want to encrypt or decrypt this message? ").lower()

new_text = ""

if answer == "encrypt":
	for l in cipher_text:
		new_text += chr(ord(l) + 3)
	print(new_text)
if answer == "decrypt":
	for l in cipher_text:
		new_text += chr(ord(l) - 3)
	print(new_text)

