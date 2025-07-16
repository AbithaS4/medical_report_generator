from fastapi import FastAPI
from medical_report_generator import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

from .patients import router as patient_router
from .medical_rpt import router as report_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend address
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(patient_router, prefix="/patients")
app.include_router(report_router, prefix="/reports")