# John "Matt" Shenk
# Date: January 19, 2023

# Starting with the code from guestList.py, I am going to modify the list, as one of the guest couldn't make it.
# I am printing the name of that person who cannot make it in a custom message.
# I am then going to replace that person's name in the list with another person, then reprint the invitations with 
# the modified list.

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