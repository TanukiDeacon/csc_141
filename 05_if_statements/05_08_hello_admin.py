# this program will loop through usernames to give greetings 

names = ["admin", 'Derian', 'Jack', 'Sam', 'Roger']

for name in names:
    if name == "admin":
        print ("Hello admin, would you like to see a status report?")
    else:
        print(f'Hello {name}, thank you for logging in again.')