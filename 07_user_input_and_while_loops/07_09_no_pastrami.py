# this program will make sandwich orders

sandwich_orders = ['Pastrami' ,'tuna sandwich', 'BLT', 'Pastrami', 'Bacon egg and cheese' , 'Pulled pork' , 'Pastrami']

finished_orders =[]

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print('Sorry, we have no pastrami.')

while sandwich_orders:
    new_order = sandwich_orders.pop()

    print(f'Your {new_order} is done.')

    finished_orders.append(new_order)
    

print (finished_orders)