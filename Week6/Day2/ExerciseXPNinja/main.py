# # Ex 3
# 3 <= 3 < 9        true
# 3 == 3 == 3       true
# bool(0)           false
# bool(5 == "5")    false
# bool(4 == 4) == bool("4" == "4")          true
# bool(bool(None))                   not sure need explanation.

# x = (1 == True)
# y = (1 == False)
# a = True + 4
# b = False + 10
#
# print("x is", x)               true
# print("y is", y)               false
# print("a:", a)                 5
# print("b:", b)                 10

# Ex 4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore" \
          " magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo" \
          " consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur." \
          " Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

print(len(my_text))

# Ex 5

while True:
    userWord = input("Enter the longest sentence you can without the letter 'A': ")
    if not userWord.__contains__("a") and not userWord.__contains__("A"):
        print("Congrats!")
        continue
    else:
        break
