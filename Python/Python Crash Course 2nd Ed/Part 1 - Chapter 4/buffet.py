# John "Matt" Shenk
# Date: January 24, 2023

# In this program I am thinking of 5 basic foods to include in a buffet and storing them in a tuple.
# I am then using a for loop to print each food, then attempting to write over one of the values in the tuple
# (commented out to ensure final code will run), then overwriting the entire tuple with a new one and printing those out
# (replacing two food items with new ones)

buffet_foods = ("pizza", "salad", "french fries", "chicken tenders", "breadsticks")

for food in buffet_foods:
    print(food)

# buffet_foods[0] = "cereal"

buffet_foods = ("cereal", "salad", "french fries", "chicken tenders", "grilled cheese")
print("\n")

for food in buffet_foods:
    print(food)
