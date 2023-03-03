# John "Matt" Shenk
# Date: January 30, 2023

# For this program I am making a list of five or more usernames, one of which has to be 'admin'.
# I will loop through the list and print a generic greeting for each user, the exception being 'admin',
#   who gets a special greeting
#
# In this version I am adding an if statement that checks if the username list is empty, printing an appropriate message if it is.
# For this version I am also initializing an empty list to output the appropriate message


usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")
