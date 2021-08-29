guests = ['billy', 'bob', 'joe']

invitation = f"Dear {guests[0].title()}, {guests[-1].title()} and {guests[1].title()},\nyou are invited to this party."
print(invitation)

rejection = f"\nHey, it's me, {guests[0].title()} and I can't make it, sorry."
print(rejection)

del guests[0]
guests.insert(0, 'jerry')

invitation = f"\nDear {guests[0].title()}, {guests[-1].title()} and {guests[1].title()},\nyou are invited to this party."
print(invitation)

update = f"\nDear {guests[0].title()}, {guests[-1].title()} and {guests[1].title()}\nI found new table for more people."
print(update)

guests.insert(0, 'chad')
guests.insert(2, 'brad')
guests.append('john')

newInvitation = f"\n{guests[0].title()}, {guests[1].title()}, {guests[2].title()}, {guests[3].title()}, {guests[4].title()} and {guests[5].title()} are invited."
print(newInvitation)

announce = f"\nI have realized the table can only fit 2 people."
print(announce)

apologyOne = f"\nsorry {guests[1].title()}, but ur not cool"
apologyTwo = f"\nsorry {guests[3].title()}, but ur not cool"
apologyThree = f"\nsorry {guests[-1].title()}, but ur not cool"
apologyFour = f"\nsorry {guests[-2].title()}, but ur not cool"

guests.pop(1)
print(apologyOne)

guests.pop(3)
print(apologyTwo)

guests.pop(-1)
print(apologyThree)

guests.pop(2)
print(apologyFour)

print(guests)

announceTwo = f"\n{guests[0].title()} and {guests[1].title()} are the last men standing and can come to party"
print(announceTwo)

del guests[0]
del guests[0]
print(guests)
