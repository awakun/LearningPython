# From exer 4-7
threes = list(range(3, 31, 3))
for number in threes:
    print(number)

print(f'The first three values are: {threes[:3]}')
print(f'Three items from the middle of the list are: {threes[2:5]}')
print(f'The last three items in the list are: {threes[-3:]}')