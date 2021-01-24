basic_menu = ('Steak', 'Potatoes', 'Asparagus', 'Avacados', 'Ice Cream')
for food in basic_menu:
    print(food)

# Should fail (and does, TypeError):
# basic_menu[2] = 'Hamburger'

basic_menu = ('Hamburger', 'Steak', 'Avacados', 'Pie', 'Asparagus')
for food in basic_menu:
    print(food)