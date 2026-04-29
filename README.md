# 🤖 Portfolio AI Chatbot Backend

A machine learning-powered chatbot API built with **Flask** and **scikit-learn**, designed to answer questions about my portfolio, skills, projects, and experience.

---

## 🚀 Features

- 🧠 ML-based intent classification (TF-IDF + Logistic Regression)
- 💬 REST API for chatbot interaction
- 🌐 CORS enabled for frontend integration (Next.js portfolio)
- ⚡ Fast and lightweight backend

---

## 🛠️ Tech Stack

- Python
- Flask
- scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Gunicorn (for deployment)

---

## 📂 Project Structure
.
├── app.py
├── intents.json
├── requirements.txt
├── Procfile
└── README.md


---

## ⚙️ Installation (Local)

```bash
git clone https://github.com/ejluv143/portfolio-ai-chatbot-backend.git
cd portfolio-ai-chatbot-backend

python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
