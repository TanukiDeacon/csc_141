# This will tell you the price of your ticket depending on your age.

prompt = ('What is your age: ')
print ('Input quit to stop')


while True:
    age = input(prompt)
    age = int(age)

    if age < 3:
       print('Your ticket is free.')
    elif age <= 12:
       print('Your ticket is $10.')
    elif age > 12:
       print('Your ticket is $15')

    if age == 'quit':
       break