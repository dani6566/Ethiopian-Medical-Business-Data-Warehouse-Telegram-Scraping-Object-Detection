# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
# from . import crud ,models, schemas
from crud import create_medical_business, get_medical_businesses
from models import MedicalBusiness
from schemas import MedicalBusinessCreate, MedicalBusiness
from database import SessionLocal, engine, get_db,Base

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

@app.post("/medical-businesses/", response_model=MedicalBusiness)
def create_medical_business(medical_business: MedicalBusinessCreate, db: Session = Depends(get_db)):
    return create_medical_business(db=db, medical_business=medical_business)

@app.get("/medical-businesses/", response_model= list)
def read_medical_businesses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    businesses = get_medical_businesses(db, skip=skip, limit=limit)
    return businesses


