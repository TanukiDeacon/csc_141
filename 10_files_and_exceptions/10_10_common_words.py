# this program will use count() to check how many times 'the' appears in Frankinstein

import os
os.chdir("C:/Users/tanuk/OneDrive/Escritorio/csc_141/10_files_and_exceptions/")
from pathlib import Path

path = Path('frankenstein.txt')

contents = path.read_text()

lines = contents.splitlines()

print(lines.count('the '))