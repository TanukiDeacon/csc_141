# this will print a list of pets

pets = []


# this is making the dictionaries
pet1 = {
    'Species' : 'cat',
    'Owner' : 'Derian',
    'Name' : 'Bruno',
    'Gender' : 'Male'
    }


pet2 = {
   'Species' : 'cat',
    'Owner' : 'Derian',
    'Name' : 'Mishu',
    'Gender' : 'Female'
    }


pet3 = {
   'Species' : 'dog',
    'Owner' : 'Derian',
    'Name' : 'Kira',
    'Gender' : 'Female'
    }

# this puts them in the list
pets.append(pet1)
pets.append(pet2)
pets.append(pet3)


for pet in pets:
    print (f'\n{pet}')