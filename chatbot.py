def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! I am your AI chatbot. How can I help you?"

    elif "name" in user_input:
        return "My name is TechBot."

    elif "skills" in user_input:
        return "I can help answer questions about Python, machine learning, and your portfolio."

    elif "bye" in user_input:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand yet. I am still learning."


print("TechBot: Hello! Type 'bye' to exit.")

while True:
    user_message = input("You: ")

    response = chatbot_response(user_message)
    print("TechBot:", response)

    if "bye" in user_message.lower():
        break