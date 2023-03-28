# John "Matt" Shenk
# March 8, 2023

# For this program I am modifying t_shirts.py so that the make_shirts function makes large shirts with the phrase
#   "I Love Python". I will then call the function to make a medium and large shirt with the default message, and then a
#   shirt of any size with a different message.


def make_shirt(size = 'large', text='I Love Python'):
    """Print out a message about the shirt"""
    print(f"Here is your {size} shirt with the text '{text.upper()}'.")

make_shirt('medium')
make_shirt()
make_shirt('small', 'JavaScript is cool, too!')
