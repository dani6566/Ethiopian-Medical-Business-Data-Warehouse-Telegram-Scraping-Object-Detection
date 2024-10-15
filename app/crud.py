# crud.py
from sqlalchemy.orm import Session
from . import models, schemas

def get_medical_businesses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.MedicalBusiness).offset(skip).limit(limit).all()

def create_medical_business(db: Session, medical_business: schemas.MedicalBusinessCreate):
    db_medical_business = models.MedicalBusiness(**medical_business.dict())
    db.add(db_medical_business)
    db.commit()
    db.refresh(db_medical_business)
    return db_medical_business
