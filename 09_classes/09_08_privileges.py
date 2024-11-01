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

class Privilege:

    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ['Can add post', 'Can delete post', 'Can ban user']
        self.privileges = privileges

    def show_privileges(self):
        print("You are an admin. Your privileges include:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(Users):

    def __init__(self, first_name, last_name, age, race, gender):

        super().__init__(first_name, last_name, age, race, gender)
        self.privileges = Privilege()


admin = Admin("Derian", "Arroyo", "19", "Latino", "Male")

admin.describe_user()
admin.greet_user()
admin.privileges.show_privileges()
