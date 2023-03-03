# John "Matt" Shenk
# Date: January 30, 2023

# For this program I am making an example of how websites ensure users have unique usernames:
#   - Making a list of five or more usernames, calling it current_users.
#   - Making a list of five usernames called new_users, making sure on or two entries in current_users exist
#       in this new list
#   - Loop through new_users to see if each username has already been used. If it has, print a message saying
#       the user should change their username. Otherwise, print a message saying the username is available
#   - Make sure comaprisons are case insensitive (JOHN  == john)

current_users = ['MattTheGeek', 'Alena', 'SullyTheCat', 'TonyStark', 'Gengar', 'Rekt']

new_users = ['IchabobMuttonhead', 'ALENA', 'SoraTheKeybladeWielder', 'GeNgaR', 'TyrantLucifer']

current_users2 = []

for username in current_users:
    current_users2.append(username.lower())

for username in new_users:
    if username.lower() in current_users2:
        print("Username already exists. Choose a new username.")
    else:
        print(f"The username {username} is available!")
        
