# John "Matt" Shenk
# Date: January 20, 2023

# For this program I am making a list of three animals that share a common characteritic, then:
#   1. Printing out the name of each animal
#   2. Printing a statement for each animal that share that characterists, such as "A dog would make a great pet"
#   3. Printing a statement at the end of the program stating what the common characteristic between the animals is

animals = ["eagle", "dragonfly", "vampire Bat"]

for animal in animals:
    print(animal)

print("")

for animal in animals:
    print(f"The {animal} has wings.")

print("\nAll of these animals have wings.")