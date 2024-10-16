# main.py
import sys
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from typing import List  # Import List for type annotations
from database import SessionLocal, engine, get_db, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

@app.post("/medical-businesses/", response_model=schemas.MedicalBusiness)
def create_medical_business(medical_business: schemas.MedicalBusinessCreate, db: Session = Depends(get_db)):
    return crud.create_medical_business(db=db, medical_business=medical_business)

@app.get("/medical-businesses/", response_model=List[schemas.MedicalBusiness])
def read_medical_businesses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    businesses = crud.get_medical_businesses(db, skip=skip, limit=limit)
    return businesses

@app.get("/medical-businesses/{channel_title}", response_model=List[schemas.MedicalBusiness])
def read_medical_businesses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    businesses = crud.get_medical_businesses(db, skip=skip, limit=limit)
    return businesses