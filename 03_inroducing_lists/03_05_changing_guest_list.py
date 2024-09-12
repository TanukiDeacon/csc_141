
dinner_guest = ["my first cat", "Yoko Taro", "Kentaro Miura"]

for guest in dinner_guest:
    print (f"Hello {guest} would you like to have dinner with me.")

print(f"{dinner_guest[1]} cant make it.")

del dinner_guest[1]

dinner_guest.append("Hideaki Itsuno")

for guest in dinner_guest:
    print (f"Hello {guest} would you like to have dinner with me.")