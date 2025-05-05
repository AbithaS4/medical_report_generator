from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import PatientDB, MedicalReportDB
from schemas import PatientCreate, MedicalReportCreate, MedicalReportResponse, Patient
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi import APIRouter
from typing import List  # Import List from typing module

# Create the database tables
PatientDB.metadata.create_all(bind=engine)
MedicalReportDB.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS for your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins or specify the frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency for getting the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Router for patients
patient_router = APIRouter()

# POST route for adding a new patient
@patient_router.post("/patients", response_model=Patient)
def add_patient(patient: PatientCreate, db: Session = Depends(get_db)):  # Fixed: Added Depends
    db_patient = PatientDB(name=patient.name, age=patient.age, gender=patient.gender, phone=patient.phone)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

# GET route to fetch all patients
@patient_router.get("/patients", response_model=List[Patient])  # Fixed: Added List import
def get_patients(db: Session = Depends(get_db)):
    return db.query(PatientDB).all()

# Add the patient router to the main app
app.include_router(patient_router)
