from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models

# Import routers
from .patients import router as patient_router
from .medical_rpt import router as report_router

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend address
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(patient_router, prefix="/patients", tags=["patients"])
app.include_router(report_router, prefix="/reports", tags=["reports"])