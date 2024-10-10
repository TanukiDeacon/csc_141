# this program will check if their is enough space for your group

# this is the input for how many in the group
group = input("How big is your group: ")
# this will make it into an int
group = int(group)

#this will tell you if we have space
if group > 8:
    print("Sorry but you will have to wait for a table.")
else:
    print("Your table is ready.")