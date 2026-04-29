import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
with open("intents.json", "r") as file:
    data = json.load(file)

sentences = []
labels = []
responses = {}

for intent in data["intents"]:
    tag = intent["tag"]
    responses[tag] = intent["responses"]

    for pattern in intent["patterns"]:
        sentences.append(pattern)
        labels.append(tag)

# Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sentences)

# Train model
model = LogisticRegression()
model.fit(X, labels)

def chatbot_response(user_input):
    X_input = vectorizer.transform([user_input])
    predicted_tag = model.predict(X_input)[0]

    confidence = model.predict_proba(X_input).max()

    # Lowered threshold to be more responsive to user inputs
    if confidence < 0.1:
        return "Sorry, I don't understand yet."

    # Ensure predicted tag exists in responses
    if predicted_tag not in responses:
        return "I'm still learning about that topic."

    return random.choice(responses[predicted_tag])

print("TechBot: Hello! Type 'bye' to exit.")

while True:
    message = input("You: ")

    if message.lower() in ["bye", "exit", "quit"]:
        print("TechBot: Goodbye!")
        break

    print("TechBot:", chatbot_response(message))