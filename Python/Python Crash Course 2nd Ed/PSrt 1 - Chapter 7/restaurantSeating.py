# John "Matt" Shenk
# February 15, 2023

# In this exercise I am writing a program requesting a number of dinner guests from the user.
# If the number is more than eight, print that they will have to wait. Otherwise, inform the user their table is ready.

guests = input("How many guests do you have for us this evening? ")
guests = int(guests)

if guests > 8:
    print("You will have to hang tight and wait for a table")
else:
    print("Perfect! Your table is ready.")
