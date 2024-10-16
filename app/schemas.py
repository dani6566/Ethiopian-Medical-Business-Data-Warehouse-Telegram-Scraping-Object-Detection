# schemas.py
from pydantic import BaseModel, ConfigDict
from datetime import datetime 

class MedicalBusinessBase(BaseModel):
    channel_title: str
    channel_username: str
    message: str
    date: datetime
    media_path: str

class MedicalBusinessCreate(MedicalBusinessBase):
    pass

class MedicalBusiness(BaseModel):
    id: str
    channel_title: str
    channel_username: str
    message: str
    date: datetime
    media_path: str

    class Config:
        model_config = ConfigDict(
            from_attributes=True  # Use this for Pydantic v2+ instead of orm_mode
        )
