import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# Sample dataset
data = {
    "text": [
        "Your account is locked, click here to reset password",
        "Please verify your PayPal account immediately",
        "Let's schedule a meeting for tomorrow",
        "Here’s the updated project document",
        "Urgent: Update your banking information",
        "Lunch at 1 PM today?",
    ],
    "label": [1, 1, 0, 0, 1, 0],
}
df = pd.DataFrame(data)

X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2)

vectorizer = TfidfVectorizer(stop_words="english")
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_vec, y_train)

pred = model.predict(X_test_vec)
acc = accuracy_score(y_test, pred)
print(f"✅ Model trained successfully — Accuracy: {acc:.2f}")

os.makedirs("backend/ml/baseline", exist_ok=True)
joblib.dump(model, "backend/ml/baseline/baseline_phish_model.pkl")
joblib.dump(vectorizer, "backend/ml/baseline/tfidf_vectorizer.pkl")

print("✅ Model and vectorizer saved in backend/ml/baseline/")
