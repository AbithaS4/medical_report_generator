from pydantic import BaseModel
from typing import Optional, List

# ---------------- Patients ----------------
class Patient(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    phone: str

    class Config:
        from_attributes = True  # Pydantic v2

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    phone: str  # ✅ added phone

# ---------------- Medical Reports ----------------
class MedicalReportCreate(BaseModel):
    patient_id: int
    diagnosis: str
    test_results: str
    notes: Optional[str] = None

class MedicalReportResponse(BaseModel):
    id: int
    patient_id: int
    diagnosis: str
    test_results: str
    notes: Optional[str]

    class Config:
        from_attributes = True
