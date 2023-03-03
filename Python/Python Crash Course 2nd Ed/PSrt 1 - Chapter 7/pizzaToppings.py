# John "Matt" Shenk
# February 15, 2023

# In this program I am writing a loop that prompts the user to enter a series of pizza toppings,
#   only ending when the user enters "quit"

topping = input("Welcome! Please enter a pizza topping, or quit to cancel: ")

while topping.lower() != "quit":
    print(f"Ok, we will put {topping} on your pizza.")
    topping = input("\nPlease enter a pizza topping, or quit to cancel: ")

print("Got it! We will have your pizza ready soon enough!")
