from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
from fastapi.responses import StreamingResponse
from .pdf_generator import generate_report_pdf
import json

router = APIRouter()

@router.post("/")
def create_report(report: schemas.MedicalReportCreate, db: Session = Depends(database.get_db)):
    db_report = models.MedicalReport(
        patient_id=report.patient_id,
        report_type=report.report_type,
        report_data=json.dumps(report.report_data)
    )
    db.add(db_report)
    db.commit()
    return {"message": "Report saved successfully"}

@router.get("/")
def get_all_reports(db: Session = Depends(database.get_db)):
    reports = db.query(models.MedicalReport).all()
    return [
        {
            "id": r.id,
            "patient": {
                "id": r.patient.id,
                "name": r.patient.name
            } if r.patient else {
                "id": None,
                "name": "Unknown"
            },
            "report_type": r.report_type,
            "report_data": json.loads(r.report_data)
        } for r in reports
    ]

@router.get("/{report_id}")
def get_report(report_id: int, db: Session = Depends(database.get_db)):
    report = db.query(models.MedicalReport).get(report_id)
    if report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return {
        "id": report.id,
        "patient": {
            "id": report.patient.id,
            "name": report.patient.name
        },
        "report_type": report.report_type,
        "report_data": json.loads(report.report_data)
    }
@router.get("/{report_id}/pdf")
def download_pdf(report_id: int, db: Session = Depends(database.get_db)):
    report = db.query(models.MedicalReport).get(report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    patient_name = report.patient.name
    report_data = json.loads(report.report_data)
    pdf_buffer = generate_report_pdf(patient_name, report.report_type, report_data)

    return StreamingResponse(pdf_buffer, media_type="application/pdf", headers={
        "Content-Disposition": f"attachment; filename=report_{report_id}.pdf"
    })