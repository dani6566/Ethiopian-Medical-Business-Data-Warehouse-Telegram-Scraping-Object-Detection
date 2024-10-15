from pydantic import BaseModel, ConfigDict

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
        model_config = ConfigDict(
            from_attributes=True  # Use this instead of orm_mode for Pydantic v2+
        )
