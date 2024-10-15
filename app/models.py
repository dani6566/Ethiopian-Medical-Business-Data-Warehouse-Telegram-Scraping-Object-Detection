# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class MedicalBusiness(Base):
    __tablename__ = 'medical_businesses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    contact_info = Column(String)
    channel_username = Column(String)
    message = Column(String)
    date = Column(String)
    media_path = Column(String)
    
