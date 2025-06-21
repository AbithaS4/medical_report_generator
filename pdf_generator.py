from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def generate_report_pdf(patient_name: str, report_type: str, report_data: dict):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Medical Report")
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Patient Name: {patient_name}")
    y -= 20
    c.drawString(50, y, f"Report Type: {report_type}")
    y -= 30

    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Report Details:")
    y -= 20

    c.setFont("Helvetica", 12)
    for key, value in report_data.items():
        c.drawString(60, y, f"{key}: {value}")
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    buffer.seek(0)
    return buffer
