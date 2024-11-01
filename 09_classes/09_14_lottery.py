# this program will make a lottery ticket

from random import choices

lottery_numbers = ('a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')


winning_ticket = choices(lottery_numbers, k = 4)

print(f'Anyone who gets {winning_ticket} wins!')