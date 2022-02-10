people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

filtered_list = list(filter(lambda a: len(a) < 5, people))
mapped_list = list(map(lambda a: f"Hello {a}", filtered_list))

print(mapped_list)