# John "Matt" Shenk
# March 28, 2023

# This exrecise consists of two parts:
#   1. This program, printing_functions.py, containing the functions from the printing_models.py example to be imported
#   2. printing_models_2.py, from which this program will be imported

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

        
