dinner_guest = ["my first cat", "Yoko Taro", "Kentaro Miura"]

for guest in dinner_guest:
    print (f"Hello {guest} would you like to have dinner with me.")

print (f"Hello {dinner_guest} I have found a bigger table so no I will invite more guest.")

dinner_guest.insert(0, "Richard Garfield")
dinner_guest.insert(3, "Stan Lee")
dinner_guest.append("Hideaki Anno")

for guest in dinner_guest:
    print (f"Hello {guest} would you like to have dinner with me.")

