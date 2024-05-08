import logging
import logging.config
from PySide6.QtWidgets import QMessageBox
import os
import yaml


class ReportController:
    """ Report controller class. This class is responsible for handling the report view events. """

    def __init__(self, report_view, report_model, logger) -> None:
        self.logger = logger

        self.view = report_view
        self.model = report_model
        self.current_user_info = []

        # add handler to buttons in main Menu
        self.view.cytology_pushButton.clicked.connect(
            self.view.on_cytology_pushButton_clicked)

        self.view.nocropsy_pushButton.clicked.connect(
            self.view.on_nocropsy_pushButton_clicked)

        self.view.check_report_pushButton.clicked.connect(
            self.view.on_check_report_pushButton_clicked)

        self.view.sign_out_pushButton.clicked.connect(
            self.view.on_sign_out_pushButton_clicked)

        # add handler to login page
        self.event_handler_login_page()

    def event_handler_login_page(self):
        """ Method to handle the login page events. """
        self.view.login_pushButton.clicked.connect(
            self.login_button_clicked)
        # add handler to login password lineEdit returnPressed event
        self.view.login_password_lineEdit.returnPressed.connect(
            self.login_button_clicked)

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
                    print(self.current_user_info)
                    # enable all buttons in main menu
                else:
                    QMessageBox.critical(self.view, "Warning",
                                         "คุณไม่ได้รับอนุญาตให้ใช้งานระบบนี้")
            else:
                QMessageBox.critical(
                    self.view, "Warning", "Invalid username or password")
