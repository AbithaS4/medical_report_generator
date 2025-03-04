from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from database import SessionLocal, MedicalReportDB  #  Import from database.py
from pydantic import BaseModel, Field
from typing import List, Optional
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

router = APIRouter()

#  Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  Pydantic Model for Request
class PatientDetails(BaseModel):
    name: str
    age: int
    gender: str
    phone: str = Field(..., pattern=r'^\d{10}$')  
    symptoms: str
    diagnosis: Optional[str] = None
    treatment_plan: Optional[str] = None

# Pydantic Model for Response
class MedicalReportResponse(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    phone: str
    symptoms: str
    diagnosis: str
    treatment_plan: str

#  POST: Store Report in Database
@router.post("/generate-report/", response_model=MedicalReportResponse)
async def generate_report(patient: PatientDetails, db: Session = Depends(get_db)):
    #  Check if phone number already exists
    existing_patient = db.query(MedicalReportDB).filter(MedicalReportDB.phone == patient.phone).first()
    if existing_patient:
        raise HTTPException(status_code=400, detail="Phone number already exists")

    report = MedicalReportDB(
        name=patient.name,
        age=patient.age,
        gender=patient.gender,
        phone=patient.phone,
        symptoms=patient.symptoms,
        diagnosis=patient.diagnosis if patient.diagnosis else "Pending",
        treatment_plan=patient.treatment_plan if patient.treatment_plan else "Not Defined"
    )
    
    db.add(report)
    db.commit()
    db.refresh(report)
    return report

#  GET: Retrieve All Reports from Database
@router.get("/reports/", response_model=List[MedicalReportResponse])
async def get_reports(db: Session = Depends(get_db)):
    reports = db.query(MedicalReportDB).all()
    return reports

#  GET: Retrieve Reports by Patient ID
@router.get("/reports/{patient_id}", response_model=List[MedicalReportResponse])
async def get_reports_by_patient(patient_id: int, db: Session = Depends(get_db)):
    reports = db.query(MedicalReportDB).filter(MedicalReportDB.id == patient_id).all()
    
    if not reports:
        raise HTTPException(status_code=404, detail="No reports found for this patient")

    return reports

#  Function to Generate PDF for a Report
def generate_pdf(report):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setTitle(f"Medical Report - {report.name}")

    # Add content to the PDF
    pdf.drawString(100, 750, f"Medical Report for {report.name}")
    pdf.line(100, 745, 400, 745)
    pdf.drawString(100, 720, f"Age: {report.age}")
    pdf.drawString(100, 700, f"Gender: {report.gender}")
    pdf.drawString(100, 680, f"Phone: {report.phone}")
    pdf.drawString(100, 660, f"Symptoms: {report.symptoms}")
    pdf.drawString(100, 640, f"Diagnosis: {report.diagnosis}")
    pdf.drawString(100, 620, f"Treatment Plan: {report.treatment_plan}")

    pdf.save()
    buffer.seek(0)
    return buffer

#  API to Download PDF Report
@router.get("/reports/{report_id}/pdf")
async def get_report_pdf(report_id: int, db: Session = Depends(get_db)):
    report = db.query(MedicalReportDB).filter(MedicalReportDB.id == report_id).first()

    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    pdf_buffer = generate_pdf(report)
    headers = {
        "Content-Disposition": f"attachment; filename=report_{report_id}.pdf"
    }
    return Response(pdf_buffer.read(), media_type="application/pdf", headers=headers)
