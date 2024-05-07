import mariadb
import yaml
import os
import sys
import reportlab
# create a PDF file using reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Image, Frame
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('THNiramitAS', 'TH Niramit AS.ttf'))


def create_hemato(sample_detail, data):
    """This function is used to create the hematology test detail."""
    pass


def create_molecular_biology(sample_detail, data, output_file):
    """This function is used to create the molecular biology test detail."""

    left_margin = 0.5 * inch
    right_margin = 0.5 * inch
    top_margin = 0.25 * inch
    bottom_margin = 0.25 * inch

    # Create a SimpleDocTemplate object with custom margins
    pdf_file = SimpleDocTemplate(output_file, pagesize=A4,
                                 leftMargin=left_margin, rightMargin=right_margin,
                                 topMargin=top_margin, bottomMargin=bottom_margin)

    elements = []
    cvdtt_logo = os.path.join(os.path.dirname(__file__), "cvdtt_logo.png")
    title_data = [
        [Image(cvdtt_logo, width=1.5*inch, height=1*inch),
         'ใบคำขอรับบริการทดสอบจุลพยาธิวิทยา/เซลล์วินิจฉัย', ''],
        ['', Paragraph("ศูนย์ชันสูตรโรคสัตว์และถ่ายทอดเทคโนโลยี คณะสัตวแพทยศาสตร์ มหาวิทยาลัยเชียงใหม่ <br/> (Center of Veterinary Diagnosis and Technology Transfer) <br/> Tel. 053-948041 Mobile 094-6362641 <br/> E-mail vet_diag@cmu.ac.th", set_paragraph_style()), ''],
    ]
    col_widths = [120, 320, 100]  # Adjust the widths as needed
    # Create a table from the data
    table = Table(title_data, colWidths=col_widths)

    # Define the style for the table
    style = TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'THNiramitAS'),  # Specify the font name
        ('FONTSIZE', (1, 0), (1, 1), 20),
        ('FONTSIZE', (1, 1), (-1, -1), 10),
        # Background color for the first row
        ('BACKGROUND', (0, 0), (-1, -1), '#FFFFFF'),
        # Center alignment for all cells
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        # Middle vertical alignment for all cells
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        # ('SPAN', (1, 0), (1, 1)),
        ('SPAN', (0, 0), (0, 1)),
        # zero padding
        ('PADDING', (0, 0), (-1, -1), 0),
        # show grid
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    table.setStyle(style)

    # Add the table to the list of elements
    elements.append(table)
    # add space
    elements.append(Paragraph("<br/><br/>", getSampleStyleSheet()['BodyText']))

    # Define the data for the table
    data = [['Name', 'บ้าน', 'City'],
            ['John Doe', '35', 'New York'],
            ['Jane Smith', '28', 'Los Angeles'],
            ['Bob Johnson', '42', 'Chicago']]

    # Add the table
    table = Table(data)
    table_style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                              ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                              ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                              # Specify the font name
                              ('FONTNAME', (0, 0), (-1, -1), 'THNiramitAS'),
                              ('FONTSIZE', (0, 0), (-1, -1), 16),
                              ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                              ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                              ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(table_style)
    elements.append(table)

    # # Add an image
    # image = Image('example_image.png', width=3*mm, height=2*mm)
    # elements.append(image)

    # Build the PDF
    pdf_file.build(elements)


def set_paragraph_style():
    styles = getSampleStyleSheet()
    style = styles['BodyText']  # You can choose other styles as needed
    style.fontName = 'THNiramitAS'  # Set the desired font name
    style.fontSize = 12  # Set the desired font size
    return style
# =================================================================================================


def get_molecular_biology_test_detail(id):
    """This function is used to get the detail of the molecular biology test."""
    pass


def select_data_from_db(sql_cmd, parameters):
    """This function is used to select data from the database."""
    # read server_config.yml and sql_cmd.yml
    server_config_file = os.path.join(
        os.path.dirname(__file__), "server_config.yml")
    with open(server_config_file, "r", encoding='utf-8') as ymlfile:
        server_config = yaml.load(ymlfile, Loader=yaml.FullLoader)
    # connect to database
    conn = mariadb.connect(
        user=server_config["user"],
        password=server_config["password"],
        host=server_config["host"],
        port=server_config["port"],
        database=server_config["database"]
    )
    cur = conn.cursor()
    # get data
    cur.execute(sql_cmd, [parameters])
    data = cur.fetchall()
    conn.close()
    return data


if __name__ == "__main__":
    sql_cmd_file = os.path.join(os.path.dirname(__file__), "sql_cmd.yml")
    with open(sql_cmd_file, "r", encoding='utf-8') as ymlfile:
        sql_cmd = yaml.load(ymlfile, Loader=yaml.FullLoader)
    cmd = sql_cmd["get_sample_data"]
    sample_data = select_data_from_db(cmd, "113")
    cmd = sql_cmd["get_molecular_biology_tests"]
    test_data = select_data_from_db(cmd, "113")

    # if run from script the path is relative to the script else it is relative to the exe file
    output_file = ""
    if getattr(sys, 'frozen', False):
        # frozen
        output_file = os.path.join(os.path.dirname(sys.executable),
                                   "molecular_biology_test_detail.pdf")
    else:
        # unfrozen
        output_file = os.path.join(os.path.dirname(
            __file__), "molecular_biology_test_detail.pdf")

    create_molecular_biology(sample_data, test_data, output_file)
