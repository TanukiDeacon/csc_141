# this program will use json to store a users favorite number

import os
os.chdir("C:/Users/tanuk/OneDrive/Escritorio/csc_141/10_files_and_exceptions/")
from pathlib import Path
import json

path = Path('fav_num_10_12.json')
if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print (f'Your favorite number is {favorite_number}!')
else:
    favorite_number = input("What is your favorite number: ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print ("I'll remember your favorite number!")