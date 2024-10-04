# Store information about a pizza being ordered.

pizza = {
    'crust': ['thick', 'stuffed'],
    'toppings': ['peparoni', 'sausage', 'extra cheese'],
 }

# Summarize the order.
print(f"You ordered a {pizza['crust'][0]} {pizza['crust'][1]}-crust pizza "
 "with the following toppings:")


for topping in pizza['toppings']:
    print(f"\t{topping.title()}")

print ('\nWould that be all?')