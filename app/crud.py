# crud.py
from sqlalchemy.orm import Session
from models import MedicalBusiness
from schemas import MedicalBusinessCreate

def get_medical_businesses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(MedicalBusiness).offset(skip).limit(limit).all()

def create_medical_business(db: Session, medical_business: MedicalBusinessCreate):
    db_medical_business = MedicalBusiness(**medical_business.dict())
    db.add(db_medical_business)
    db.commit()
    db.refresh(db_medical_business)
    return db_medical_business
