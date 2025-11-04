from pydantic import BaseModel

class FeedbackRequest(BaseModel):
    email_text: str
    system_flagged_as_phish: bool
    user_says_phish: bool
