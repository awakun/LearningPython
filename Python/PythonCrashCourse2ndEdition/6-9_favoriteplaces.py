favorite_places = {
    'Dave': ['Seattle', 'Crystal Mountain'],
    'Lizzy': 'Baltimore',
    'Taylor': ['Philadelphia', 'Tokyo', 'San Francisco']
}

for name, places in favorite_places.items():
    # isinstance checks whether or not an object is of a certain type
    # doing this to see if places is a single string
    if isinstance(places, str):
        print(f"{name} likes {places}!")
    else:
        # join() joins strings, call it on the delimiter(s) you want with the list as the argument
        print(f'{name} likes all these places: {", ".join(places)}!')
