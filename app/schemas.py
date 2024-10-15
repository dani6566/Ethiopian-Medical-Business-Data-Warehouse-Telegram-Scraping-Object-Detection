# schemas.py
from pydantic import BaseModel

class MedicalBusinessBase(BaseModel):
    name: str
    address: str
    contact_info: str
    channel_username: str
    message: str
    date: str
    media_path: str

class MedicalBusinessCreate(MedicalBusinessBase):
    pass

class MedicalBusiness(MedicalBusinessBase):
    id: int

    class Config:
        orm_mode = True  # This tells Pydantic to convert SQLAlchemy models to dicts
