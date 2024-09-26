# this program will check if the user has a unique username

current_users = ["Adam", 'Derian', 'Jack', 'Sam', 'Roger']

new_users = ["Adam", 'Jared', 'Jack', 'Janet', 'Devon']

for user in new_users:
    if user in current_users:
        print ('Sorry youu need a new user name.')
    else:
        print(f'Welcome {user}')