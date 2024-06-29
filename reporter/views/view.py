from PySide6.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from views.main_view import Ui_MainWindow
import logging
import os
from views.parasite_form_view import initial_parasite_form, parasite_clear_form


class MainView(Ui_MainWindow, QMainWindow):
    """ Main UI class: Handle the main UI of the reporter application """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        super(MainView, self).__init__()
        self.setupUi(self)
        self.login_password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.reset_widgets_state()
        
        self.logger.info("MainView initialized")
        
        # ========= detail in parasite_form_handler.py ===================
        initial_parasite_form(self)
        # ================================================================

    def reset_widgets_state(self):
        """ Reset widgets state """
        self.login_username_lineEdit.clear()
        self.login_password_lineEdit.clear()
        self.serum_pushButton.setEnabled(False)
        self.bacteria_pushButton.setEnabled(False)
        self.bacteriaVirtek_pushButton.setEnabled(False)
        self.molecularBio_pushButton.setEnabled(False)
        self.parasite_pushButton.setEnabled(False)
        self.water_quality_pushButton.setEnabled(False)
        self.food_quality_pushButton.setEnabled(False)
        self.sperm_pushButton.setEnabled(False)
        self.virus_pushButton.setEnabled(False)
        self.chemical_pushButton.setEnabled(False)
        self.pathology_pushButton.setEnabled(False)
        self.approve_report_pushButton.setEnabled(False)
        self.sign_out_pushButton.setEnabled(False)
        
    def enable_main_menu_buttons(self):
        """ Enable main menu buttons """
        self.serum_pushButton.setEnabled(True)
        self.bacteria_pushButton.setEnabled(True)
        self.bacteriaVirtek_pushButton.setEnabled(True)
        self.molecularBio_pushButton.setEnabled(True)
        self.parasite_pushButton.setEnabled(True)
        self.water_quality_pushButton.setEnabled(True)
        self.food_quality_pushButton.setEnabled(True)
        self.sperm_pushButton.setEnabled(True)
        self.virus_pushButton.setEnabled(True)
        self.chemical_pushButton.setEnabled(True)
        self.pathology_pushButton.setEnabled(True)
        self.approve_report_pushButton.setEnabled(True)
        self.sign_out_pushButton.setEnabled(True)

    def clear_all_forms(self):
        """ Clear all forms """
        self.serum_clear_form()
        self.bacteria_clear_form()
        self.bacteria_virtek_clear_form()
        self.micro_bio_clear_form()
        parasite_clear_form(self)
        self.water_quality_clear_form()
        self.food_quality_clear_form()
        self.sperm_quality_clear_form()
        self.virus_clear_form()
        self.chemical_clear_form()
        self.pathology_clear_form()
        self.approve_report_clear_form()
        
    def serum_clear_form(self):
        """ Clear serum form """
        pass
    
    def bacteria_clear_form(self):
        """ Clear bacteria form """
        pass
    
    def bacteria_virtek_clear_form(self):
        """ Clear bacteria virtek form """
        pass
    
    def micro_bio_clear_form(self):
        """ Clear micro bio form """
        pass
    
    def water_quality_clear_form(self):
        """ Clear water quality form """
        pass
    
    def food_quality_clear_form(self):
        """ Clear food quality form """
        pass
    
    def sperm_quality_clear_form(self):
        """ Clear sperm quality form """
        pass
    
    def virus_clear_form(self):
        """ Clear virus form """
        pass
    
    def chemical_clear_form(self):
        """ Clear chemical form """
        pass
    
    def pathology_clear_form(self):
        """ Clear pathology form """
        pass
    
    def approve_report_clear_form(self):
        """ Clear approve report form """
        pass
    
    
    def closeEvent(self, event):
        """ Event handler for close event """
        reply = QMessageBox.question(
            self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
