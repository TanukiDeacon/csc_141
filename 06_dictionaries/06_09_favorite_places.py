# this will print peoples favorite places

favorite_places = {
    'Derian' : ['Netherlands', 'Japan'],
    'Justin' : ['America', 'Scotland'],
    'Carol' : ['South Korea', 'Iceland']
}

for k,v in favorite_places.items():
    print (f"\n{k.title()}'s favorite places are {v[0]} and {v[1]}.")