# John "Matt" Shenk
# March 27, 2023

# This program is going to work off of sending_messages.py, I am going to send a copy of the list of messages to show the original list has not been tampered with

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

# Instead of sending the original list, let's send a copy!
show_messages(messages[:], sent_messages) 

print(f"\nOriginal:\n{messages}")

print_sent_messages(sent_messages)
