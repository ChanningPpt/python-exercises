buffet = ("burger", "hot dog", "pizza", "macaroni", "steak")
print(f"Here is the menu of the restaurant:")
for meal in buffet:
    print(meal.title())

print(f"\nHere is the new menu:")
buffet = ("burger", "nuggets", "pizza", "macaroni", "chicken")
for meal in buffet:
    print(meal.title())
