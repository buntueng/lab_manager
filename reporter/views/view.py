from PySide6.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from views.main_view import Ui_MainWindow
import logging
import logging.config
import os


class MainView(Ui_MainWindow, QMainWindow):
    """ Main UI class: Handle the main UI of the reporter application """

    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)
        config_file = os.path.join(os.path.dirname(os.path.dirname(
            __file__)), "config_files", "log_config.ini")
        logging.config.fileConfig(config_file)  # load logging configuration
        self.logger = logging.getLogger('sLogger')
        self.login_password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.reset_widgets_state()

        self.logger.info("MainView initialized")

    def reset_widgets_state(self):
        """ Reset widgets state """
        self.login_username_lineEdit.clear()
        self.login_password_lineEdit.clear()

        self.cytology_pushButton.setEnabled(False)
        self.nocropsy_pushButton.setEnabled(False)
        self.check_report_pushButton.setEnabled(False)
        self.sign_out_pushButton.setEnabled(False)

    def on_login_pushButton_clicked(self):
        """ Event handler for login button clicked """
        self.logger.info("Login button clicked")
        self.cytology_pushButton.setEnabled(True)
        self.nocropsy_pushButton.setEnabled(True)
        self.check_report_pushButton.setEnabled(True)
        self.sign_out_pushButton.setEnabled(True)

    def on_cytology_pushButton_clicked(self):
        """ Event handler for cytology button clicked """
        self.logger.info("Cytology button clicked")

    def on_nocropsy_pushButton_clicked(self):
        """ Event handler for necropsy button clicked """
        self.logger.info("Necropsy button clicked")

    def on_check_report_pushButton_clicked(self):
        """ Event handler for check report button clicked """
        self.logger.info("Check report button clicked")

    def on_sign_out_pushButton_clicked(self):
        """ Event handler for sign out button clicked """
        self.logger.info("Sign out button clicked")

    def closeEvent(self, event):
        """ Event handler for close event """
        self.logger.info("Close event")
        reply = QMessageBox.question(
            self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
