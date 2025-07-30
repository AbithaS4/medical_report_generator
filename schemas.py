from pydantic import BaseModel
from typing import Optional

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    phone: str
    city:  str
    
class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    class Config:
        orm_mode = True

class MedicalReportCreate(BaseModel):
    patient_id: int
    report_type: str
    report_data: dict  # Expecting key-value pairs like {"Hemoglobin": "14", "WBC Count": "8000"}
