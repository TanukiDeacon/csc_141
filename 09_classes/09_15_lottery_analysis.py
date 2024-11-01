# this prgram will check how hard it is to win the lottery 

from random import choices

total_pulls = 0

lottery_numbers = ('a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

winning_ticket = choices(lottery_numbers, k = 4)

print(f'Anyone who gets {winning_ticket} wins!')

my_ticket = ('7', 'a', 'b', 'a')

print (f'Your ticket is {my_ticket}.')

while winning_ticket != my_ticket:
    winning_ticket = choices(lottery_numbers, k = 4)
    print (winning_ticket)
    print ('\nIs the winning ticket')
    total_pulls += 1

print (f'It took {total_pulls} polls for you to win!')