# John "Matt" Shenk
# March 7, 2023

# Working off of the program from 'deli.py', I am going to remove 'pastrami' from the list of sandiwches, as the shop has run out of pastrami.
# I am going to ensure that 'pastrami' does not appear in the list.

sandwich_orders = ['pastrami', 'tuna', 'PB&J', 'Italian', 'pastrami', 'tuna', 'ham', 'pastrami']
finished_sandwiches = []

print("We have run out of pastrami :(\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
