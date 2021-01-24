# From 4-1
pizzas = ['Pepperoni', 'Chicken, bacon, ranch', 'Mediterranean']
for pizza in pizzas:
    message = f'I like {pizza} pizza.'
    print(message)
print('I really love pizza!')

friend_pizzas = pizzas[:]
pizzas.append('Meat')
friend_pizzas.append('Veggie')

print(f'My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)