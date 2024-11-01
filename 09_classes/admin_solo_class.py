

from user_solo_class import *

class Admin(Users):

    def __init__(self, first_name, last_name, age, race, gender, *privileges):
        super().__init__(first_name, last_name, age, race, gender)

        self.privileges = privileges

    def privilege(self):
        print("You are an admin. Your privileges include: ")
        print(self.privileges)