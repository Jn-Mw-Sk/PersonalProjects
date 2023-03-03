# John "Matt" Shenk
# January 31, 2023

# In this program I am making a dictionary named "favorite_places", using people's names as the key
#   and the name of a place as the value. I will then loop through the dictionary and
#   print out the name of each person and the place they like.

favorite_places = {"Alena": ["In my arms", "The Simmiverse"],
                   "Jeff": ["Gamestop", "Home"],
                   "Matt": ["Comic Book Store", "Natural History Museum"]}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorites places are {places[0]} and {places[1]}.")
