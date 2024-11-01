# this program will make a dice

from random import randint


class Dice:

    def __init__(self, first_side , max_sides):
        self.fixed = first_side
        self.sides = max_sides

    def roll_die(self):
        rolled_number = randint(self.fixed, self.sides)
        print (f'You rolled a {rolled_number}!')

print("This is for 6 sided die.")
six_sided_die = Dice(1, 6)
for i in range(10):
    six_sided_die.roll_die()

print("\nThis is for 10 sided die.")
ten_sided_die = Dice(1,10)
for i in range(10):
    ten_sided_die.roll_die()

print("\nThis is for 20 sided die.")
twenty_sided_die = Dice(1,20)
for i in range(10):
    six_sided_die.roll_die()