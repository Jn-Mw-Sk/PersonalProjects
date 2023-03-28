# John "Matt" Shenk
# March 27, 2023

# In this program, I am working off of the exercies 'messages.py' and changing it so that the printed messages are removed from the original list and moved to a new list called
#   'sent_messages'. I will then print each list to make sure everything went well.
#
# This program showcases how lists can be permanently changed when passed to a function.

def show_messages(messages, sent_messages):
    """Print out each message, removing from original list and appending it to new list"""
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

def print_sent_messages(sent_messages):
    """Prints out sent messages"""
    print("\nSent messages:")
    for message in sent_messages:
        print(f"{message}")

messages = ["I like Python", "I like Dungeons and Dragons", "I like video games"]
sent_messages = []

show_messages(messages, sent_messages)

print(f"\nOriginal:\n{messages}")

print_sent_messages(sent_messages)

