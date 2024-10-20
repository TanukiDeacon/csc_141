# this program will make a text based gladiator fighter
import random
import os
os.system('cls') 

print("                                      Gladiator                                      ")
print("-------------------------------------------------------------------------------------")
print("    You've become a prisoner of war! They have thrown you into the colosseum pits!   ")
print("              Now you have to choice but to fight for your survival!")
print("                                   As a gladiator!")
print("-------------------------------------------------------------------------------------")
print("")

# keeps track of how manys times you have won
victorys = 0


# Set variables
gladiators = {'Civilian': 1, 
              'Goliath': 10,
              'Soldier': 5, 
              'Lion': 9,
              'Wyvern': 12, 
              'Samurai': 7, 
              'Mercenary': 5, 
              'Barbarian': 5, 
              'Fighter': 10,
              "Rouge": 1, 
              'Pirate': 6,
              'Knight': 15,
              'Ninja': 3,
              'Basilisk': 12, 
              'Ogre': 14, 
              'Orc': 8 ,
              'Chimera': 10, 
              'Goblin': 3,
              'Quasit': 4, 
              'Cockatrice': 3, 
            }


fighter_max_damage = {'Civilian': 2, 
     		          'Goliath': 13,
                      'Soldier': 4,
                      'Lion': 8,
                       'Wyvern': 8,
                       'Samurai': 10,
                       'Mercenary': 5,
                       'Barbarian': 20,
                       'Fighter': 6,
                       "Rouge": 15,
                       'Pirate': 7,
                       'Knight': 7,
                       'Ninja': 20,
                       'Basilisk': 10,
                       'Ogre': 8,
                       'Orc': 14,
                       'Chimera': 11,
                       'Goblin': 3,
                       'Quasit': 4,
                       'Cockatrice': 5,
                      }

choice = ''
weapon_choice = ''
you_die = False
gladiators_dies = False
number_of_gladiators = len(gladiators)
gladiators_power_levels = list(gladiators.values()) 
gladiators_names = list(gladiators.keys())  
random_number = random.randint(1, number_of_gladiators)

print ("\n---------------------------------Choose your weapon-----------------------------------")
print ("\n--------------------------------------------------------------------------------------")
print("\nAxe -- Min-Damage = 0   -----  Sword -- Min-Damage = 9  ----- Lance -- Min-Damage = 5")
print("Axe -- Max-Damage = 20  -----  Sword -- Max-Damage = 10   ----- Lance -- Max-Damage = 13")
weapon_choice = input("Axe = a -- Sword = s -- Lance = l: ").lower()

if weapon_choice == "a":
    weapon_min_damage = 0
    weapon_max_damage = 20
elif weapon_choice == "s":
    weapon_min_damage = 9
    weapon_max_damage = 10
elif weapon_choice == "l":
    weapon_min_damage = 5
    weapon_max_damage = 13


# Select a random gladiator to fight
gladiator = gladiators_names[random_number]
fighter_power = gladiators_power_levels[random_number]
fighter_damage = fighter_max_damage[gladiator]
your_power_level = 30
your_min_damage = weapon_min_damage
your_max_damage = weapon_max_damage


def you_fight(fighter_power, your_power_level):
    # You strike gladiator
    damage_to_fighter = random.randint(your_min_damage, your_max_damage)
    if damage_to_fighter == 0:
        print(f'You barely miss striking the {gladiator}!')
    else:
        print(f'You strike the {gladiator}, delivering {damage_to_fighter} points of damage.')
    fighter_power = fighter_power - damage_to_fighter
    if fighter_power <= 0:
        print(f'You killed the {gladiator}!')
        number_of_gladiators = len(gladiators)
        if gladiator in gladiators:
            del gladiators[gladiator]
        your_power_level = your_power_level + 6
    return False, fighter_power, your_power_level

def gladiator_fights_you(your_power_level):
    # gladiator fights you
    damage_to_you = random.randint(0, fighter_damage)
    if damage_to_you == 0:
        print(f'The {gladiator} barely misses you!')
    else:
        print(f'The {gladiator} strikes you, delivering {damage_to_you} points of damage.')
    your_power_level = your_power_level - damage_to_you
    if your_power_level <= 0:
        print(f'You are killed.')
        return True, your_power_level
    return False, your_power_level


# print_fighter()
print(f'You find yourself in the arena with a {gladiator}, who has a power level of {fighter_power}!')
print(f"Your power level is {your_power_level}.")

# Main Game Loop
while True:
    while True == True:
       
        choice = input("Do you (e)scape, or (f)ight?: ")

        if choice == 'e':  
            print(f"You retreat.")
            number_of_gladiators = len(gladiators)
            random_number = random.randint(0, number_of_gladiators)
            gladiator = gladiators_names[random_number-1]
            fighter_power = gladiators_power_levels[random_number-1]
            fighter_damage = fighter_max_damage[gladiator]
            print(f'\nYou find yourself in the arena with a {gladiator}, who has a power level of {fighter_power}!')  
            print(f"Your power level is {your_power_level}.")        


        if choice == 'f':  
            # You fight the gladiator
            fighter_dies, fighter_power, your_power_level = you_fight(fighter_power, your_power_level) 
            if fighter_power <=0: 
                victorys = victorys + 1
                number_of_gladiators = len(gladiators)
                random_number = random.randint(1, number_of_gladiators)
                gladiator = gladiators_names[random_number]
                fighter_power = gladiators_power_levels[random_number]
                fighter_damage = fighter_max_damage[gladiator]                    
                random_number = random.randint(1, number_of_gladiators)
                print(f'\nYou find yourself in the arena with a {gladiator}, who has a power level of {fighter_power}!')  
                print(f"Your power level is {your_power_level}.")   
            
            # gladiator fights you
            you_die, your_power_level = gladiator_fights_you(your_power_level)
            if you_die == True:
                 break

            if victorys == 10:
                print ("You've won the tournament!")
                break
            
    break

# Game end
print ('\nHope you had fun!')