# John "Matt" Shenk
# March 28, 2023

# This file contains the functions to be imported to making_sandwiches.py

def make_sandwich(*ingredients):
    """Prints out the summary of a sandwich to be made with the ingredients passed in"""
    print("\nPreparing your sandwich with: ")
    for ingredient in ingredients:
        print(ingredient)
