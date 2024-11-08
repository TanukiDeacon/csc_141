# this program will use a txt file to print what I have learned so far in python.
import os
os.chdir("C:/Users/tanuk/OneDrive/Escritorio/csc_141/10_files_and_exceptions/")
from pathlib import Path

path = Path('what_ive_learned.txt')
contents = path.read_text()

print(contents)

lines = contents.splitlines()
message = ''

for line in lines:
    message += line.lstrip()

print(message)
