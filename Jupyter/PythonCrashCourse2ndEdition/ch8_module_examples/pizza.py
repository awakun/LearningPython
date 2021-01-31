def make_pizzas(size, *toppings):
    """Describe the pizza that will be made"""
    print(f"A {size} pizza will be made with the following toppings:")
    for topping in toppings:
        print(f"{topping}")
