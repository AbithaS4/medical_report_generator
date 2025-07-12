# Medical Report Generator Backend

A FastAPI-based backend for generating and managing medical reports, including PDF export functionality.It allows submitting patient details and test data, stores it using SQLAlchemy and SQLite, and returns downloadable reports via dynamically generated PDFs using ReportLab.


## Features
- Medical report creation with JSON data storage
- Dynamic PDF report generation
- RESTful API with SQLite database (easy to switch to PostgreSQL)
- Modular and production-ready codebase
- RESTful API with CORS enabled for frontend integration

## Tech Stack

| Component       | Technology                          |
|-----------------|-------------------------------------|
| Framework       | FastAPI                             |
| Database        | SQLite (with SQLAlchemy ORM)        |
| PDF Generation  | ReportLab                           |
| API Docs        | Auto-generated Swagger/OpenAPI      |


## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/medical-report-generator.git
    cd medical-report-generator/backend
    ```

2.  Create a Virtual Environment (Optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

3.  Install Dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.Run the server:
```bash
 uvicorn main:app --reload
    ```

