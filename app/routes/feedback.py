from fastapi import APIRouter
from app.schemas.feedback_schema import FeedbackRequest
import json, os

router = APIRouter(prefix="/feedback", tags=["Feedback"])

FEEDBACK_PATH = "data/feedback/feedback_log.jsonl"

@router.post("/")
def save_feedback(request: FeedbackRequest):
    os.makedirs("data/feedback", exist_ok=True)
    feedback_entry = request.dict()
    with open(FEEDBACK_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(feedback_entry) + "\n")
    return {"message": "Feedback saved successfully"}
