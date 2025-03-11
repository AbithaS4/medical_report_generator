from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORS Middleware
from database import Base, engine
import medical_rpt

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include the routes from medical_rpt.py
app.include_router(medical_rpt.router)

# Health check endpoint
@app.get("/")
def root():
    return {"message": "Medical Report API is running!"}
