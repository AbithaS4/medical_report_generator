from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

#  Database URL (SQLite)
DATABASE_URL = "sqlite:///./medical_reports.db"

#  Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#  Base class for models
Base = declarative_base()

#  Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#  Database URL (SQLite)
DATABASE_URL = "sqlite:///./medical_reports.db"

#  Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#  Base class for models
Base = declarative_base()

#  Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#  Define the MedicalReport table
class MedicalReportDB(Base):
    __tablename__ = "medical_reports"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    phone = Column(String, unique=True, nullable=False)  #  Ensures unique phone numbers
    symptoms = Column(String)
    diagnosis = Column(String, default="Pending")
    treatment_plan = Column(String, default="Not Defined")

#  Create the table inside `medical_reports.db`
Base.metadata.create_all(bind=engine)

class MedicalReportDB(Base):
    __tablename__ = "medical_reports"
    __table_args__ = {"extend_existing": True}  #  Add this line to avoid duplicate table issue


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    phone = Column(String, unique=True, nullable=False)  #  Ensures unique phone numbers
    symptoms = Column(String)
    diagnosis = Column(String, default="Pending")
    treatment_plan = Column(String, default="Not Defined")

# Create the table inside `medical_reports.db`
Base.metadata.create_all(bind=engine)
