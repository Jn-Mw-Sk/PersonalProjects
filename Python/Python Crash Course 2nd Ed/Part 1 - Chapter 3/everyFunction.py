# John "Matt" Shenk
# Date: January 20, 2023

# ALL THE FUNCTIONS!!!
# In this program I am creating a list of something (In this case, my top 5 favorite video games!)
# I am then using every function introduced in chapter 3 at least once, which are:
# append(), insert(), pop(), remove(), sort(), sorted(), len(), del

# First, let's make and print list!

favGames = ["Monster Hunter 4 Ultimate", "7 Days to Die", "DragonQuest VIII: Journey of the Cursed King",
                "Shin Megami Tensei IV", "Kingdom Hearts 368/2 Days"]

print(favGames)

print("\nLet's see how it looks sorted...\n")

print(sorted(favGames))

print("\nYeah, let's sort it!\n")

favGames.sort()
print(favGames)

print("\nLet's reverse the list for fun!\n")

favGames.reverse()
print(favGames)

print("\nHmm, let's make it 6!\n")

favGames.append("Mariokart 8 Deluxe")
print(favGames)

print("\nEh, maybe that's too much.\n")

favGames.pop()
print(favGames)

print("\nYeah you know what, let's add it in the middle\n")

favGames.insert(3, "Mariokart 8 Deluxe")
print(favGames)

print("\nAnd add another! \n")

favGames.append("Ark Survival Evolved")
print(favGames)

print("\nLet's remove Mariokart 8 Deluxe\n")

del favGames[3]
print(favGames)

print("\nMy favorite dino in Ark died, I don;t wanna think about it anymore...\n")

favGames.remove("Ark Survival Evolved")
print(favGames)

print(f"\nAt the end of all this, there are {len(favGames)} games in this list")




