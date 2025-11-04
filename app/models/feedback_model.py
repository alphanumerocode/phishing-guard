from pydantic import BaseModel
from datetime import datetime

class FeedbackModel(BaseModel):
    email_text: str
    system_flagged_as_phish: bool
    user_says_phish: bool
    timestamp: datetime = datetime.utcnow()
