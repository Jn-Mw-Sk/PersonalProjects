# John "Matt" Shenk
# Date: January 19, 2023

# In this exercise I am adding three more guests to the list as I have found a bigger table.
# I am: 
#   Using insert() to add a guest to the beginning of the list
#   Using insert() to add a guest to the middle of the list
#   Using append() to add a guest to the end of the list
# 
#   Once that is done I am printing a new set of invitations

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