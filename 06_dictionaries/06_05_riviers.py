# this code will print rivers and the countrys they belong too

rivers = {'The Nile' : 'Egypt',
          'The Amazon' : "South America",
          'The Missisipi' : 'North America'
          }

for river, country in rivers.items():
    print ('\n' + river + ' runs through ' + country)

for river in rivers.keys():
    print('\n' + river)

for country in rivers.values():
    print ('\n' + country)