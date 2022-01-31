# # Ex 1
# print("hello world\n" * 5 + "I love python\n" * 5)

# Ex 2
month = int(input("Enter a month in the form of a number: "))

if month == 12 or month > 0 and month < 3:
    print("That month is in Winter")
elif month > 2 and month < 6:
    print("That month is in Spring")
elif month > 5 and month < 9:
    print("That month is in Summer")
elif month > 8 and month < 12:
    print("That month is in Autumn")
else:
    print("Invalid month :(")
