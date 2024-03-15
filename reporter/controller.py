import logging
import logging.config
from PySide6.QtWidgets import QMessageBox
import os
import yaml


class ReportController:
    """ Report controller class. This class is responsible for handling the report view events. """

    def __init__(self, report_view, report_model) -> None:
        config_file = os.path.join(
            os.path.dirname(__file__), "config_files", "log_config.ini")
        logging.config.fileConfig(config_file)  # load logging configuration
        self.logger = logging.getLogger('sLogger')

        self.main_view = report_view
        self.session_model = report_model

        # add handler to buttons in main Menu
        self.main_view.cytology_pushButton.clicked.connect(
            self.main_view.on_cytology_pushButton_clicked)

        self.main_view.nocropsy_pushButton.clicked.connect(
            self.main_view.on_nocropsy_pushButton_clicked)

        self.main_view.check_report_pushButton.clicked.connect(
            self.main_view.on_check_report_pushButton_clicked)

        self.main_view.sign_out_pushButton.clicked.connect(
            self.main_view.on_sign_out_pushButton_clicked)

        # add handler to login page
        self.main_view.login_pushButton.clicked.connect(
            self.login_button_clicked)
        # add enter key handler to login page in password lineEdit
        self.main_view.login_password_lineEdit.returnPressed.connect(
            self.login_button_clicked)

    def login_button_clicked(self):
        """ Method to handle the login button click event. """
        self.logger.debug("Login button clicked")
        username = self.main_view.login_username_lineEdit.text()
        password = self.main_view.login_password_lineEdit.text()
        if username == "" or password == "":
            QMessageBox.critical(
                self.main_view, "Warning", "Username or password is empty")
        else:
            self.session_model.check_login(username, password)
            if len(self.session_model.current_user) > 0:
                self.logger.debug("Login successful")
            else:
                QMessageBox.critical(
                    self.main_view, "Warning", "Invalid username or password")
