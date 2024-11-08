# thsi program will use json to store info about a user

import os
os.chdir("C:/Users/tanuk/OneDrive/Escritorio/csc_141/10_files_and_exceptions/")
from pathlib import Path
import json

path = Path('user.json')
if path.exists():
    contents = path.read_text()
    user = json.loads(contents)
    print(f"Welcome back, {user}")
else:
    username = input("What is your name: ")
    age = input("What is you age:")
    gender = input ("What is your gender: ")
    user = username
    user += (f'\nYou are {age}.')
    user += (f'\nYou are a {gender}.')
    contents = json.dumps(user)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")