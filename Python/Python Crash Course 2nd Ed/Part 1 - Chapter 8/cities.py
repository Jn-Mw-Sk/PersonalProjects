# John "Matt" Shenk
# March 8, 2023

# For this exercise I am writing a function called describe_city(). This function accepts the name of a city and a country and prints a simple sentence about
#   the city in the country. The function MUSt have a default value. I will call the function using three cities, with one that is not in the default country.

def describe_city(city, country = 'United States'):
    """Print out a simple message about the city"""
    print(f"{city.title()} is located in {country.title()}.")

describe_city('Pittsburgh')
describe_city('Dallas')
describe_city('Sydney', 'Australia')
