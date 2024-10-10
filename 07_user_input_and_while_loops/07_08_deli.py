# this program will make sandwich orders

sandwich_orders = ['tuna sandwich', 'BLT', 'Bacon egg and cheese' , 'Pulled pork']

finished_orders =[]

while sandwich_orders:
    new_order = sandwich_orders.pop()

    print(f'Your {new_order} is done.')

    finished_orders.append(new_order)
    

print (finished_orders)