# Medical Report Generator Backend

A **FastAPI**-based backend for generating and managing medical reports, including PDF export functionality.It allows submitting patient and test data, stores it using SQLAlchemy and SQLite, and returns downloadable reports via dynamically generated PDFs using ReportLab.


## Features
-  Medical report creation with JSON data storage
-  Dynamic PDF report generation
-  RESTful API with SQLite database (easy to switch to PostgreSQL)
-  RESTful API with CORS enabled for frontend integration

## Tech Stack

| Component      | Tech             |
|----------------|----------------- |
| Framework      | FastAPI          |
| ORM            | SQLAlchemy       |
| PDF Generator  | ReportLab        |
| Database       | SQLite           |
| Docs UI        | Swagger / Redoc  |


# Installation

1.  Clone the repository:
```bash
    git clone https://github.com/yourusername/medical-report-generator.git
    cd medical-report-generator/backend
```

2.  Create a Virtual Environment (Optional)
```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
```  

3.  Install Dependencies
```bash
   pip install -r requirements.txt
```


4.  Run the development server:
```bash
  uvicorn main:app --reload
```
