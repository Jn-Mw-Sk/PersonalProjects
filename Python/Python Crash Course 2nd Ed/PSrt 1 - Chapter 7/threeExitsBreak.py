# John "Matt" Shenk
# March 2, 2023

# For this program I am editing exercise 7-5 (movieTickets.py) to do each of the following at last once:
#
#   -> Use a conditional test in the while statment to stop the loop
#   -> Use an active variable to control how long the loop runs
#   -> Use a break statement to exit the loop when the user enters a quit value 
#
# This version uses a break variable
#
# User can use 'quit' to exit

age = input("Enter your age to see your price (or 'quit' to exit): ")



while True:

    if age == 'quit':
        break
    else:
        age = int(age)
        
        if age < 3:
            print("Your movie ticket is free!")
        elif age >= 3 and age < 12:
            print("Your movie ticket is $10")
        else:
            print("Your movie ticket is $15")
            
        age = input("\nEnter your age to see your price (or 'quit' to exit): ")
    

        

print("\nEnjoy the movie!")
