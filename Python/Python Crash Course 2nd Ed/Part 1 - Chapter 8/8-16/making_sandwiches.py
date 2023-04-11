# John "Matt" Shenk
# March 28, 2023

# This file imports sandwich_functions.py to "make" the sandwiches, using different conventions for importing functions

import sandwich_functions
sandwich_functions.make_sandwich('ham', 'cheese', 'mayonnaise')

from sandwich_functions import make_sandwich
make_sandwich('turkey', 'lettuce', 'tomato', 'mayonnaise')

from sandwich_functions import make_sandwich as ms
ms('peanut butter', 'grape jelly')

import sandwich_functions as sf
sf.make_sandwich('tuna', 'cheese')

# As this is highly similar to thee seecond convention, comment out either-or to see results
from sandwich_functions import *
make_sandwich('peanut butter', 'pickle')
