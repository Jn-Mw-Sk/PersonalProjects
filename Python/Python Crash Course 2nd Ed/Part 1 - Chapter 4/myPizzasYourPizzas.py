# John "Matt" Shenk
# Date: January 24, 2023

# Starting with the program from exercies 4-1 (pizzas.py), I am making a copy of my
# list and calling it "friend_pizzas", then :
#   Adding a new pizza to the original list,
#   Adding a different new pizza to the freind_pizzas list,
#   Then outputting both to assure that the changes are made.

pizzas = ["Buffalo Chicken", "Supreme", "Pepperoni"]

for pizza in pizzas:
    print(pizza)

print("")

for pizza in pizzas:
    print(f"I like {pizza} Pizza.")

print("\nI really like pizza!")

friend_pizzas = pizzas[:]

pizzas.append("Chicken Bacon Ranch")

friend_pizzas.append("Cheese")

print("\nMy pizzas: ")

for pizza in pizzas:
    print(pizza)

print("\nMy friend's pizzas: ")
for pizza in friend_pizzas:
    print(pizza)
