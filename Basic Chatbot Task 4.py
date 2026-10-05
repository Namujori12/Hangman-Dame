# Task 4: Basic Chatbot

print("===== BASIC CHATBOT =====")
print("Hello! I am a simple chatbot.")
print("Type 'bye' to end the conversation.")

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "hello":
        print("Bot: Hi!")

    elif user_input == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")