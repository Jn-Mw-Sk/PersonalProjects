# John "Matt" Shenk
# Date: January 20, 2023

# In this program I am making a list of the first 10 cubes (cubes of numbers 1 through 10),
#   and then of course using a for loop to print those cubes

cubes = list(value**3 for value in range(1, 11))

for cube in cubes:
    print(cube)