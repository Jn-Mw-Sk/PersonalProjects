# John "Matt" Shenk
# April 4, 2023

# In this excercise I am adding a login_attempts attribute to the class in the user class from users.py.
#
# I will also bee writing two methods:
#   1. increment_login_attempts() - Increments the value of login_attempts by 1
#   2. reset_login_attempts() - Sets the value of login_attempts to 0
#
# To demonstrate the changes, I will create an instance of the user class, call increment_login_attempts(), print the value of login_attempts, call reset_login_attempts(),
#   then print the value of login_attempts again

class User:
    """A simple class to represent a user."""
    
    def __init__(self, first_name, last_name, age, email, city):
        """Initialize user instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        """Print a message describing a user"""
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")
        print(f"{self.first_name} {self.last_name} lives in {self.city}.")
        print(f"You can contact {self.first_name} {self.last_name} at {self.email}.")

    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Set the value of login_attempts to 0"""
        self.login_attempts = 0


john = User('John', 'Shenk', 26, 'shenk2015@gmail.com', 'Lancaster')
print(john.login_attempts)
john.increment_login_attempts()
print(john.login_attempts)
john.reset_login_attempts()
print(john.login_attempts)


