

class Users:
    
    def __init__(self, first_name, last_name, age, race, gender):
        self.firstName = first_name
        self.lastName = last_name
        self.age = age 
        self.race = race
        self.gender = gender
    
    def describe_user(self):
        print (f'\nUser info: First name: {self.firstName} Last name: {self.lastName} Age: {self.age} Race: {self.race} Gender: {self.gender}')

    def greet_user(self):
        print(f'Hello, {self.firstName}.')