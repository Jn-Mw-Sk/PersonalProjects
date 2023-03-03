# John "Matt" Shenk
# February 15, 2023

# In this program I am requesting a number from the user and printing if that number is a multiple of 10 or not.

number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is NOT a multiple of 10") 
