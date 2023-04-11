# John "Matt" Shenk
# March 28, 2023

# In this exercise, I will creae a user() class that contains a first name, last name, and a couple other attributes
#   (age, email, city).
#
# This class will contain two methods:
#   1. describe_user(), which prints a message describing the user
#   2. greet_user(), which prints a custom message for the user
#
# I will make several instances of this class and call both methods for each.

class User:
    """A simple class to represent a user."""
    
    def __init__(self, first_name, last_name, age, email, city):
        """Initialize user instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city

    def describe_user(self):
        """Print a message describing a user"""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"{self.first_name} {self.last_name} lives in {self.city}.")
        print(f"You can contact {self.first_name} {self.last_name} at {self.email}.")

    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print(f"Hello, {self.first_name} {self.last_name}!")

john = User('John', 'Shenk', 26, 'shenk2015@gmail.com', 'Lancaster')
bob = User('Bob', 'Personson', 54, 'bob1234@example.com', 'New York City')
jane = User('Jane', 'Doe', 32, 'janeDoe@somewhere.com', 'Sydney')

john.describe_user()
john.greet_user()

bob.describe_user()
bob.greet_user()

jane.describe_user()
jane.greet_user()
