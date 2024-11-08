# this program will use try except to make sure all files excest before running

import os
os.chdir("C:/Users/tanuk/OneDrive/Escritorio/csc_141/10_files_and_exceptions/")
from pathlib import Path

path_dog = Path('dog.txt')
path_cat = Path('ca.txt')

try:
    contents_dog = path_dog.read_text()
    contents_cat = path_cat.read_text()
except FileNotFoundError:
    print ("Sorry but one of the files couldn't be found!")
else:

    lines_d = contents_dog.splitlines()
    lines_c = contents_cat.splitlines()

    dogs = ''
    cats = ''

    for line_d in lines_d:
        dogs += line_d.lstrip()

    for line_c in lines_c:
        cats += line_c.lstrip()

    print(dogs)
    print(cats)

