# this program will input what pizza toppings you want

prompt = ('What toppings do you want: ')
print ('Input quit when you are done')

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f'We will put {toppings} on your pizza!')