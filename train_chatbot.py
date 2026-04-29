import json
import random

with open("intents.json", "r") as file:
    data = json.load(file)

def chatbot_response(user_input):
    user_input = user_input.lower()

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            if pattern in user_input:
                return random.choice(intent["responses"])

    return "Sorry, I don't understand yet."

print("TechBot: Hello! Type 'bye' to exit.")

while True:
    message = input("You: ")
    response = chatbot_response(message)
    print("TechBot:", response)

    if "bye" in message.lower():
        break