# John "Matt" Shenk
# February 15, 2023

# For this program I am modifying Exercise 6-1 (favoriteNumber.py) and allowing each perosn to have more than one
#   favorite number. I will then loop through and print each person's name along with their favorite number


personNumbers = {'Matt': [7_000_000_000_000, 94, 4],
                 'Mista': ['anything but 4'],
                 'Alena': [100, 10, 5],
                 'George': [642_637, 549_870, 3, 7],
                 'Ash': [25]}
for person, numbers in personNumbers.items():
    print(f"\n{person.title()}'s favorite number(s) are:")
    for number in numbers:
        print(f"\t{number}")
