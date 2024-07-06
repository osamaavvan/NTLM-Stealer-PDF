from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import red

def create_pdf_with_smb_link(smb_server, share_name, file_name, output_pdf):
    smb_url = f"file://{smb_server}/{share_name}/{file_name}"
    
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter
    c.drawString(100, 750, "Click the link below to access the shared folder:")
    link_text = "Access the shared folder here"
    c.setFillColor(red)
    c.drawString(100, 730, link_text)
    c.linkURL(smb_url, (100, 730, 100 + c.stringWidth(link_text), 745), relative=1)
    c.save()
    return output_pdf

smb_server = input("Enter SMB server: ")
share_name = input("Enter share name: ")
file_name = input("Enter file name: ")
output_pdf = "smb_custom_link.pdf"

create_pdf_with_smb_link(smb_server, share_name, file_name, output_pdf)
