from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

def generate_pdf(code, parsed, patterns, complexity, ai_feedback, score):
    """
    Generates a PDF report with all code analysis details using ReportLab.

    Returns:
        BytesIO buffer containing the PDF.
    """
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    y = height - 50
    line_height = 14

    # Title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "CodeSense AI Report")
    y -= 30
    pdf.setFont("Helvetica", 12)

    # Helper function to write multiline text and handle page breaks
    def draw_multiline_text(pdf_obj, text, x, y_pos):
        for line in str(text).splitlines():
            pdf_obj.drawString(x, y_pos, line)
            y_pos -= line_height
            if y_pos < 50:
                pdf_obj.showPage()
                pdf_obj.setFont("Helvetica", 12)
                y_pos = height - 50
        return y_pos

    # Draw each section
    y = draw_multiline_text(pdf, f"Code:\n{code}", 50, y)
    y -= line_height
    y = draw_multiline_text(pdf, f"Parsed:\n{parsed}", 50, y)
    y -= line_height
    y = draw_multiline_text(pdf, f"Patterns:\n{patterns}", 50, y)
    y -= line_height
    y = draw_multiline_text(pdf, f"Static Complexity: {complexity}", 50, y)
    y -= line_height
    y = draw_multiline_text(pdf, f"AI Feedback:\n{ai_feedback}", 50, y)
    y -= line_height
    y = draw_multiline_text(pdf, f"Overall Score: {score}", 50, y)

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer