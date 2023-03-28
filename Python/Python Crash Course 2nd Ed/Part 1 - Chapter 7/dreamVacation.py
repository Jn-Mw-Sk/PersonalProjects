# John "Matt" Shenk
# March 7, 2023

# For this exercise I am writing a program to poll users about their dream vacation. I will then print out the results of the poll.

responses = {}

# The flag letting us know if we should keep asking for polls
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("What is your dream vacation? ")

    responses[name] = response

    if input("\nWould you like to let another person respond? (yes/no) ") == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go to {response}.")

    
