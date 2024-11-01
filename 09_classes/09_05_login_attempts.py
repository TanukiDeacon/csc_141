# this program will make users

class Users:
    
    def __init__(self, first_name, last_name, age, race, gender):
        self.firstName = first_name
        self.lastName = last_name
        self.age = age 
        self.race = race
        self.gender = gender
        self.loginAttempts = 0
    
    def describe_user(self):
        print (f'\nUser info: First name: {self.firstName} Last name: {self.lastName} Age: {self.age} Race: {self.race} Gender: {self.gender}')

    def greet_user(self):
        print(f'Hello, {self.firstName}.')

    def increment_attempts(self):
        self.loginAttempts +=1
        print(f'Login Attempts: {self.loginAttempts}')

    def reset_attempts(self):
         self.loginAttempts =0
         print(f'Login Attempts: {self.loginAttempts}')


user = Users('Derian', 'Arroyo', '19', 'Latino', 'Male')

user.describe_user()
user.greet_user()

for i in range (5):
    user.increment_attempts()

user.reset_attempts()