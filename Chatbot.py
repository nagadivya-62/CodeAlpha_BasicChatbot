# Task 4: Basic Chatbot

def get_bot_response(user_input):
    """
    Returns a predefined response based on user input.
    """
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I didn't understand that. Try saying 'hello', 'how are you', or 'bye'."

def start_chat():
    """
    Starts the chatbot interaction loop.
    """
    print("Welcome to CodeAlpha Chatbot!")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("Bot:", response)
        if user_input.lower().strip() == "bye":
            break

# Start the chatbot
start_chat()
