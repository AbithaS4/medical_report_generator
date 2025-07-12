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
5. Visit the interactive API docs at:
   Swagger UI: http://127.0.0.1:8000/docs

## Technologies Used

- FastAPI – Web API framework
- Uvicorn – ASGI server for development
- SQLAlchemy – Database ORM
- SQLite – Lightweight relational database
- ReportLab – PDF report generation
- Pydantic – Data validation using schemas
- Python 3.10+

## How It Works

1. The client (such as a frontend app) sends a POST request to /reports/ with patient details and test data.
2. The server stores this data and generates a PDF using ReportLab.

3. The generated report is sent back as a downloadable file.

## Future Enhancements

- Add user authentication (doctor login, JWT)
- Save reports to cloud storage (e.g., AWS S3)
- Add Docker support for easy deployment
- Expand to include more report types (e.g., X-ray, ECG)
- Add automated testing (e.g., using pytest)

