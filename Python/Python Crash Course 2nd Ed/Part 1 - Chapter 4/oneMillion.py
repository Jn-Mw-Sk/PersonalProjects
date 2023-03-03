# John "Matt" Shenk
# Date: January 20, 2023

# In this program I am making a list of the number 1 - 1,000,000, then printing that list using a for loop
# If the program is taking too long you can Ctrl-C or close output termial to stop.

numbers = list(range(1, 1_000_001))

for number in numbers:
    print(number)