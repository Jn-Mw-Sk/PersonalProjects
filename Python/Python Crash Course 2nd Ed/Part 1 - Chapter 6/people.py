# John "Matt" Shenk
# Date: February 13, 2023

# In this program, starting with the program from exercise 6-1 (person.py) I am making two new dictionaries representing
#   two different people. I am then putting the dictionaries in a list then looping throught the list and printing out each
#   piece of information about that person.


jeff = {'firstName': 'Jeff',
        'lastName': 'Hendricks',
        'age': 22,
        'city': 'Pine Grove'}

bex = {'firstName': 'Bex',
       'lastName': 'Shenk',
       'age': 26,
       'city': 'Pine Grove'}

alena = {'firstName': 'Alena',
         'lastName': 'Olt',
         'age': 25,
         'city': 'Millersville'}

people = [jeff, bex, alena]

for person in people:
    print(f"\nFirst Name: {person['firstName']}")
    print(f"Last Name: {person['lastName']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    
    
