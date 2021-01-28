pet_0 = {'owner': 'Ali', 'name': 'Chernk', 'type': 'dog'}
pet_1 = {'owner': 'Phil', 'name': 'Ash', 'type': 'cat'}
pet_2 = {'owner': 'DK', 'name': 'Midnight', 'type': 'cat'}

pets = [pet_0, pet_1, pet_2]
for pet in pets:
    print(f"{pet['name']} is owned by {pet['owner']} and is a {pet['type']}.")
