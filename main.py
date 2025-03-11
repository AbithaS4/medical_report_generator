from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
import medical_rpt

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ Enable CORS for the local frontend (Next.js on port 3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ✅ Allow frontend requests from Next.js
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # ✅ Allow all headers
)

# ✅ Create database tables
Base.metadata.create_all(bind=engine)

# ✅ Include the routes from medical_rpt.py
app.include_router(medical_rpt.router)

# ✅ Health check endpoint
@app.get("/")
def root():
    return {"message": "Medical Report API is running!"}
