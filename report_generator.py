from fpdf import FPDF

def generate_report(name, career, details):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt=f"Career Counselling Report for {name}", ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=f"Recommended Career Path: {career}\n")
    pdf.multi_cell(0, 10, txt=f"Description: {details['description']}\n")
    pdf.multi_cell(0, 10, txt="Skills Required: " + ", ".join(details['skills']))
    pdf.multi_cell(0, 10, txt="Suggested Courses: " + ", ".join(details['courses']))
    filename = f"{name.replace(' ', '_').lower()}_career_report.pdf"
    pdf.output(filename)
    return filename
