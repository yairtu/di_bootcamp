# Ex 1
print("Hello world\nHello world\nHello world\nHello world")

# Ex 2
print()
print((99**3)*8)

# Ex 3
# >>> 5 < 3   true
# >>> 3 == 3  true
# >>> 3 == "3" false
# >>> "3" > 3 error? or NaN?
# >>> "Hello" == "hello" false

# Ex 4
print()
computer_brand = "Eluktronics"
print(f"I have an {computer_brand} computer")

# Ex 5
print()
name = "Yair"
age = 28
shoe_size = 43
info = f"My name is {name}, I am {age}, my shoe size is {shoe_size}, and Skiing is my favorite sport"
print(info)


# Ex 6
print()
a = 6
b = 5
if a > b:
    print("Hello World")

# Ex 7
print()
userNum = int(input("Enter a number: "))

if not userNum % 2:
    print(f"{userNum} is even")
else:
    print(f"{userNum} is odd")

# Ex 8
print()
usersName = input("What is your name? ")
if usersName == name:
    print("No way! We have the same last name!")

# Ex 9
print()
height = int(input("How tall are you? "))
if height > 145:
    print("You are tall enough to go on the ride")
else:
    print("Sorry, you need to grow some more before you can go on this ride :(")
