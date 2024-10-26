# this program will return a 3 city and country pairs

def city_country(city = 'New York City', country = 'America'):
    pair = f'{city.title()}, {country.title()}'
    return pair

place = city_country()

print (place)

place = city_country(city = 'reading')

print (place)

place = city_country(city = 'tokyo', country = 'japan')

print (place)