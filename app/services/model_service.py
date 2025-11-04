import joblib
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class ModelService:
    def __init__(self):
        model_path = "backend/ml/baseline/baseline_phish_model.pkl"
        vectorizer_path = "backend/ml/baseline/tfidf_vectorizer.pkl"

        if os.path.exists(model_path) and os.path.exists(vectorizer_path):
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(vectorizer_path)
        else:
            # If model not trained yet — create dummy one
            self.vectorizer = TfidfVectorizer(stop_words='english')
            self.model = LogisticRegression()
            # Train on simple fake dataset
            X = ["Your account has been hacked", "Claim your prize now", "Meeting schedule", "Invoice attached"]
            y = [1, 1, 0, 0]
            X_vec = self.vectorizer.fit_transform(X)
            self.model.fit(X_vec, y)
            os.makedirs("backend/ml/baseline", exist_ok=True)
            joblib.dump(self.model, model_path)
            joblib.dump(self.vectorizer, vectorizer_path)

    def predict(self, email_text: str):
        vec = self.vectorizer.transform([email_text])
        prob = self.model.predict_proba(vec)[0][1]
        return (prob >= 0.5, float(prob))
