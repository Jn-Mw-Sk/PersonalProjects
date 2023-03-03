# John "Matt" Shenk
# Date: January 24, 2023

# For this program I am taking a list from an earlier exercise in part 4 and
# using the slices to output the first 3, middle 3, and last 3 items
# from the list.

cubes = list(value**3 for value in range(1, 11))

for cube in cubes:
    print(cube)

print("\nThe first 3 items in this list are:\n")
for cube in cubes[:3]:
    print(cube)

print("\n3 items from the middle of this list are:\n")
for cube in cubes[3:6]:
    print(cube)

print("\nThe last 3 items in this list are:\n")
for cube in cubes[-3:]: # You can use negative indexes! How cool is that!
    print(cube)
