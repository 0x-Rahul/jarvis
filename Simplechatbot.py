def simple_chatbot():
    print("Bot: Hi there! I'm a simple chatbot. How can I help you today?")
    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easier matching

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How are you?")
        elif "how are you" in user_input:
            print("Bot: I'm a bot, so I don't have feelings, but I'm functioning well!")
        elif "what is your name" in user_input:
            print("Bot: I don't have a name, I'm just a simple bot.")
        elif "bye" in user_input or "goodbye" in user_input:
            print("Bot: Goodbye! Have a great day!")
            break  # Exit the chat loop
        else:
            print("Bot: I'm sorry, I don't understand that. Can you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    simple_chatbot()
