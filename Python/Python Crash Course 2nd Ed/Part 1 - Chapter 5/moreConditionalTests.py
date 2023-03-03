# John "Matt" Shenk
# Date: January 25, 2023

# In thi exercise I am working oof of the exercise in conditionalTests.py and adding new tests that:
#   1. Test for equality and inequality using strings
#   2. Test using the lower() method
#   3. Test numerical values involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
#   4. Test using the 'and' keyword and 'or' keyword
#   5. Test whether an item is in a list
#   6. Test whether an item is not in a list
# Make sure there is a test that results in true and a test that results in true for each!


game = 'Monopoly'
print("\nDoes game equal Monopoly? I guess True!")
print(game == "Monopoly")

print("\nDoes game equal Catan? I guess False!")
print(game == "Catan")

game = 'Scrabble'
print('\nDoes game equal Scrabble? I guess False!')
print(game == 'Scrabble')

print("\nDoes game equal Raccoon Tycoon? I guess True!")
print(game == "Raccoon Tycoon")

game = 'Apples to Apples'
print("\nDoes game equal Apples to Apples? I guess True!")
print(game == 'Apples to Apples')

game = "Disney Villainous"
print("\nDoes game equal Checkers? I guess False!")
print (game == "Checkers")

print("\nDoes game equal Disney Villainous? I guess False!")
print(game == "Disney Villainous")

print("\nDoes game equal Disney Villainous? I guess False!")
print(game == "Disney Villainous")

game = "Epic Spell Wars of the Battle Wizards: Duel at Mt. Skullfyre"
print("\nDoes game equal Go Fish? I guess False!")
print(game == "Go Fish")

print("\nDoes game equal Solitaire? I guess True!")
print(game == "Solitaire")

##### NEW STUFF #####

# String equalities
game = "Dixit"
print("\nIs game equal to Dixit? I  guess True!")
print(game == "Dixit")

print("\nIs game not equal to Dixit? I guess False!")
print(game != "Dixit")


# Tests using lower() method
name = "Matt"
print("\nIs the name Matt? Let's find out!")
print("matt" == name.lower())

print("\nIs the name matt? Let's find out!")
print("Matt" == name.lower())

# Numerical Tests
var1 = 2
var2 = 5
var3 = 3
var4 = 3

print(f"\nThe result of different numerical tests...\n{var1 == var2}")
print(var2 != var3)
print(var1 < var3)
print(var2 > var3)
print(var3 >= var4)
print(var3 <= var2)

# 'and' and 'or'
print

