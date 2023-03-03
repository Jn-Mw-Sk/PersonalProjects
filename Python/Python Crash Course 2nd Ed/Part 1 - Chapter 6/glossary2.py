# John "Matt" Shenk
# January 31, 2023

# In this program I am making a glossary of sorts.
# I am going to make a list of 5 programming words from previous chapters in the book,
#   writing the term as the key and the definition as the value in the dictionary.
# I will then ouput those words and definitions in an orderly fashion.
#
# In this updated version I am cleaning up the code and looping through the list to print
#   the words and definitions. I will add five more terms when I know the loop is functioning

words = {'variable' : 'A name that can be associated with a value that one can use in a program',
         'list' : 'A collection of items in a particular order',
         'dictionary' : 'A collection of key-value pairs',
         'comment' : 'A line of code that is ignored by the interpeter that provides additional information for those reading the code',
         'string' : 'A series of characters',
         'conditional' : 'A statement that results in true or false',
         'newline' : 'A special character denoted as a backslash and an (n} to tell the print statment to add an additional line',
         'element' : 'An item in a list',
         'float' : 'A number with a decimal point',
         'constant' : 'A type of variable that stays the same throughout the life of a program.'}

for key, value in words.items():
    print(f"\n{key}: {value}")
