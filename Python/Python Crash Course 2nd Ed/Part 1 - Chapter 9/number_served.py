# John "Matt" Shenk
# March 28, 2023

# Starting with the code from restaurants.py, I will add an attribute called number_served with a default value of 0.
# I will add 2 methods:
#   1. set_number_served(), which sets the number_served attribute to a new number.
#   2. increment_number_served, which lets one increment the number served by a certain amount.
#
# I will call each method once.

# Restaurant class
class Restaurant:
    """A simple class modeling a restaurant"""

    def __init__(self, name, cuisine):
        """Initializes name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Display a message describing the restaurant"""
        print(f"{self.name} serves {self.cuisine} cuisine.")

    def open_restaurant(self):
        """Display a message saying the restaurant is open"""
        print(f"{self.name} is open!")

    def set_number_served(self, number_served):
        """Set the number of people served at the restaurant to a specified amount"""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increment the number served by a specified amount"""
        self.number_served += number_served
        

# Code
this_restaurant = Restaurant('Red Lion', 'Pennsylvania Dutch')

print(this_restaurant.name)
print(this_restaurant.cuisine)

this_restaurant.describe_restaurant()
this_restaurant.open_restaurant()

# Print out number served (should be 0)
print(this_restaurant.number_served)

this_restaurant.set_number_served(30)
# Print out number served (should be 30 now)
print(this_restaurant.number_served)

this_restaurant.increment_number_served(8)
# Print out number served (should be 38 now)
print(this_restaurant.number_served)

