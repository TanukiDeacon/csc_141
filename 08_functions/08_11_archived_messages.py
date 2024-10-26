# this will use a function to print out messages

def show_messages(messages):
    for message in messages:
        print(message)

    while messages:
        sending_message = messages.pop()
        sent_messages.append(sending_message)

text_messages = ['Hi', 'Hello', 'How are you doing?', 'Good and you?', 'Good.']
sent_messages = []

show_messages(text_messages[:])

print(text_messages)
print(sent_messages)