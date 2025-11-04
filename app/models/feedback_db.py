from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    email_text = Column(String, nullable=False)
    system_flagged_as_phish = Column(Boolean, default=False)
    user_says_phish = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
