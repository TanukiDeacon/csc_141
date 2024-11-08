
import os
os.chdir("C:/Users/tanuk/OneDrive/Escritorio/csc_141/10_files_and_exceptions/")
from pathlib import Path
import json

path = Path('username.json')

if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print (f'Are you {username}')
    verify = input("(Y)es or (N)o: ")

    if verify.upper() == 'Y':
        print(f"Welcome back, {username}!")
    elif verify.upper() == 'N':
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
   
