# backend/scripts/train_model.py

# Step 1: Import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Step 2: Sample training data
emails = [
    "Your account has been suspended! Click here to verify.",
    "Urgent: update your payment info immediately.",
    "Hello, here is your weekly newsletter.",
    "Meeting schedule for next week."
]

labels = [1, 1, 0, 0]  # 1 = Phish, 0 = Safe

# Step 3: Convert emails to numerical features
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(emails)

# Step 4: Train a classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, labels)

# Step 5: Save the trained model and vectorizer
os.makedirs("../models", exist_ok=True)  # create folder if it doesn't exist
joblib.dump(model, "../models/phish_model.pkl")
joblib.dump(vectorizer, "../models/vectorizer.pkl")
print("Model and vectorizer saved successfully!")
