# this program will use write text to put text into a txt file

import os
os.chdir("C:/Users/tanuk/OneDrive/Escritorio/csc_141/10_files_and_exceptions/")
from pathlib import Path

path = Path('guest.txt')

guests = ''

promt = ("What is your name: ")
print('Enetr quit to end at any time.')
while True:
    guest = input(promt.title())
    guests += (f'{guest}\n')

    if guest == 'quit':
        break

path.write_text(guests)

print('You have been added to the guest list.')