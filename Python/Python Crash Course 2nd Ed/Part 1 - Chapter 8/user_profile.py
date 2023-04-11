# John "Matt" Shenk
# March 28. 2023

# In this exercise I am modifying the program user_profile.py on page 149 in the book to build a profile of myself using my first and last name and three other key-value pairs

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('John', 'Shenk', age = '26', favorite_game = 'Monster Hunter 4 Ultimate', favorite_color = 'Red')  

print(user_profile)
