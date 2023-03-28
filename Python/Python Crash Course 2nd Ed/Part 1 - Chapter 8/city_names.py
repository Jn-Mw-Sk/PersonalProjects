# John "Matt" Shenk
# March 8, 2023

# For this exercie I am writing a functiion called city_countrythat accepts two parameters,
#   a city name and a country name, and that returns a formatted string of the form '<city>, <country>'.
#
# I will call the function three times and use print out the return value.

def city_country(city, country):
    """Return a formatted string of the form '<city>, <country>'"""
    return f"{city.title()}, {country.title()}"

print(city_country('Philadelphia', 'United States'))
print(city_country('Ottawa', 'Canada'))
print(city_country('Paris', 'France'))
