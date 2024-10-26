# this prgram will make sanwhiches 

def sanwiches(*toppings):
    print('\nYour sanwich will have: ')
    for topping in toppings:
        print (f"- {topping}")


sanwiches('salami', 'cheese')

sanwiches('Bacon', 'Lettuce', 'Tomato')

sanwiches('Pepperoni')