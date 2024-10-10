# this will be a poll for peoples dream vaction spot

responses = {}
polling_active = True
promt = ('If you could go to any place in the world where would you go:')

while polling_active:
    name = input("What is your name?")
    response = input(promt)

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")



