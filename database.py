from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ Database URL (SQLite)
DATABASE_URL = "sqlite:///./medical_reports.db"

# ✅ Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# ✅ Base class for models
Base = declarative_base()

# ✅ Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Define the MedicalReport table
class MedicalReportDB(Base):
    __tablename__ = "medical_reports"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    symptoms = Column(String)
    diagnosis = Column(String, default="Pending")
    treatment_plan = Column(String, default="Not Defined")

# ✅ Step 2: Create the table inside `medical_reports.db`
Base.metadata.create_all(bind=engine)
