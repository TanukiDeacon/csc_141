from city_country import city_countrys

def test_city_country():
    santiago_chile = city_countrys('santiago', 'chile')
    assert santiago_chile == 'Santiago, Chile'