""" Controller to handle events and views for parasite form """
from PySide6.QtWidgets import QFileDialog
from bs4 import BeautifulSoup
from PIL import Image


def get_parasite_report_content(view) -> list:
    html_contents = view.parasiteResultTextEdit.toHtml()
    soup = BeautifulSoup(html_contents, 'html.parser')
    extracted_content = []
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        text = p.get_text()
        images = p.find_all('img')
        image_paths = [img['src'] for img in images]
        extracted_content.append({
            'text': text,
            'images': image_paths
        })
    # convert list of dictionary to plain text
    report_content = [f"{content['text'],content['images']}\n" for content in extracted_content]
    return report_content

def reload_parasite_report(view, report_content)-> None:
    """ Reload parasite report """
    # convert plain text to list of dictionary
    report_content = [content.split('\n') for content in report_content]
    report_content = [{'text': content[0], 'images': content[1]} for content in report_content]
    
    # inser extracted content to comment
    view.parasiteResultTextEdit.clear()
    for content in report_content:
        view.parasiteResultTextEdit.insertPlainText(content['text'])
        for image_path in content['images']:
            view.parasiteResultTextEdit.insertPlainText(f'<img src="{image_path}" />')
    # view html
    view.parasiteResultTextEdit.setHtml(view.parasiteResultTextEdit.toPlainText())


def insert_image_parasite_page(view) -> None:
    # insert image tp QTextEdit
    image_path, _ = QFileDialog.getOpenFileName(view, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
    # check image size if the image width > 500px, resize it to 500px
    if image_path:
        image = Image.open(image_path)
        width, height = image.size

        cursor = view.parasiteResultTextEdit.textCursor()
        if width >= 900:
            cursor.insertHtml(f'<img src="{image_path}" width="900" />')
        else:
            cursor.insertHtml(f'<img src="{image_path}") />')
    

def initial_parasite_form(view)-> None:
    """ Initialize parasite form """
    # set column width for parasite QtreeWidget
    view.parasiteTreeWidget.setColumnWidth(0, 120)      # data -time
    view.parasiteTreeWidget.setColumnWidth(1, 120)      # case ID
    view.parasiteTreeWidget.setColumnWidth(2, 150)      # type
    view.parasiteTreeWidget.setColumnWidth(3, 200)      # Lab name
    view.parasiteTreeWidget.setColumnWidth(4, 100)      # keep method
    view.parasiteTreeWidget.setColumnWidth(5, 100)      # speed
    view.parasiteTreeWidget.setColumnWidth(6, 150)      # status
    
def parasite_clear_form(veiw)->None:
    """ Clear parasite form """
    pass

