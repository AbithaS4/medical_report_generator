from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define the request model using Pydantic
class PatientDetails(BaseModel):
    name: str
    age: int
    gender: str
    symptoms: str
    diagnosis: Optional[str] = None
    treatment_plan: Optional[str] = None

# Define a POST route to generate a medical report
@app.post("/generate-report/")
async def generate_report(patient: PatientDetails):
    # Logic to generate a medical report (can be a string, dictionary, or even a file)
    report = f"""
    Medical Report for {patient.name}:
    ------------------------------
    Age: {patient.age}
    Gender: {patient.gender}
    Symptoms: {patient.symptoms}
    Diagnosis: {patient.diagnosis if patient.diagnosis else 'Pending'}
    Treatment Plan: {patient.treatment_plan if patient.treatment_plan else 'Not Defined'}
    """

    return {"report": report}

# Optional: Add a GET route for testing the API or health checks
@app.get("/")
async def root():
    return {"message": "Welcome to the Medical Report Generator API!"}