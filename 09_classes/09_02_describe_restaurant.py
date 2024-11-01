# this program will make multipke restaurants

class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f'{self.name} serves {self.cuisine} food.')

    def open_restaurant(self):
        print(f'{self.name} is now open.')


restaurant = Restaurant("Giuseppis", 'Italian')

restaurant.describe_restaurant()

restaurant2 = Restaurant("Mcdonalds", 'American')

restaurant2.describe_restaurant()

restaurant3 = Restaurant("Olive Garden", 'Italian')

restaurant3.describe_restaurant()
