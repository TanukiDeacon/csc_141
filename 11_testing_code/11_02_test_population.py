from population import city_country

def test_city_country():
   
    santiago_chile = city_country('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'

def test_city_country_population():
    santiago_chile = city_country('santiago', 'chile', population=5_000_000)
    assert santiago_chile == 'Santiago, Chile - population 5000000'