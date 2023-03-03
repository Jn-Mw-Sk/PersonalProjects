# John "Matt" Shenk
# Date: January 19, 2023

# In this exercise I am making a list of at least 5 places I would like to visit And performing 
#   different sort operations on that list. Original list should not be in alphabetical order to
#   show how some functions work!

places = ["Las Vegas", "Tokyo", "Ireland", "New Zealand", "Niagra Falls"]

# Print List in original order

print(places)

# Use sorted() to print out list in alphabetical order without modifying original list

print(sorted(places))

# Show list is in original order by printing it

print(places)

# Use sorted() to print list in reverse alphabetical order without modifying original list

print(sorted(places, reverse=True))

# Show list is in original order by printing it

print(places)

# Use reverse to change order of list, then print again to show changes were made

places.reverse()
print(places)

# Use reverse to change order of list, then print to show list is in original order

places.reverse()
print(places)

# Use sort() to change list to alphabetical order, then print to show changes

places.sort()
print(places)

# Use sort() to change list to reverse alphabetical order, then print to show changes

places.sort(reverse=True)
print(places)

