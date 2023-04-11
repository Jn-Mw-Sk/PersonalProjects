# John "Matt" Shenk
# March 28, 2023

# In this exercise I will be writing a function that stores information about a car, always receiving a make and model and an arbitrary amount of key-value pair arguments.
# I will call the function with a make, model, and two other name-value pairs to construct a dictionary then print it.

def make_car(make, model, **car_info):
    """Add the make and model to the car_info dictionary and return that dictionary"""
    car_info['make'] = make
    car_info['model'] = model
    return car_info

car_info = make_car('ford', 'tempo', color = 'light blue', year = 1992)

print(car_info)
