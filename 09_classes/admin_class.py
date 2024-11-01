# this will give admin privileges 


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

class Admin(Users):

    def __init__(self, first_name, last_name, age, race, gender, *privileges):
        super().__init__(first_name, last_name, age, race, gender)

        self.privileges = privileges

    def privilege(self):
        print("You are an admin. Your privileges include: ")
        print(self.privileges)