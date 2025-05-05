from fastapi import APIRouter
from schemas import MedicalReportCreate, MedicalReportResponse
from typing import List

router = APIRouter()

# Sample in-memory storage (just for testing)
fake_reports = []

@router.post("/reports", response_model=MedicalReportResponse)
def create_medical_report(report: MedicalReportCreate):
    new_report = {
        "id": len(fake_reports) + 1,
        "patient_id": report.patient_id,
        "diagnosis": report.diagnosis,
        "test_results": report.test_results,
        "notes": report.notes,
    }
    fake_reports.append(new_report)
    return new_report

@router.get("/reports", response_model=List[MedicalReportResponse])
def get_reports():
    return fake_reports
