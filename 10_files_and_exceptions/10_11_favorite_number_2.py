import os
os.chdir("C:/Users/tanuk/OneDrive/Escritorio/csc_141/10_files_and_exceptions/")
from pathlib import Path
import json

path = Path('fav_num.json')

contents = path.read_text()
favorite_number = json.loads(contents)
print (f'Your favorite number is {favorite_number}!')