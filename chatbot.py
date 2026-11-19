#  RULE-BASED CHATBOT

print("=" * 45)
print("       WELCOME TO CODEORBIT CHATBOT")
print("=" * 45)

print("Hello! I am your Python chatbot.")
print("You can ask me questions.")
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.")

def chatbot_response(user_input):

    # Convert input to lowercase
    user_input = user_input.lower().strip()

    # Greeting responses
    if user_input in ["hello", "hi", "hey", "good morning"]:
        return "Hello! How can I help you today?"

    # How are you
    elif "how are you" in user_input:
        return "I am doing great! Thank you for asking."

    # Chatbot name
    elif "your name" in user_input:
        return "My name is CodeOrbit Chatbot."

    # Python information
    elif "python" in user_input:
        return "Python is a popular and beginner-friendly programming language."

    # Artificial intelligence
    elif "artificial intelligence" in user_input or " ai " in " " + user_input + " ":
        return "Artificial Intelligence allows computers to perform intelligent tasks."

    # Internship information
    elif "internship" in user_input:
        return "This is my Rule-Based Chatbot project for CodeOrbit Tech."

    # Help command
    elif user_input == "help":
        return """
Available commands:
1. Hello
2. How are you?
3. What is your name?
4. Tell me about Python
5. What is Artificial Intelligence?
6. Tell me about internship
7. Bye
"""

    # Thank you
    elif "thank" in user_input:
        return "You're welcome! Happy to help."

    # Goodbye
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a wonderful day."

    # Unknown input
    else:
        return "Sorry, I don't understand that. Please try another question."



while True:

    user = input("\nYou: ")

    # Get chatbot response
    response = chatbot_response(user)

    print("Bot:", response)

    # Stop chatbot when user says bye
    if user.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
        break

print("\nChatbot session ended.")
