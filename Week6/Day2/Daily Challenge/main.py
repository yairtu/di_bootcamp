import random

userIn = input("Enter a string: ")
if len(userIn) < 10:
    print("String is not long enough")
elif len(userIn) > 10:
    print("String is too long")

print(userIn[0] + userIn[len(userIn) - 1])

newString = ""
for e in userIn:
    newString += e
    print(newString)

newStringArr = []

for e in newString:
    newStringArr.append(e)


random.shuffle(newStringArr)

newString = ""
for e in newStringArr:
    newString += e

print(newString)

