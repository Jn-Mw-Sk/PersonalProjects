# John "Matt" Shenk
# January 31, 2023

# In this program I am making a list of three major rivers and their country of origin
#   and printing out a sentence for each river like "The Nile runs througjh Egypt"
# I will also be printing the name of the river and the countries individually

rivers = {'nile' : 'egypt',
          'mississippi' : 'united states',
          'thames' : 'england'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\n")

for river in rivers.keys():
    print(river)

print("\n")

for country in rivers.values():
    print(country)
