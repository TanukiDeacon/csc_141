# this code will make an ice cream stand

# this code will make a restaurant 

class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print(f'{self.name} serves {self.cuisine} food.')

    def open_restaurant(self):
        print(f'{self.name} is now open.')



class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine_type, flavor, flavor2):
        super().__init__(name, cuisine_type)

        self.flavor = flavor
        self.flavor2 = flavor2

    def flavors(self):
        print (f'The flavors we have are {self.flavor} and {self.flavor2}')

    
iceCreamStand = IceCreamStand('Ice Cream Emporium', 'Ice Creams', 'Chocolate', 'Vanilla')


iceCreamStand.describe_restaurant()

iceCreamStand.open_restaurant()

iceCreamStand.flavors()


