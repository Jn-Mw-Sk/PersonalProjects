# John "Matt" Shenk
# March 28, 2023

# This exrecise consists of two parts:
#   1. printing_functions.py, containing the functions from the printing_models.py example to be imported
#   2. This file, printing_models_2.py, from which this program will import printing_functions.py

import printing_functions as pf

unprinted_designs = ['nintendo switch case', 'airpod case', 'thingamajig']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
