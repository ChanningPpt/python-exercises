usernames = ['admin', 'john', 'daniel', 'philip', 'tim']
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Welcome, almighty admin!")
        else:
            print(f"Hello, {username.title()}.")
else:
    print("We need to find users!")

currentUsers = ['jack', 'bill', 'PHIL', 'lana', 'jim']
newUsers = ['justin', 'louis', 'phil', 'peter', 'mike']

checkCurrentUsers = {currentUser.lower() for currentUser in currentUsers}
print("\t")
for newUser in newUsers:
    if newUser.lower() in checkCurrentUsers:
        print(f"{newUser} is unavailable. Please pick another name.")
    else:
        print(f"Welcome, {newUser}")

print("\t")
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for number in numbers:
    if number == '1':
        print(f"{number}st")
    elif number == '2':
        print(f"{number}nd")
    elif number == '3':
        print(f"{number}rd")
    else:
        print(f"{number}th")