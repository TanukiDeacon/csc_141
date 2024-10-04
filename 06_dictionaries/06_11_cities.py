# this will give info about cities

cities = {
    'New York' :
    {'Country' : 'America',
     'Population' : '8.80 mil',
     'Fact' : 'Set train tracks on fire to get rid of ice'
     },

    'Reading' :
    {'Country' : 'America',
     'Population' : '95k',
     'Fact' : 'Was known for its 3Bs during the idustrial revolution : Beer, Bricks, and biscuits'
     },

    'Las Vegas' :
    {'Country' : 'America',
     'Population' : '641k',
     'Fact' : 'The famous "Las Vegas Strip" is NOT located in Las Vegas. It is actually in Clark County.'
     }
}

for city, info in cities.items():
    print (f'\nSome facts about {city} are {info} ')