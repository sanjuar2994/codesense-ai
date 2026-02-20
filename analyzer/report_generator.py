from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import ListFlowable, ListItem
from io import BytesIO


def generate_pdf_report(result):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)

    elements = []

    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    heading = styles["Heading1"]

    elements.append(Paragraph("CodeSense AI - Analysis Report", heading))
    elements.append(Spacer(1, 0.5 * inch))

    elements.append(Paragraph("<b>Errors:</b>", normal))
    elements.append(Paragraph(result["errors"], normal))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("<b>Patterns Detected:</b>", normal))
    elements.append(Paragraph(result["patterns"], normal))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph("<b>Suggestions:</b>", normal))
    elements.append(Paragraph(result["suggestions"], normal))
    elements.append(Spacer(1, 0.3 * inch))

    elements.append(Paragraph(f"<b>Score:</b> {result['score']}", normal))

    doc.build(elements)
    buffer.seek(0)

    return buffer
