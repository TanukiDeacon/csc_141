# this code will make a restaurant 

class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
        self.numberServed = 0

    def describe_restaurant(self):
        print(f'{self.name} serves {self.cuisine} food.')

    def open_restaurant(self):
        print(f'{self.name} is now open.')

    def set_number_served(self, number_served):
        self.numberServed = number_served
        print(f'The restaurant has served {self.numberServed} people.')

    def increment_number_served(self, served):
        self.numberServed += served
        print(f'The restaurant has served {self.numberServed} people.')




restaurant = Restaurant("Giuseppis", 'Italian')

restaurant.describe_restaurant()

restaurant.open_restaurant()

restaurant.set_number_served(12)

restaurant.increment_number_served(3)