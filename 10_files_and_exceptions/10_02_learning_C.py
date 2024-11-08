# this program will import a text file then use replece to replace 'python' with 'C++'

import os
os.chdir("C:/Users/tanuk/OneDrive/Escritorio/csc_141/10_files_and_exceptions/")
from pathlib import Path

path = Path('what_ive_learned.txt')
contents = path.read_text()
contents = contents.replace('python', 'C++')

print(contents)