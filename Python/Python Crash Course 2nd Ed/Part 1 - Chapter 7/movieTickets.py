# John "Matt" Shenk
# February 15, 2023

# For this program I am writing a loop that asks the user for their age and tells that user how much their movie ticket will be.
#
# Prices are as follows:
#   - under age of 3 ---> free
#   - between 3 and 12 -> $10
#   - over 12 ----------> $15
#
# User can use 'quit' to exit

age = input("Enter your age to see your price (or 'quit' to exit): ")

while age.lower() != 'quit':
    age = int(age)
    
    if age < 3:
        print("Your movie ticket is free!")
    elif age >= 3 and age < 12:
        print("Your movie ticket is $10")
    else:
        print("Your movie ticket is $15")

    age = input("\nEnter your age to see your price (or 'quit' to exit): ")

print("\nEnjoy the movie!")
