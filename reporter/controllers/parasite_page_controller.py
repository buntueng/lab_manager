""" Bind events for parasite page """
from PySide6.QtWidgets import QFileDialog
from bs4 import BeautifulSoup
from PIL import Image
from views.parasite_form_view import get_parasite_report_content,insert_image_parasite_page
from models.parasite_page_model import save_parasite_data


def bind_event_parasite_page(controller):
    """ Bind event for parasite form """
    controller.view.parasiteSearchPushButton.clicked.connect(lambda: search_parasite_clicked(controller))
    controller.view.parasiteSelectPushButton.clicked.connect(lambda: select_parasite_clicked(controller))
    controller.view.parasiteInsertImagePushButton.clicked.connect(lambda: insert_image_clicked(controller))
    controller.view.parasiteSavePushButton.clicked.connect(lambda: save_report_clicked(controller))
    
def search_parasite_clicked(controller):
    # controller.model.load_parasite_wait_report()
    pass

def save_report_clicked(controller):
    report_content = get_parasite_report_content(controller.view)
    current_user_id = controller.current_user_info
    # print(current_user_id)
    if save_parasite_data(report_content):
        print("OK")
    else:
        print("Fail")
    

def reload_parasite_report(controller):
    print("reload OK")

def select_parasite_clicked(controller):
    print("select OK")

def insert_image_clicked(controller):
    insert_image_parasite_page(controller.view)