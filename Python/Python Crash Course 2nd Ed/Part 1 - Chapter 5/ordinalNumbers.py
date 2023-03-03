# John "Matt" Shenk
# Date: January 31, 2023

# In this program I am going to output a list of ordinal numbers from 1 through 9
# (An ordinal numbber indicates its position in a list, such as 1st and 2nd.
#   Most ordinal numbers in in th, excepts 1, 2, and 3)
#
#   I will loop through the list and use an if-elif-else chain to properly print each entry

ordinalNumbers = list(range(1, 10))

for number in ordinalNumbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
