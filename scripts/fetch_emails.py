import os
from pathlib import Path
import email
from email import policy
import joblib

# Load your model and vectorizer
model = joblib.load("models/phish_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Folder with .eml files
raw_folder = Path("data/raw")

def extract_email_content(file_path):
    with open(file_path, "rb") as f:
        msg = email.message_from_binary_file(f, policy=policy.default)
    
    # Get plain text or fallback to HTML
    content = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                content += part.get_content()
            elif part.get_content_type() == "text/html" and not content:
                content += part.get_content()
    else:
        content = msg.get_content()
    return content

# Scan emails
for file in raw_folder.glob("*.eml"):
    text = extract_email_content(file)
    X = vectorizer.transform([text])
    prob_phish = model.predict_proba(X)[0][1]  # index 1 = Phish
    label = "Phish" if prob_phish >= 0.5 else "Safe"

    print(f"📧 File: {file.name}")
    print(f"🧠 Predicted: {label}")
    print(f"📊 Phishing probability: {prob_phish:.2f}\n")
