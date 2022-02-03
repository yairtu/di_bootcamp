# # Ex 1
#
# my_fav_numbers = {1, 2, 3, 4, 5}
# my_fav_numbers.update({6, 7})
# my_fav_numbers.remove(7)
# print(my_fav_numbers)
#
# friend_fav_numbers = {10, 11, 12}
# our_favorite_numbers = (my_fav_numbers | friend_fav_numbers)  # same as (my_fav_numbers.union(friend_fav_numbers))
# print(our_favorite_numbers)
#
# # Ex 2
# # Given a tuple which value is integers, is it possible to add more integers to the tuple? No, tuples are not changeable
#
# # 3
# for i in range(1, 21):
# 	print(i)
# 	i += 1
#
# # Ex 4
# # Recap – What is a float? What is the difference between an integer and a float? float is a number with decimal point
# # Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# for i in range(1, 11):
# 	print(i / 2)
#
# # Ex 5
# # Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# #
# # Remove “Banana” from the list.
# # Remove “Blueberries” from the list.
# # Add “Kiwi” to the end of the list.
# # Add “Apples” to the beginning of the list.
# # Count how many apples are in the basket.
# # Empty the basket.
# # Print(basket)
#
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.remove("Blueberries")
# basket.append("Kiwi")
# basket.insert(0, "Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)
#
# # Exercise 6 : Loop
# # Instructions
# # Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
# #
# while True:
# 	userName = input("Enter your name: ")
# 	if userName == "Yair":
# 		break
#
# while input("Enter your name: ") != "Yair":
# 	continue
#
# # Exercise 7
# # Instructions
# # Given a list, use a loop to print out every element which has an even index.
# numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# for e in numList:
# 	if e % 2 == 0:  # Why is is it not printing
# 		print(e)
#
# # Exercise 8
# # Instructions
# # Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
# num = 1500
#
# while num <= 2500:
# 	if not num % 5:
# 		print(num)
# 	if not num % 7:
# 		print(num)
# 	num += 1
#
# # Exercise 9: Favorite Fruits
# # Instructions
# # Ask the user to input their favorite fruit(s) (one or several fruits).
# # Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# # Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# # Now that we have a list of fruits, ask the user to input a name of any fruit.
# # If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# # If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
#
# favFruits = input("What are your favorite fruits? user a comma (,) to separate them: ")
# favFruitsArr = favFruits.split(",")
# fruit = input("Enter a fruit: ")
# if favFruitsArr.__contains__(fruit):
# 	print("You chose one of your favorite fruits! Enjoy!")
# else:
# 	print("You chose a new fruit. I hope you enjoy")
#
# # Exercise 10: Who Ordered A Pizza ?
# # Instructions
# # Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for
# toppings.
# # As they enter each topping, print a message saying you’ll add that topping to their pizza.
# # Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each
# topping).

# toppings = ""
#
# price = 0
# while True:
# 	answer = input("Enter yor toppings: ")
# 	if answer == "quit":
# 		print(f"Total price: {10 + price}\nToppings:\n{toppings}")
# 		break
# 	toppings += f"{answer}\n"
# 	price += 2.5
# 	print("Topping added")
#
# # Exercise 11: Cinemax
# # Instructions
# # A movie theater charges different ticket prices depending on a person’s age.
# # if a person is under the age of 3, the ticket is free.
# # if they are between 3 and 12, the ticket is $10.
# # if they are over the age of 12, the ticket is $15.
# # Ask a family the age of each person who wants a ticket.
# # Store the total cost of all the family’s tickets and print it out.
# # A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people
# between the ages of 16 and 21.
# # Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch
# the movie.
#

cost = 0
# for age in ages:
# 	if int(age) <= 3:
# 		continue
# 	if int(age) <= 12:
# 		cost += 10
# 	if int(age) > 12:
# 		cost += 15
# print(ages)
# print(cost)
#
# ages = input("Enter your age seperated by a comma (,): ").split(",")
# finalAges = []
# print(ages)
#
# for age in ages:
# 	if int(age) >= 16 and int(age) <= 21:
# 		finalAges.append(age)
#
# print(finalAges)
#
# # Exercise
# # 12: Who Is Under 16?
# # Instructions
# # Given a list of names, write a program that asks every user for their age, if they are less than 16 years old remove them from the list.
# # At the end, print the final list.
#
# whatsYourAge = input("What is your age? separate by a comma: ").split(",")
# for age in whatsYourAge:
# 	if int(age) < 16:
# 		whatsYourAge.remove(age)
#
# print(whatsYourAge)

# Exercise 13
# Instructions
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your
# tuna sandwich.

print("The deli has run out of pastrami")

sandwich_orders = ["pastrami", "pastrami", "pastrami", "roast beef", "tuna"]
finished_sandwiches = []
new_Sandwich_List = []
i = 0

for sandwich in sandwich_orders:
	if sandwich != "pastrami":
		new_Sandwich_List.append(sandwich)


sandwich_orders = new_Sandwich_List
print(sandwich_orders)


for sandwich in sandwich_orders:
	finished_sandwiches.append(sandwich)
	print(f"I made your {sandwich} sandwich")
