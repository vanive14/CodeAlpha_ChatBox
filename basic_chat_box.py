# Basic Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "My name is SimpleBot."

    elif user_input == "what can you do":
        return "I can chat with you using predefined responses."

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


# Main program
print("================================")
print("        BASIC CHATBOT")
print("================================")
print("Type 'bye' to end the conversation.")

while True:

    user_input = input("\nYou: ")

    response = chatbot_response(user_input)

    print("Bot:", response)

    if user_input.lower() == "bye":
        break

print("\nThank you for chatting!")