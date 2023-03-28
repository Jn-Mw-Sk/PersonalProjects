# John "Matt" Shenk
# March 8, 2023

# For this exercise I am writing a function called make_album() that builds a dictionary dexcribing a music album.
# The function should take in an artists name and an album title, and should retunr a dictionary containing that information.
# I will call the function three times to make three dictionaries, and print out each dictionary to ensure correctness.
# I will add a default value to a paramter to accept a number of tracks on the album, making at least one additional function call
#   using this new parameter

def make_album(artist, album, number_of_tracks = None):
    """Make a dictionary containing the artist's name, album title,
                and number of tracks(optional) and return it."""
    artist_album = {'name': artist, 'albume_title': album}

    if number_of_tracks:
        artist_album['number_of_tracks'] = number_of_tracks

    return artist_album

print(make_album('Disturbed', 'Indestructible'))
print(make_album('Metallica', 'Metallica'))
print(make_album('Mono Inc.', 'The Book Of Fire'))

# Print out new albums using optional parameter
print(make_album('Tungsten', 'We Will Rise', 12))
print(make_album('Xandria', "Neverworld's End", 14))
    
