# this program will give a different reponse depening on if they have taken the poll

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'c++',
 'phil': 'python',
 }

should_take_poll = ['edward', 'david', 'steve', 'jen']

for people in should_take_poll:
    if people not in favorite_languages.keys():
        print (people.title() + ' please take the poll!')