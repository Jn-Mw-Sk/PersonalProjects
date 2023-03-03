# John "Matt" Shenk
# Date: January 30, 2023

# For this program I am imagining an alien in a game is shot down and assigning a variable
#   called called alien_color and assigning it "red", "green", or "yellow".
#
#   I am going to use an if-elif-else chain to determine how many points the player earned, that is:
#       1. If the color is green, output that the player earned 5 points.
#       2. If the color is yellow, output that the player earned 10 points
#       3. If the color is red, output that the player earned 15 points

# This version of the program uses a green alien

alien_color = "green"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

