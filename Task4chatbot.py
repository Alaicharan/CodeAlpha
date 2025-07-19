def get_reply(message):
    # Function to return chatbot response based on user input
    if message == "hello":
        return "hi"
    elif message == "How are you":
        return "I m fine"
    elif message == "Bye":
        return "Good bye"
    else:
        return "I don't understand"

def chat():
    # Main function to handle the chat loop
    while True:
        user_input = input("You: ")  # Take input from the user
        reply = get_reply(user_input)  # Get chatbot response
        print("Chatbot:", reply)  # Print chatbot response
        
        # Exit the chat if user says 'bye'
        if user_input == "bye":
            break

chat()  # Start the chatbot
