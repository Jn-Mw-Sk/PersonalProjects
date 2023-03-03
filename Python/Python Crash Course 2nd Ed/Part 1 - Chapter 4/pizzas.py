# John "Matt" Shenk
# Date: January 20, 2023

# For this program I am making a list of three different types of pizzas I like, then:
#   1. Print each pizza's name using a for loop
#   2. Like above, but instead using that pizza's name in a sentence like "I like <insert pizza name here> Pizza"
#   3. Output a sentence at the end that says "I really like pizza!"

pizzas = ["Buffalo Chicken", "Supreme", "Pepperoni"]

for pizza in pizzas:
    print(pizza)

print("")

for pizza in pizzas:
    print(f"I like {pizza} Pizza.")

print("\nI really like pizza!")

