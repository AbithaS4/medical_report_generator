from sqlalchemy import Column, Integer, String
from database import Base

class MedicalReportDB(Base):
    __tablename__ = "medical_reports"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, index=True)
    diagnosis = Column(String)
    test_results = Column(String)
    notes = Column(String)

class PatientDB(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    phone = Column(String)  # ✅ added phone
