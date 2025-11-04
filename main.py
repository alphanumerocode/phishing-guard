from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

app = FastAPI(title="PhishGuard AI", version="1.0")

# -----------------------------
# Enable CORS for frontend
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for local dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# 1. Train or load simple model
# -----------------------------
MODEL_FILE = "phishguard_model.joblib"

if not os.path.exists(MODEL_FILE):
    emails = [
        "Claim your free reward now!",
        "Update your password immediately",
        "Your invoice for the recent purchase",
        "Meeting scheduled for tomorrow",
        "Click here to win an iPhone",
        "Your bank account has been locked",
        "Let’s catch up for lunch today",
    ]
    labels = [1, 1, 0, 0, 1, 1, 0]  # 1 = phishing, 0 = safe

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(emails)
    model = MultinomialNB()
    model.fit(X, labels)

    joblib.dump((vectorizer, model), MODEL_FILE)
else:
    vectorizer, model = joblib.load(MODEL_FILE)

# -----------------------------
# 2. Data Models
# -----------------------------
class ScanRequest(BaseModel):
    email: str

class FeedbackRequest(BaseModel):
    email_text: str
    system_flagged_as_phish: bool
    user_says_phish: bool

# -----------------------------
# 3. API Endpoints
# -----------------------------
@app.get("/")
def read_root():
    return {"message": "Welcome to PhishGuard AI - Email Phishing Detection API"}

@app.post("/scan/")
def scan_email(request: ScanRequest):
    """Classify email as phishing or safe."""
    X_new = vectorizer.transform([request.email])
    prediction = model.predict(X_new)[0]
    prob = model.predict_proba(X_new)[0][prediction]

    is_phishing = bool(prediction)
    message = "Phishing detected" if is_phishing else "Safe email"

    return {
        "message": message,
        "is_phishing": is_phishing,
        "confidence": round(float(prob), 2),
    }

@app.post("/feedback/")
def feedback(request: FeedbackRequest):
    """Handle user feedback."""
    print("📝 Feedback received:")
    print(f"Email: {request.email_text}")
    print(f"System flagged as phishing: {request.system_flagged_as_phish}")
    print(f"User says phishing: {request.user_says_phish}")
    return {"message": "Feedback recorded successfully"}

# -----------------------------
# Run: uvicorn main:app --reload
# -----------------------------
