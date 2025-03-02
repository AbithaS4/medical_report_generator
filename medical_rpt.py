from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, MedicalReportDB
from pydantic import BaseModel
from typing import List, Optional
from fastapi import HTTPException



router = APIRouter()

# ✅ Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Pydantic Model for Request
class PatientDetails(BaseModel):
    name: str
    age: int
    gender: str
    symptoms: str
    diagnosis: Optional[str] = None
    treatment_plan: Optional[str] = None

# ✅ Pydantic Model for Response
class MedicalReportResponse(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    symptoms: str
    diagnosis: str
    treatment_plan: str

# ✅ POST: Store Report in Database
@router.post("/generate-report/", response_model=MedicalReportResponse)
async def generate_report(patient: PatientDetails, db: Session = Depends(get_db)):
    report = MedicalReportDB(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        symptoms=patient.symptoms,
        diagnosis=patient.diagnosis if patient.diagnosis else "Pending",
        treatment_plan=patient.treatment_plan if patient.treatment_plan else "Not Defined"
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

# ✅ GET: Retrieve All Reports from Database
@router.get("/reports/", response_model=List[MedicalReportResponse])
async def get_reports(db: Session = Depends(get_db)):
    reports = db.query(MedicalReportDB).all()
    return reports

'''

@router.delete("/delete-report/{report_id}")
async def delete_report(report_id: int, db: Session = Depends(get_db)):
    report = db.query(MedicalReportDB).filter(MedicalReportDB.id == report_id).first()
    
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    db.delete(report)
    db.commit()
    return {"message": f"Report with ID {report_id} deleted successfully"}
'''
