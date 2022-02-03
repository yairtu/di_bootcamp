import datetime
#
birthdate = input("Enter your birthdate, (use format: DD/MM/YYYY) or DDMMYYYY: ").split("/")
birthString = birthdate[0]
day = int(birthString[0:2])
month = int(birthString[2:4])
year = int(birthString[4:8])
# print(day)
# print(month)
# print(year)
# print(birthdate)
# print(birthString)
dob = datetime.datetime(year, month, day)
age = (datetime.datetime.now() - dob)
convertDays = int(age.days)
ageYears = convertDays/365
ageYearsString = str(ageYears)
candlesAmount = int(ageYearsString[1])
print(int(ageYears))
underscore = "_"
#
iz = ""
i = 0
while i < candlesAmount:
	iz += "i"
	i += 1

underscore = underscore * int(((11 - candlesAmount) / 2))


print(f"   {underscore}{iz}{underscore}")
print("  |:H:a:p:p:y:|")
print("__|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")