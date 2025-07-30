from fastapi import APIRouter, Depends, HTTPException, status
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
    patients = db.query(models.Patient).all()
    if not patients:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No patients found in database"
        )
    return patients

@router.get("/{patient_id}", response_model=schemas.Patient)
def get_patient(patient_id: int, db: Session = Depends(database.get_db)):
    patient = db.query(models.Patient).get(patient_id)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with id {patient_id} not found"
        )
    return patient

@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(database.get_db)):
    patient = db.query(models.Patient).get(patient_id)
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with id {patient_id} not found"
        )
    db.delete(patient)
    db.commit()
    return {"message": f"Patient with id {patient_id} deleted successfully"}