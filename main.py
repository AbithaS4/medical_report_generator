from fastapi import FastAPI
from . import models
from .database import engine
from .patients import router as patient_router
from .medical_rpt import router as report_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(patient_router, prefix="/patients")
app.include_router(report_router, prefix="/reports")
