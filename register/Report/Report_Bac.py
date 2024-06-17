from reportlab.lib.pagesizes import A4,portrait
from reportlab.pdfgen import canvas
# Add Thai font
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO 
import os
from ftplib import FTP
import sys

font_path = ""
if getattr(sys, 'frozen', False):
    # frozen
    font_path = os.path.join(os.path.dirname(
        sys.executable), "TH Niramit AS Bold.ttf")
else:
    # unfrozen
    font_path = os.path.join(os.path.dirname(__file__), "TH Niramit AS Bold.ttf")
pdfmetrics.registerFont(TTFont('TH Niramit AS Bold.ttf', font_path))

template_path = os.path.join(os.path.dirname(__file__), "PDF","Bac_from.pdf")
output_pdf_path = os.path.join(os.path.dirname(__file__), "OUTPUT","BacReport.pdf")

ftp_username = "cvdtt"
ftp_password = "cvdtt123"
main_ip = ""

# test parameter
number_of_report = "123456721"
number_of_sample = "000000021"
number_of_page = "2"
# page 1
owner_name = "นาย สมชาย ใจดี"
owner_phone = "081-234-5678"
owner_email = "test@gmail.com"
owner_address = "123 หมู่ 4 ต.บ้านใหม่ อ.เมือง จ.เชียงใหม่ 50000"

sender_name = "นาย ทดสอบ ระบบ"
sender_phone = "081-234-5678"
sender_email = "admin@gmail.com"
sender_address = "123 หมู่ 4 ต.บ้านใหม่ อ.เมือง จ.เชียงใหม่ 50000"

animal_type = "Canine"
animal_name = "test_cat"
breed = "test_breed"
sex = "test_sex"
sample_type = "test_sample_type"
aeg = "test_aeg"
result_page1 = "test result of sample 1234567890-12345678901234567890-234567890-"
note_page1 = "test note page 1 0987654320987654321098765421"
# page 2
date_of_regiter_sample = "2021-01-01"
date_of_test = "2021-01-02"
date_of_report = "2021-01-03"
result_page2 = "test result of sample 1234567890-12345678901234567890-234567890-"
note_page2 = "test note page 2 0987654320987654321098765421"
name_of_reporter = "(นาย ทดสอบ รายงาน)"
position_of_reporter = "นักทดสอบรายงาน"
name_of_approve_reporter = "(นาย รับรอง รายงาน)"
position_of_approve_reporter = "นักรับรองรายงาน"

def create_canvas_for_page0():
    # Extract the customer information from the database
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=portrait(A4))
    pdfmetrics.registerFont(TTFont('THSarabunNew',font_path))
    
    c.setFont("THSarabunNew", 16)
    c.drawString(110, 673, number_of_report)
    c.drawString(275, 673, number_of_sample)
    c.drawString(526, 673, number_of_page)
    c.drawString(110, 652, owner_name)
    c.drawString(300, 652, owner_phone)
    c.drawString(437, 652, owner_email)
    c.drawString(70, 629, owner_address)
    c.drawString(110, 608, sender_name)
    c.drawString(300, 608, sender_phone)
    c.drawString(437, 608, sender_email)
    c.drawString(70, 585, sender_address)
    c.drawString(90, 565, animal_type)
    c.drawString(210, 565, animal_name)
    c.drawString(340, 565, breed)
    c.drawString(460, 565,sex)
    c.drawString(110, 543, sample_type)
    c.drawString(460, 543, aeg)
    c.drawString(70, 500, result_page1)
    c.drawString(70, 155, note_page1)
    c.save()
    packet.seek(0)
    return packet

def create_canvas_for_page1():
    # Extract the customer information from the database
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=portrait(A4))
    pdfmetrics.registerFont(TTFont('THSarabunNew',font_path))
    
    c.setFont("THSarabunNew", 16)
    c.drawString(110, 706, number_of_report)
    c.drawString(285, 706, number_of_sample)
    c.drawString(526, 706, number_of_page)
    c.drawString(110, 684, date_of_regiter_sample)
    c.drawString(300, 684, date_of_test)
    c.drawString(460, 684, date_of_report)
    c.drawString(70, 641, result_page2)
    c.drawString(85, 252, note_page2)
    c.drawString(112, 133, name_of_reporter)
    c.drawString(123, 117, position_of_reporter)
    c.drawString(375, 133, name_of_approve_reporter)
    c.drawString(385, 117, position_of_approve_reporter)
    c.save()
    packet.seek(0)
    return packet



def gen_pdf_output():
    # Create a PdfWriter object to write the output PDF
    output = PdfWriter()
    # Read the existing template PDF
    template_pdf = PdfReader(template_path)
    # Iterate through the pages of the template PDF
    for i in range(len(template_pdf.pages)):
        template_page = template_pdf.pages[i]
        if i == 0:
            packet = create_canvas_for_page0()
            new_pdf = PdfReader(packet)
            new_page = new_pdf.pages[0]
        if i == 1:
            packet = create_canvas_for_page1()
            new_pdf = PdfReader(packet)
            new_page = new_pdf.pages[0]
        template_page.merge_page(new_page)
        output.add_page(template_page)

    # Write the output PDF to a file
    with open(output_pdf_path, "wb") as output_stream:
        output.write(output_stream)
    # close the packet
    packet.close()

gen_pdf_output()