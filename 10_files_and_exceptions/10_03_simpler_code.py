'''from pathlib import Path



path = Path('pi_digits.txt')


contents = path.read_text()
pi_string = ''

for line in contents.splitlines():   i changed this from lines to contents.splitlines()
    pi_string += line


print(pi_string)
print(len(pi_string))'''