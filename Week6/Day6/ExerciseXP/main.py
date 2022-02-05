# # Ex 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# new_dict = dict(zip(keys, values))
# print(new_dict)
#
# # Exercise 2 : Cinemax #2
# print()
# # family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# family = {}
# while True:
# 	userName = input("What is your name? Enter empty to finish.")
# 	if userName == "":
# 		break
# 	userAge = input("What is your age? ")
# 	family[userName] = int(userAge)
#
# sum = 0
# for key in family:
# 	if family[key] < 3:
# 		print(f"{key}'s ticket is free.")
# 		continue
# 	if family[key] <= 12:
# 		print(f"{key}'s ticket cost $10.")
# 		sum += 10
# 	if family[key] > 12:
# 		print(f"{key}'s ticket cost $15.")
# 		sum += 15
# print(f"Total cost of your tickets is ${sum}")

# # Ex 3
# brand = {
#     "name": "Zara",
#     "creation_date": 1975,
#     "creator_name": ["Amancio", "Ortega", "Gaona"],
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {"France": ["blue"], "Spain": ["red"], "US": ["pink", "green"]},
# }
#
# brand["number_stores"] = 2
# print(brand)
# print(f"{brand['name']}'s clients are people who like clothes.")
# brand["country_creation"] = "Spain"
# if "international_competitors" in brand:
#     internationalComps = brand["international_competitors"]
#     brand["international_competitors"].append("Desigual")
# del brand["creation_date"]
# print(brand["international_competitors"][len(brand["international_competitors"]) - 1])
# print(brand["major_color"]["US"])
# print(len(brand))

# Ex 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {}

for i, user in enumerate(users):
    disney_users_A[user] = i
print(disney_users_A)

print()
disney_users_B = {}
for i, user in enumerate(users):
    disney_users_B[i] = user
print(disney_users_B)

print()
users.sort()
disney_users_C = {}
for i, user in enumerate(users):
    disney_users_C[user] = i
print(disney_users_C)

print()

dict_one = {}
for i, key in enumerate(disney_users_A.keys()):
    if "i" in key:
        dict_one[key] = i
print(dict_one)

# print()
# dict_two = {}
# for i, key in enumerate(disney_users_A.keys()):
#     print(key[0])
#     if "m" in key[0]:
#         dict_two[key] = i
#     if "p" in key[0]:
#         dict_two[key] = i
# print(dict_two)