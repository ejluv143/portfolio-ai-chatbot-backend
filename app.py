from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os

app = Flask(__name__)
CORS(app)

# Home route for browser testing
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask chatbot backend is running."})

# Load intents
with open("intents.json", "r", encoding="utf-8") as file:
    data = json.load(file)

sentences = []
labels = []
responses = {}

for intent in data["intents"]:
    tag = intent["tag"]
    responses[tag] = intent["responses"]

    for pattern in intent["patterns"]:
        sentences.append(pattern.lower())
        labels.append(tag)

# Train model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sentences)

model = LogisticRegression(max_iter=1000)
model.fit(X, labels)

@app.route("/chat", methods=["POST"])
def chat():
    body = request.get_json()

    if not body or "message" not in body:
        return jsonify({"response": "Please send a message."}), 400

    user_input = body["message"].lower().strip()

    if user_input == "":
        return jsonify({"response": "Please type something."})

    X_input = vectorizer.transform([user_input])
    predicted_tag = model.predict(X_input)[0]
    confidence = model.predict_proba(X_input).max()

    print("User:", user_input)
    print("Predicted:", predicted_tag)
    print("Confidence:", confidence)

    if confidence < 0.15:
        return jsonify({"response": "Sorry, I don't understand yet."})

    return jsonify({
        "response": random.choice(responses[predicted_tag]),
        "intent": predicted_tag,
        "confidence": round(float(confidence), 2)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)