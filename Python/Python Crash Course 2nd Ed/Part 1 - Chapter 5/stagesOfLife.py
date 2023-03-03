# John "Matt" Shenk
# Date: January 30, 2023

# For this program I am using an if-elif-else chain to determine a person's stage of life, using a variable for age.
#   1. If the person is less that 2 years old, print that the person is a baby
#   2. If the person is at least 2 years old but less than 4, print that the person is a toddler
#   3. If the person is at least 4 year old but less than 13, print that the person is a kid
#   4. If the person is at least 13 years old but less than 20, print that the person is a teenager
#   5. If the person is at least 20 years old but less than 65, print that the person is an adult
#   6. If the person is at age 65 or older, print that the person is an elder

age = 26

if age < 2:
    print("This person is a baby.")
elif age >= 2 and age < 4:
    print("This person is a toddler.")
elif age >= 4 and age < 13:
    print("This person is a kid.")
elif age >= 13 and age < 20:
    print("This person is a teenager.")
elif age >= 20 and age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

