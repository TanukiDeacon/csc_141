# this program will make users

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


user = Users('Derian', 'Arroyo', '19', 'Latino', 'Male')

user.describe_user()
user.greet_user()

user2 = Users('Carolaine', 'Arroyo', '20', 'Latina', 'Female')

user2.describe_user()
user2.greet_user()

user3 = Users('Sheila', 'Arroyo', '41', 'Latina', 'Female')

user3.describe_user()
user3.greet_user()

user4 = Users('Horacio', 'Arroyo', '51', 'Latino', 'Male')

user4.describe_user()
user4.greet_user()