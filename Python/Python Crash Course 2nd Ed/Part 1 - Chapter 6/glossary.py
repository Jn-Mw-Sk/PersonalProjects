# John "Matt" Shenk
# January 31, 2023

# In this program I am making a glossary of sorts.
# I am going to make a list of 5 programming words from previous chapters in the book,
#   writing the term as the key and the definition as the value in the dictionary.
# I will then ouput those words and definitions in an orderly fashion.

words = {'variable' : 'A name that can be associated with a value that one can use in a program',
         'list' : 'A collection of items in a particular order',
         'dictionary' : 'A collection of key-value pairs',
         'comment' : 'A line of code that is ignored by the interpeter that provides additional information for those reading the code',
         'string' : 'A series of characters'}

print(f"Variable : {words['variable']}\n")
print(f"List : {words['list']}\n")
print(f"Dictionary : {words['dictionary']}\n")
print(f"Comment : {words['comment']}\n")
print(f"String : {words['string']}\n")
