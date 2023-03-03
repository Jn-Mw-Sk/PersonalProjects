# John "Matt" Shenk
# January 31, 2023

# In this program I am am using the code for favorite_lngusges.py (from chapter 6)
#   and expanding on that program. I am going to make a lsit of people who should take the
#   "favorite programming languages" poll (making sure some names on the list appear on the dictionary).
# I will then loop through the list and see who has voted or not. If someone has voted, print a message saying thanks for voting. Otherwise,
#   print an invite to take part in the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

new_pollees = ['tom', 'margaret', 'jen', 'wallace', 'lucas', 'phil']

for pollee in new_pollees:
    if pollee in favorite_languages:
        print(f"Thank you {pollee.title()} for taking the poll!")
    else:
        print(f"We invite you to take the favorite programming languages poll, {pollee.title()}.")
