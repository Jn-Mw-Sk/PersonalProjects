# John "Matt" Shenk
# March 7, 2023

# For this program I am going to make a list called 'sandwich_orders' and filing it with the names of various sandwiches. Then I'll make an empty list called 'finished_sandwiches'.
# I will then loop through the list and print a message about each order, like 'I made your <insert name here> sandwich.'. AS I 'make' each sandwich, I will remove it from
#   the order list and place that sandwich in the finished list. I will then print out the list of finished sandwiches to ensure the list was properly formed.

sandwich_orders = ['pastrami', 'tuna', 'PB&J', 'Italian', 'pastrami', 'tuna', 'ham', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
