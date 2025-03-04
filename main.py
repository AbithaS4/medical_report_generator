from fastapi import FastAPI
from database import Base, engine
import medical_rpt

#  Initialize FastAPI app
app = FastAPI()

#  Create database tables
Base.metadata.create_all(bind=engine)

#  Include the routes from medical_rpt.py
app.include_router(medical_rpt.router)

#  Health check endpoint
@app.get("/")
def root():
    return {"message": "Medical Report API is running!"}
