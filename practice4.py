# Every Function Exercise

countries = ['china', 'india', 'usa', 'japan', 'mexico', 'uk', 'australia']
message = f"The country I live in is {countries[2].upper()}"
print(message)

print(countries)
print(countries[0].title())

countries.sort()
print(countries)
print(countries[0].title())

countries[0] = 'alaska'
print(countries)

countries.append('russia')
print(countries)

countries.insert(0, 'canada')
print(countries)

del countries[0]
print(countries)

del countries[0]
print(countries)

countriesPopped = countries.pop()
print(countries)
print(countriesPopped.title())

visitCountry = countries.pop(0)
print(f"I want to visit {visitCountry.title()}")

print(countries)
ignoredCountry = 'india'
countries.remove(ignoredCountry)
print(countries)
print(f"I would not visit {ignoredCountry.title()}")

print(f"\nHere is original list:")
print(countries)

print(f"\nHere is reversed list:")
print(sorted(countries, reverse=True))

print(f"\nHere is original list again:")
print(countries)
print(len(countries))
