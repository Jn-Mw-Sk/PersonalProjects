# John "Matt" Shenk
# March 27, 2023

# In this program I am writing a function that takes an arbitrary amount of sandwich ingredients and which prints out a summary of the sandwich.
# This function will be called three different times with varying amounts of arguments.
# This program explains the ability for python functions to take arbitrary amounts of arguments.

def make_sandwich(*ingredients):
    """Prints out the summary of a sandwich to be made with the ingredients passed in"""
    print("\nPreparing your sandwich with: ")
    for ingredient in ingredients:
        print(ingredient)

make_sandwich('ham', 'cheese', 'mayonnaise')
make_sandwich('turkey', 'lettuce', 'tomato', 'mayonnaise')
make_sandwich('peanut butter', 'grape jelly')
