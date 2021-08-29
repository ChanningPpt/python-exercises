pizzas = ['cheese', 'pepperoni', 'hawaiian']
friendPizzas = pizzas[:]

pizzas.append('margarita')
friendPizzas.append('buffalo')

print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print(f"\nMy friend's favorite pizzas are:")
for friendPizza in friendPizzas:
    print(friendPizza.title())
