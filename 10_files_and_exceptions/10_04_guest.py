# this program will use write text to put text into a txt file

import os
os.chdir("C:/Users/tanuk/OneDrive/Escritorio/csc_141/10_files_and_exceptions/")
from pathlib import Path

path = Path('guest.txt')

guest = input("What is your name: ")

path.write_text(guest.title())

print('You have been added to the guest list.')