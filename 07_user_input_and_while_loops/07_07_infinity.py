# This will give an infinite loop


prompt = ('What is your age: ')
print ('Input quit to stop')
# put this in the whille loop so it isn't infinite anymore
age = input(prompt)
age = int(age)

while True:

    if age < 3:
       print('Your ticket is free.')
    elif age <= 12:
       print('Your ticket is $10.')
    elif age > 12:
       print('Your ticket is $15')

    if age == 'quit':
       break