# Conditional Tests
color = 'red'
print("color == red is True.")
print(color == 'red')

print("\ncolor == green is False.")
print(color == 'green')

fruit = 'Banana'
print("\t")
print(fruit == 'banana')
print(fruit.lower() == 'banana')

numberOne = 20
numberTwo = 35
print("\t")
print(numberOne > numberTwo)
print(numberOne >= numberTwo)
print(numberOne <= numberTwo)
print(numberOne < numberTwo)
print("\t")
print(numberOne >= 20 and numberTwo >= 35)
print(numberOne >= 21 or numberTwo >= 36)

drinks = ['water', 'juice', 'soda']
print("\t")
print('water' in drinks)
print('apple cider' in drinks)