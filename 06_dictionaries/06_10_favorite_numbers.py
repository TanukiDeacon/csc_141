# this program will print each persons favorite numbers

# This will give each person 1 favorite number

favorite_numbers = {
    'Derian' : [21, 16],
    'Carol' : [7, 777],
    'Justin' : [69, 420],
    'Sheila' : [5, 23],
    'Horacio' : [10, 3],
}

for k,v in favorite_numbers.items():
    print (f"{k}'s favorite numbers are {v[0]} and {v[1]}.")