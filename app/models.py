# models.py
from sqlalchemy import Column, String, Text, TIMESTAMP
from database import Base

class MedicalBusiness(Base):
    __tablename__ = 'medical_businesses'

    id = Column(String, primary_key=True, index=True)
    channel_title = Column(String(255))
    channel_username = Column(String(255))
    message = Column(Text)
    date = Column(TIMESTAMP(timezone=True))
    media_path = Column(String(255))
