#  Medical Report Generator (FastAPI Backend)

A backend application built with **FastAPI** for generating medical reports.

---

##  Installation

Install the required packages:

```bash
pip install fastapi uvicorn
pip install sqlalchemy
pip install reportlab
```

## Getting Started

To run the backend use;
```bash
uvicorn medical_report_generator.main:app --reload 
uvicorn main:app --reload
```
Then open your browser at:

[http://localhost:8000/docs]