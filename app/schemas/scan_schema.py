from pydantic import BaseModel

class ScanRequest(BaseModel):
    email_text: str

class ScanResponse(BaseModel):
    is_phishing: bool
    confidence: float
    message: str
