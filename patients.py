from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(database.get_db)):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/", response_model=list[schemas.Patient])
def get_patients(db: Session = Depends(database.get_db)):
    return db.query(models.Patient).all()

@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(database.get_db)):
    patient = db.query(models.Patient).get(patient_id)
    if patient:
        db.delete(patient)
        db.commit()
        return {"message": "Deleted"}
    return {"error": "Not found"}
