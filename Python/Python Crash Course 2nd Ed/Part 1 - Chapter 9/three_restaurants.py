# John "Matt" Shenk
# March 28, 2023

# In this exercise I a writing a class to represent a restaurant with two attributes: name and cuisine.
#
# In this class I will write two methods:
#   1. describe_restaurant(), which prints out information about the restaurant
#   2. open_restaurant(), which prints out a message saying the restaurant is open
#
# Working off of the code from restaurant.py, I will make three instances of the restaurant class and call the
#   describe_restaurant() method for each one

# Restaurant class
class Restaurant:
    """A simple class modeling a restaurant"""

    def __init__(self, name, cuisine):
        """Initializes name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """Display a message describing the restaurant"""
        print(f"{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        """Display a message saying the restaurant is open"""
        print(f"{self.name} is open!")

# Code
this_restaurant = Restaurant('Red Lion', 'Pennsylvania Dutch')
that_restaurant = Restaurant('Plaza Azteca' , 'Mexican')
another_restaurant = Restaurant('Olive Garden', 'Italian')

this_restaurant.describe_restaurant()
that_restaurant.describe_restaurant()
another_restaurant.describe_restaurant()
