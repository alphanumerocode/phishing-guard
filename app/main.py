from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import scan, feedback

app = FastAPI(title="PhishGuard AI", version="1.0")

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(scan.router)
app.include_router(feedback.router)

@app.get("/")
def root():
    return {"message": "Welcome to PhishGuard AI - Email Phishing Detection API"}
