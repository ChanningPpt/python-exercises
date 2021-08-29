# Exercises 4-3 to 4-9
squares = list(range(1, 20))
for value in squares:
    print(value)

digits = list(range(1, 20, 2))
for digit in digits:
    print(digit)

numbers = list(range(3, 30, 3))
for number in numbers:
    print(number)

cubes = [cube**3 for cube in range(1, 10)]
print(cubes)
