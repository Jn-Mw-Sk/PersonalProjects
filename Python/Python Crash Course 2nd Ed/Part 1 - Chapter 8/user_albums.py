# John "Matt" Shenk
# March 8, 2023

# Starting with the previous exerciese (albums.py) I am adding a while loop to ask a user to type in an artist name and an album title. Once the information is gathered
#   I am calling the function to create a dictionary then printing it. I will ensure there is a quit value for the while loop.

def make_album(artist, album, number_of_tracks = None):
    """Make a dictionary containing the artist's name, album title,
                and number of tracks(optional) and return it."""
    artist_album = {'name': artist, 'albume_title': album}

    if number_of_tracks:
        artist_album['number_of_tracks'] = number_of_tracks

    return artist_album

user_active = True
while True:
    artist = input("Please enter an artist name (or 'q' to exit): ")
    if artist == 'q':
        break

    album = input("Please enter an album title (or 'q' to exit): ")
    if album == 'q':
        break

    print(f"{make_album(artist, album)}\n")
    response = input("Would you like to put in more information? (y / n) ")

    if response == 'n':
        break

print("Have a good day!")
