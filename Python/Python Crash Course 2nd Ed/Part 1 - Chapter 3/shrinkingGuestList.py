# John "Matt" Shenk
# Date: January 19, 2023

# Unfortunatley the table is not going to arrive early enough, so I have to cut some people :(
# I am using pop() until there are only two guests
# For each popped guest I am printing a message explaining they need to be cut from the list :(
# I am then printing an invitation to the two remaining guests
# Then I'll use delete to delete the remaining guests to make the list empty,
# and then I will print the empty list to ensure it is empty at the end of the program

guests = ["Alena Olt", "Stan Lee", "Bill Nye", "Mister Rogers"]

print(f"Dear {guests[0]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[1]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[2]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[3]}, you are cordially invited to my dinner party! Signed, Matt")

print(f"\n{guests.pop(2)} cannot make it to the dinner party. :(\n")

guests.append("Robert Downey Jr.")

print(f"Dear {guests[0]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[1]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[2]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[3]}, you are cordially invited to my dinner party! Signed, Matt")

print("\nI have found a bigger table, everyone!\n")

guests.insert(0, "Markiplier")

guests.insert(2, "Nicholas Cage")

guests.append("Reggie Fils-Aime")

print(f"Dear {guests[0]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[1]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[2]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[3]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[4]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[5]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[6]}, you are cordially invited to my dinner party! Signed, Matt")

print("\nBad news guys, the table is not going to arrive in time so I only have room for two people. :(\n")

print(f"I am so sorry {guests.pop()}, but I have to cut you from the list. :(")
print(f"I am so sorry {guests.pop()}, but I have to cut you from the list. :(")
print(f"I am so sorry {guests.pop()}, but I have to cut you from the list. :(")
print(f"I am so sorry {guests.pop()}, but I have to cut you from the list. :(")
print(f"I am so sorry {guests.pop()}, but I have to cut you from the list. :(")

print(f"\nDear {guests[0]}, you are cordially invited to my dinner party! Signed, Matt")
print(f"Dear {guests[1]}, you are cordially invited to my dinner party! Signed, Matt\n")

del guests[1]
del guests[0]

print(guests)