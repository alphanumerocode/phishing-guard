from fastapi import APIRouter
from app.schemas.scan_schema import ScanRequest, ScanResponse
from app.services.model_service import ModelService

router = APIRouter(prefix="/scan", tags=["Scan"])
model_service = ModelService()

@router.post("/", response_model=ScanResponse)
def scan_email(request: ScanRequest):
    prediction, confidence = model_service.predict(request.email_text)
    is_phish = confidence >= 0.6  # threshold

    return {
        "is_phishing": is_phish,
        "confidence": round(confidence, 3),
        "message": "Suspicious email detected" if is_phish else "Email seems safe"
    }
