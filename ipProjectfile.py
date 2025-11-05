from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Certificate of Achievement', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create a PDF instance
pdf = PDF()
pdf.add_page()

# Title
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Certificate of Achievement', 0, 1, 'C')

# Add some space
pdf.ln(20)

# Content
pdf.set_font('Arial', '', 12)
text = (
    "This certificate is proudly presented to \n"
    "[Recipient's Name] \n\n"
    "For successfully completing the project titled: \n"
    "'Analysis of PS4 Game Sales' \n\n"
    "In this project, various Python codes were utilized to analyze dataframes and create data visualizations, \n"
    "providing insights into PS4 game sales trends and patterns. \n\n"
    "Awarded on: [Date]"
)
pdf.multi_cell(0, 10, text, align='C')

# Signature space
pdf.ln(30)
pdf.set_font('Arial', 'I', 12)
pdf.cell(0, 10, 'Authorized Signatory', 0, 1, 'R')

# Output the PDF
pdf.output("ps4_sales_analysis_certificate.pdf")

print("Certificate generated as 'ps4_sales_analysis_certificate.pdf'")


