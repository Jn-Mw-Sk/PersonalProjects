# John "Matt" Shenk
# Date: February 15, 2023

# In this program I am making a dictionary called cities, using the names of three cities as keys.
# I will then add a dictionary to each key, with the city's country, approximate population, and fact about that city.
# I will then loop through the main dictionary and print out each city's name and its information

cities = {"Pittsburgh": {"country": "United States",
                          "population": 300_421,
                          "fact": "The first Ferris Wheel was designed by a Piitsburgh native."},

           "Toronto": {"country": "Canada",
                       "population": 3_000_000,
                       "fact": "Babe Ruth hit his first professional home run in Toronto."},

           "Neverwinter": {"country": "The Forgotten Realms",
                           "population": 20_000,
                           "fact": "Neverwinter is a large city on the Sword Coast."}
           }

for city, info in cities.items():
    print(f"\n{city}\n=========")
    
    country = info['country']
    population = info['population']
    funFact = info['fact']
    
    print(f"Country: {country}")
    print(f"Approx. Population: {population}")
    print(f"Fun Fact: {funFact}") 

