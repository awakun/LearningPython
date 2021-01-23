# Adding an if statement so that the print statements aren't so wrong!
# This was not part of the exercise
animals = ['Dog', 'Cat', 'Dolphin', 'Wolf', 'Polar bear', 'Penguin']
for animal in animals:
    if animal == 'Dog' or animal == 'Cat':
        print(f"A {animal.lower()} would make a great pet!")
    else:
        print(f"A {animal.lower()} would NOT make a great pet.")
print("You should be careful about what sort of animal you pick as a pet!")
