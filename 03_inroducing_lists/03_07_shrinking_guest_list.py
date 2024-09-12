dinner_guest = ["my first cat", "Yoko Taro", "Kentaro Miura"]

for guest in dinner_guest:
    print (f"Hello {guest} would you like to have dinner with me.")

print (f"Hello {dinner_guest} I have found a bigger table so no I will invite more guest.")

dinner_guest.insert(0, "Richard Garfield")
dinner_guest.insert(3, "Stan Lee")
dinner_guest.append("Hideaki Anno")

for guest in dinner_guest:
    print (f"Hello {guest} would you like to have dinner with me.")

print (f"Hello {dinner_guest} I am sorry to inform you that I can only invite 2 guest.")

print (f"I am sorry {dinner_guest[5]} you are no longer invited")
dinner_guest.pop()
print (f"I am sorry {dinner_guest[4]} you are no longer invited")
dinner_guest.pop()
print (f"I am sorry {dinner_guest[3]} you are no longer invited")
dinner_guest.pop()
print (f"I am sorry {dinner_guest[2]} you are no longer invited")
dinner_guest.pop()


for guest in dinner_guest:
    print (f"{guest} you are still invited")

del dinner_guest[1]
del dinner_guest[0]

print (dinner_guest)
