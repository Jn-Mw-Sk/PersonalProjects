# John "Matt" Shenk
# March 7, 2023

# For this [program I am wiritng a function to accept a size and text that should be on the shirt and should print a sentence summarizing the size of the shirt and message on it.
#
# I will call this function twice, one time using positional arguments and a second time using keyword arguments

def make_shirt(size, text):
    """Print out a message about the shirt"""
    print(f"Here is your {size} shirt with the text '{text.upper()}'t_shirt.py")

make_shirt('extra large', 'I love Python')
make_shirt(size='small', text='I like video games')
