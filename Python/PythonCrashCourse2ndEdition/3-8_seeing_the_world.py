places_to_visit = ['Australia', 'Whistler',
                   'London', 'New Zealand', 'Tokyo', 'Berlin']

# print original order
print(places_to_visit)

# print sorted order but maintain original order
print(sorted(places_to_visit))

# re-print original order
print(places_to_visit)

places_to_visit.reverse()
print(places_to_visit)

# reverse it again
places_to_visit.reverse()
print(places_to_visit)

# sort it permanently
places_to_visit.sort()
print(places_to_visit)

# sort it in reverse order
places_to_visit.sort(reverse=True)
print(places_to_visit)

# this is basically the next exercise (3-9):
print(f'number of places: {len(places_to_visit)}')