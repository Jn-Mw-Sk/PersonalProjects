# John "Matt" Shenk
# Date: January 14, 2023

# Uses a variable to represent a person's name, including some white space on both sides,
# making sure to use the character combos "\n" and "\t" at least once.
# Displays the name to show white space, the displaying using the three
# stripping functons lstrip(), rstrip(), and strip()

# Adding a line charcter to the right to show that the stripping functions work
name = "\tNicola Tesla\t"
print("Regular Name: \n" + name + 
    "|\nName with lstrip(): \n" + 
    name.lstrip() + "|\nName with rstrip(): \n" + 
    name.rstrip() + "|\nName with strip(): \n" + 
    name.strip() + "|")