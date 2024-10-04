# this program will store multiple dictiinaries about a person in a list

people = []


# this is making the dictionaries
person1 = {
    "First name": "Sheila",
    "Last name": "Nazario",
    "Age": 41,
    "Race": "Latina",
    "Gender": "Female",
    }


person2 = {
    "First name": "Horacio",
    "Last name": "Colon",
    "Age": 51,
    "Race": "Latino",
    "Gender": "Male",
    }


person3 = {
    "First name": "Carol",
    "Last name": "Nazario",
    "Age": 20,
    "Race": "Latina",
    "Gender": "Female",
    }

# this puts them in the list
people.append(person1)
people.append(person2)
people.append(person3)


for person in people:
    print (f'\n{person}')