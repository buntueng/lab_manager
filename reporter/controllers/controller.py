import logging
from PySide6.QtWidgets import QMessageBox
import os
import yaml
from controllers.parasite_page_controller import bind_event_parasite_page



class ReportController:
    """ Report controller class. This class is responsible for handling the report view events. """

    def __init__(self, report_view, report_model) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)

        self.view = report_view
        self.model = report_model
        self.current_user_info = []
        
        self.view.user_info_label.clear()
        # onload go to login page
        self.view.stackedWidget.setCurrentIndex(0)
        self.view.reset_widgets_state()

        # add handler to buttons in main Menu
        self.bind_event_in_main_menu()
        self.bind_events_in_login_page()
        self.bind_event_in_bacteria_page()
        self.bind_event_in_bacteria_virtek_page()
        self.bind_event_in_micro_bio_page()
        bind_event_parasite_page(self)
        self.bind_event_in_water_quality_page()
        self.bind_event_in_food_quality_page()
        self.bind_event_in_sperm_quality_page()
        self.bind_event_in_virus_page()
        self.bind_event_in_chemical_page()
        self.bind_event_in_pathology_page()
        self.bind_event_in_approve_report_page()

    def bind_event_in_main_menu(self):
        self.view.serum_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(1))
        self.view.bacteria_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(2))
        self.view.bacteriaVirtek_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(3))
        self.view.molecularBio_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(4))
        self.view.parasite_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(5))
        self.view.water_quality_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(6))
        self.view.food_quality_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(7))
        self.view.sperm_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(8))
        self.view.virus_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(9))
        self.view.chemical_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(10))
        self.view.pathology_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(11))
        self.view.approve_report_pushButton.clicked.connect(
            lambda: self.view.stackedWidget.setCurrentIndex(12))
        self.view.sign_out_pushButton.clicked.connect(
            self.sign_out_button_clicked)

    def bind_events_in_login_page(self):
        """ Bind events in login page """
        self.view.login_pushButton.clicked.connect(self.login_button_clicked)
        self.view.login_password_lineEdit.returnPressed.connect(self.login_button_clicked)

    def bind_event_in_bacteria_page(self):
        self.logger.debug("Bind event in bacteria page")

    def bind_event_in_bacteria_virtek_page(self):
        pass

    def bind_event_in_micro_bio_page(self):
        pass

    def bind_event_in_parasite_page(self):
        pass

    def bind_event_in_water_quality_page(self):
        pass

    def bind_event_in_food_quality_page(self):
        pass

    def bind_event_in_sperm_quality_page(self):
        pass

    def bind_event_in_virus_page(self):
        pass

    def bind_event_in_chemical_page(self):
        pass

    def bind_event_in_pathology_page(self):
        pass

    def bind_event_in_approve_report_page(self):
        pass

    def login_button_clicked(self):
        """ Method to handle the login button click event. """
        self.logger.debug("Login button clicked")
        username = self.view.login_username_lineEdit.text()
        password = self.view.login_password_lineEdit.text()
        if username == "" or password == "":
            QMessageBox.critical(
                self.view, "Warning", "Username or password is empty")
        else:
            current_user_info = self.model.check_login(username, password)
            if len(current_user_info) > 0:
                self.current_user_info = current_user_info[0]
                if self.current_user_info[0] < 4:   # addmin and vet-med
                    self.view.stackedWidget.setCurrentIndex(1)
                    self.view.user_info_label.setText(f"{self.current_user_info[2]}{self.current_user_info[3]} {self.current_user_info[4]}")
                    self.view.enable_main_menu_buttons()
                else:
                    QMessageBox.critical(self.view, "Warning",
                                         "คุณไม่ได้รับอนุญาตให้ใช้งานระบบนี้")
            else:
                QMessageBox.critical(
                    self.view, "Warning", "Invalid username or password")

    def sign_out_button_clicked(self):
        self.view.stackedWidget.setCurrentIndex(0)
        self.view.reset_widgets_state()
        self.view.user_info_label.clear()
        self.current_user_info = []
        self.view.clear_all_forms()