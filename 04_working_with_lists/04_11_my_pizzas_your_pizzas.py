
pizzas = ["Pepperoni", "Bacon", "Cheese"]

friends_pizzas = pizzas[ : ]

pizzas.append("Sausage")

friends_pizzas.append("Meat lovers")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friends favortite pizzas are: ")
for friend_pizza in friends_pizzas:
    print(friend_pizza)