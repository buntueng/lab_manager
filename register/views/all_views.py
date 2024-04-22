from views.main_app_view import Ui_main_app_view
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QTreeWidgetItem
# import QTreeWidgetItem

import re


class MainAppView(QMainWindow, Ui_main_app_view):
    """"Main application view. Inherits from QMainWindow and Ui_main_app_view."""

    def __init__(self):
        super(MainAppView, self).__init__()
        self.setupUi(self)
        self.clear_information()
        self.show_login_page()
        self.disable_all_buttons()

        self.reset_widgets_in_job_register_page()

    def disable_all_buttons(self):
        """Disable all buttons in the main page."""
        self.sign_out_pushButton.setEnabled(False)
        self.customer_reg_pushButton.setEnabled(False)

        self.case_register_pushButton.setEnabled(False)
        self.check_job_pushButton.setEnabled(False)
        self.barcode_pushButton.setEnabled(False)
        self.lab_order_pushButton.setEnabled(False)
        self.bill_pushButton.setEnabled(False)
        self.check_report_pushButton.setEnabled(False)
        self.employee_pushButton.setEnabled(False)
        self.personal_info_pushButton.setEnabled(False)
        self.update_prog_pushButton.setEnabled(False)
        self.sign_out_pushButton.setEnabled(False)

    def enable_all_buttons(self):
        """Enable all buttons in the main page."""
        self.sign_out_pushButton.setEnabled(True)
        self.customer_reg_pushButton.setEnabled(True)
        self.case_register_pushButton.setEnabled(True)
        self.check_job_pushButton.setEnabled(True)
        self.barcode_pushButton.setEnabled(True)
        self.lab_order_pushButton.setEnabled(True)
        self.bill_pushButton.setEnabled(True)
        self.check_report_pushButton.setEnabled(True)
        self.employee_pushButton.setEnabled(True)
        self.personal_info_pushButton.setEnabled(True)
        self.update_prog_pushButton.setEnabled(True)

    def show_view(self):
        """Show the view."""
        self.show()

    def hide_view(self):
        """Hide the view."""
        self.hide()

    def close_view(self):
        """"Close the view."""
        self.close()

    def clear_information(self):
        """Clear information in the main page."""
        self.clear_user_and_password()

    # ==================== login page ====================

    def clear_user_and_password(self):
        """Clear username and password in login page."""
        self.username_lineEdit.clear()
        self.password_lineEdit.clear()

    # page order follow the order in the stacked widget
    # Index0 - login page
    # Index1 - new customer page
    # Index2 - new job page
    # Index3 - specimen page
    # Index4 - check job page
    # Index5 - employee page
    # Index6 - check report page
    # Index7 - bill page
    # Index8 - barcode page
    # Index9 - lab report page
    # Index10 - edit personal page
    # Index11 - update page
    # Index12 - Molucular biology page
    # Index13 - Bacteria biology page
    # Index14 - Parasite biology page

    # ==================== login page ====================
    def show_login_page(self):
        """Show the login page."""
        self.stackedWidget.setCurrentIndex(0)

    # ==================== customer register page ====================
    def show_customer_register_page(self):
        """Show the customer register page."""
        self.stackedWidget.setCurrentIndex(1)
        self.new_customer_private_radioBT.setChecked(True)

    # ==================== job register page =====================
    def show_job_register_page(self):
        """Show the job register page."""
        self.stackedWidget.setCurrentIndex(2)
        # reset state of all widgets in the job register page
        self.reset_widgets_in_job_register_page()

    def backto_job_register_page(self):
        """Back to the job register page."""
        self.stackedWidget.setCurrentIndex(2)
    # ==================== check job progress ======================

    def show_check_job_progress_page(self):
        """Show the check job progress page."""
        self.stackedWidget.setCurrentIndex(4)

    # ===================== employee page ========================
    def show_employee_page(self):
        """Show the employee page."""
        self.stackedWidget.setCurrentIndex(5)

    # ===================== check report page =====================
    def show_check_report_page(self):
        """Show the check report page."""
        self.stackedWidget.setCurrentIndex(6)

    # ========================= bill page ========================
    def show_bill_page(self):
        """Show the bill page."""
        self.stackedWidget.setCurrentIndex(7)

    # ====================== print barcode page ========================
    def show_print_barcode_page(self):
        """Show the print barcode page."""
        self.stackedWidget.setCurrentIndex(8)
    # ====================== lab report page =========================

    def show_lab_order_report_page(self):
        """Show the lab report page."""
        self.stackedWidget.setCurrentIndex(9)

    # ====================== personal information page ====================
    def show_personal_information_page(self):
        """Show the personal information page."""
        self.stackedWidget.setCurrentIndex(10)
    # ======================= specimen page ========================

    def show_specimen_page(self):
        """Show the specimen page."""
        self.stackedWidget.setCurrentIndex(3)
        self.clear_specimen_information()
        self.specimen_page_save_pushButton.setEnabled(True)
        self.disable_lab_buttons()
    # ==================== update page ====================

    def show_update_page(self):
        """Show the update page."""
        self.stackedWidget.setCurrentIndex(11)
    # =======================================================

    def get_molecular_biology_data(self) -> list:
        """Get molecular biology data."""
        data = []
        checkbox_state = []
        error_message = []

        # first test in the lab
        checkbox_state.append(self.avian_AI_1_checkBox.isChecked())
        data.append(self.avian_AI_1_checkBox.text())
        # integer from lineEdit if blank return 0
        if self.avian_AI_1_lineEdit.text() == "":
            data.append(0)
        else:
            # try to add integer to list if not integer add error message
            try:
                data.append(int(self.avian_AI_1_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_AI_1_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.avian_AI_1_checkBox.text())[0][1:-1]
        data.append(int(price))

        # second test in the lab
        checkbox_state.append(self.avian_AI_2_checkBox.isChecked())
        data.append(self.avian_AI_2_checkBox.text())
        if self.avian_AI_2_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_AI_2_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_AI_2_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.avian_AI_2_checkBox.text())[0][1:-1]
        data.append(int(price))

        # third test in the lab
        checkbox_state.append(self.avian_ibv_checkBox.isChecked())
        data.append(self.avian_ibv_checkBox.text())
        if self.avian_ibv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_ibv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_ibv_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.avian_ibv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # forth test in the lab
        checkbox_state.append(self.avian_ibdv_checkBox.isChecked())
        data.append(self.avian_ibdv_checkBox.text())
        if self.avian_ibdv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_ibdv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_ibdv_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.avian_ibdv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fifth test in the lab
        checkbox_state.append(self.avian_ilt_checkBox.isChecked())
        data.append(self.avian_ilt_checkBox.text())
        if self.avian_ilt_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_ilt_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_ilt_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.avian_ilt_checkBox.text())[0][1:-1]
        data.append(int(price))

        # sixth test in the lab
        checkbox_state.append(self.avian_ndv_checkBox.isChecked())
        data.append(self.avian_ndv_checkBox.text())
        if self.avian_ndv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_ndv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_ndv_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.avian_ndv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # seventh test in the lab
        checkbox_state.append(self.avian_ndv_2_checkBox.isChecked())
        data.append(self.avian_ndv_2_checkBox.text())
        if self.avian_ndv_2_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_ndv_2_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_ndv_2_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.avian_ndv_2_checkBox.text())[0][1:-1]
        data.append(int(price))

        # eighth test in the lab
        checkbox_state.append(self.avian_pdd_checkBox.isChecked())
        data.append(self.avian_pdd_checkBox.text())
        if self.avian_pdd_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_pdd_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_pdd_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.avian_pdd_checkBox.text())[0][1:-1]
        data.append(int(price))

        # ninth test in the lab
        checkbox_state.append(self.avian_pbfdv_checkBox.isChecked())
        data.append(self.avian_pbfdv_checkBox.text())
        if self.avian_pbfdv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_pbfdv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_pbfdv_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.avian_pbfdv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # tenth test in the lab
        checkbox_state.append(self.avian_chlamydia_checkBox.isChecked())
        data.append(self.avian_chlamydia_checkBox.text())
        if self.avian_chlamydia_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_chlamydia_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_chlamydia_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.avian_chlamydia_checkBox.text())[0][1:-1]
        data.append(int(price))

        # eleventh test in the lab
        checkbox_state.append(self.avian_pasteurella_checkBox.isChecked())
        data.append(self.avian_pasteurella_checkBox.text())
        if self.avian_pasteurella_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_pasteurella_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_pasteurella_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.avian_pasteurella_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twelfth test in the lab
        checkbox_state.append(self.avian_mg_checkBox.isChecked())
        data.append(self.avian_mg_checkBox.text())
        if self.avian_mg_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.avian_mg_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.avian_mg_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.avian_mg_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirteenth test in the lab
        checkbox_state.append(self.feline_felv_checkBox.isChecked())
        data.append(self.feline_felv_checkBox.text())
        if self.feline_felv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.feline_felv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.feline_felv_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.feline_felv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fourteenth test in the lab
        checkbox_state.append(self.feline_fip_checkBox.isChecked())
        data.append(self.feline_fip_checkBox.text())
        if self.feline_fip_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.feline_fip_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.feline_fip_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.feline_fip_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fifteenth test in the lab
        checkbox_state.append(self.feline_fiv_checkBox.isChecked())
        data.append(self.feline_fiv_checkBox.text())
        if self.feline_fiv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.feline_fiv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.feline_fiv_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.feline_fiv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # sixteenth test in the lab
        checkbox_state.append(self.feline_panleukopenia_checkBox.isChecked())
        data.append(self.feline_panleukopenia_checkBox.text())
        if self.feline_panleukopenia_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.feline_panleukopenia_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.feline_panleukopenia_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.feline_panleukopenia_checkBox.text())[0][1:-1]
        data.append(int(price))

        # seventeenth test in the lab
        checkbox_state.append(self.canine_cdv_checkBox.isChecked())
        data.append(self.canine_cdv_checkBox.text())
        if self.canine_cdv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.canine_cdv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.canine_cdv_lineEdit.text() + " is not integer")

        price = re.findall("\(.*\)", self.canine_cdv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # eighteenth test in the lab
        checkbox_state.append(self.canine_cpv_checkBox.isChecked())
        data.append(self.canine_cpv_checkBox.text())
        if self.canine_cpv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.canine_cpv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.canine_cpv_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.canine_cpv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # nineteenth test in the lab
        checkbox_state.append(self.equine_ehv_checkBox.isChecked())
        data.append(self.equine_ehv_checkBox.text())
        if self.equine_ehv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.equine_ehv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.equine_ehv_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.equine_ehv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twentieth test in the lab
        checkbox_state.append(self.equine_ahs_checkBox.isChecked())
        data.append(self.equine_ahs_checkBox.text())
        if self.equine_ahs_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.equine_ahs_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.equine_ahs_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.equine_ahs_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twenty-first test in the lab
        checkbox_state.append(self.blood_1_ana_checkBox.isChecked())
        data.append(self.blood_1_ana_checkBox.text())
        if self.blood_1_ana_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_1_ana_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_1_ana_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.blood_1_ana_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twenty-second test in the lab
        checkbox_state.append(self.blood_1_babe_checkBox.isChecked())
        data.append(self.blood_1_babe_checkBox.text())
        if self.blood_1_babe_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_1_babe_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_1_babe_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_1_babe_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twenty-third test in the lab
        checkbox_state.append(self.blood_1_ehr_checkBox.isChecked())
        data.append(self.blood_1_ehr_checkBox.text())
        if self.blood_1_ehr_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_1_ehr_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_1_ehr_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.blood_1_ehr_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twenty-fourth test in the lab
        checkbox_state.append(self.blood_1_the_checkBox.isChecked())
        data.append(self.blood_1_the_checkBox.text())
        if self.blood_1_the_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_1_the_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_1_the_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.blood_1_the_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twenty-fifth test in the lab
        checkbox_state.append(self.blood_1_haem_checkBox.isChecked())
        data.append(self.blood_1_haem_checkBox.text())
        if self.blood_1_haem_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_1_haem_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_1_haem_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_1_haem_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twenty-sixth test in the lab
        checkbox_state.append(self.blood_1_ecanis_checkBox.isChecked())
        data.append(self.blood_1_ecanis_checkBox.text())
        if self.blood_1_ecanis_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_1_ecanis_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_1_ecanis_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_1_ecanis_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twenty-seventh test in the lab
        checkbox_state.append(self.blood_1_leis_checkBox.isChecked())
        data.append(self.blood_1_leis_checkBox.text())
        if self.blood_1_leis_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_1_leis_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_1_leis_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_1_leis_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twenty-eighth test in the lab
        checkbox_state.append(self.blood_1_try_checkBox.isChecked())
        data.append(self.blood_1_try_checkBox.text())
        if self.blood_1_try_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_1_try_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_1_try_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_1_try_checkBox.text())[0][1:-1]
        data.append(int(price))

        # twenty-ninth test in the lab
        checkbox_state.append(self.blood_2_asf_1_checkBox.isChecked())
        data.append(self.blood_2_asf_1_checkBox.text())
        if self.blood_2_asf_1_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_2_asf_1_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_2_asf_1_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_2_asf_1_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirtieth test in the lab
        checkbox_state.append(self.blood_2_asf_2_checkBox.isChecked())
        data.append(self.blood_2_asf_2_checkBox.text())
        if self.blood_2_asf_2_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_2_asf_2_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_2_asf_2_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_2_asf_2_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirty-first test in the lab
        checkbox_state.append(self.blood_2_asf_3_checkBox.isChecked())
        data.append(self.blood_2_asf_3_checkBox.text())
        if self.blood_2_asf_3_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_2_asf_3_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_2_asf_3_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_2_asf_3_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirty-second test in the lab
        checkbox_state.append(self.blood_2_csf_checkBox.isChecked())
        data.append(self.blood_2_csf_checkBox.text())
        if self.blood_2_csf_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_2_csf_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_2_csf_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_2_csf_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirty-third test in the lab
        checkbox_state.append(self.blood_2_hp_checkBox.isChecked())
        data.append(self.blood_2_hp_checkBox.text())
        if self.blood_2_hp_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_2_hp_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_2_hp_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_2_hp_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirty-fourth test in the lab
        checkbox_state.append(self.blood_2_prrsv_checkBox.isChecked())
        data.append(self.blood_2_prrsv_checkBox.text())
        if self.blood_2_prrsv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_2_prrsv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_2_prrsv_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_2_prrsv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirty-fifth test in the lab
        checkbox_state.append(self.blood_2_pcv_checkBox.isChecked())
        data.append(self.blood_2_pcv_checkBox.text())
        if self.blood_2_pcv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_2_pcv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_2_pcv_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_2_pcv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirty-sixth test in the lab
        checkbox_state.append(self.blood_2_ped_checkBox.isChecked())
        data.append(self.blood_2_ped_checkBox.text())
        if self.blood_2_ped_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.blood_2_ped_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.blood_2_ped_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.blood_2_ped_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirty-seventh test in the lab
        checkbox_state.append(self.elephant_eehv1a_4_checkBox.isChecked())
        data.append(self.elephant_eehv1a_4_checkBox.text())
        if self.elephant_eehv1a_4_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.elephant_eehv1a_4_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.elephant_eehv1a_4_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.elephant_eehv1a_4_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirty-eighth test in the lab
        checkbox_state.append(self.elephant_eehv1a_1_checkBox.isChecked())
        data.append(self.elephant_eehv1a_1_checkBox.text())
        if self.elephant_eehv1a_1_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.elephant_eehv1a_1_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.elephant_eehv1a_1_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.elephant_eehv1a_1_checkBox.text())[0][1:-1]
        data.append(int(price))

        # thirty-ninth test in the lab
        checkbox_state.append(self.elephant_eehv1a_2_checkBox.isChecked())
        data.append(self.elephant_eehv1a_2_checkBox.text())
        if self.elephant_eehv1a_2_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.elephant_eehv1a_2_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.elephant_eehv1a_2_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.elephant_eehv1a_2_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fortieth test in the lab
        checkbox_state.append(self.elephant_eehv4_1_checkBox.isChecked())
        data.append(self.elephant_eehv4_1_checkBox.text())
        if self.elephant_eehv4_1_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.elephant_eehv4_1_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.elephant_eehv4_1_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.elephant_eehv4_1_checkBox.text())[0][1:-1]
        data.append(int(price))

        # forty-first test in the lab
        checkbox_state.append(self.elephant_eehv4_2_checkBox.isChecked())
        data.append(self.elephant_eehv4_2_checkBox.text())
        if self.elephant_eehv4_2_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.elephant_eehv4_2_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.elephant_eehv4_2_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.elephant_eehv4_2_checkBox.text())[0][1:-1]
        data.append(int(price))

        # third column
        # forty-second test in the lab
        checkbox_state.append(self.others_bird_1_checkBox.isChecked())
        data.append(self.others_bird_1_checkBox.text())
        if self.others_bird_1_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_bird_1_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_bird_1_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_bird_1_checkBox.text())[0][1:-1]
        data.append(int(price))

        # forty-third test in the lab
        checkbox_state.append(self.others_bird_2_checkBox.isChecked())
        data.append(self.others_bird_2_checkBox.text())
        if self.others_bird_2_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_bird_2_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_bird_2_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_bird_2_checkBox.text())[0][1:-1]
        data.append(int(price))

        # forty-fourth test in the lab
        checkbox_state.append(self.others_clos_checkBox.isChecked())
        data.append(self.others_clos_checkBox.text())
        if self.others_clos_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_clos_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_clos_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_clos_checkBox.text())[0][1:-1]
        data.append(int(price))

        # forty-fifth test in the lab
        checkbox_state.append(self.others_lep_checkBox.isChecked())
        data.append(self.others_lep_checkBox.text())
        if self.others_lep_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_lep_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_lep_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_lep_checkBox.text())[0][1:-1]
        data.append(int(price))

        # forty-sixth test in the lab
        checkbox_state.append(self.others_toxo_checkBox.isChecked())
        data.append(self.others_toxo_checkBox.text())
        if self.others_toxo_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_toxo_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_toxo_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_toxo_checkBox.text())[0][1:-1]
        data.append(int(price))

        # forty-seventh test in the lab
        checkbox_state.append(self.others_melio_checkBox.isChecked())
        data.append(self.others_melio_checkBox.text())
        if self.others_melio_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_melio_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_melio_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_melio_checkBox.text())[0][1:-1]
        data.append(int(price))

        # forty-eighth test in the lab
        checkbox_state.append(self.others_myco_checkBox.isChecked())
        data.append(self.others_myco_checkBox.text())
        if self.others_myco_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_myco_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_myco_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_myco_checkBox.text())[0][1:-1]
        data.append(int(price))

        # forty-ninth test in the lab
        checkbox_state.append(self.others_mavium_checkBox.isChecked())
        data.append(self.others_mavium_checkBox.text())
        if self.others_mavium_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_mavium_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_mavium_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_mavium_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fiftieth test in the lab
        checkbox_state.append(self.others_mbovis_checkBox.isChecked())
        data.append(self.others_mbovis_checkBox.text())
        if self.others_mbovis_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_mbovis_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_mbovis_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_mbovis_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fifty-first test in the lab
        checkbox_state.append(self.others_mtube_checkBox.isChecked())
        data.append(self.others_mtube_checkBox.text())
        if self.others_mtube_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_mtube_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_mtube_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_mtube_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fifty-second test in the lab
        checkbox_state.append(self.others_ahs_checkBox.isChecked())
        data.append(self.others_ahs_checkBox.text())
        if self.others_ahs_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_ahs_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_ahs_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.others_ahs_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fifty-third test in the lab
        checkbox_state.append(self.others_others_1_checkBox.isChecked())
        data.append(self.others_others_1_lineEdit.text())
        if self.others_others_1_lineEdit_2.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_others_1_lineEdit_2.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_others_1_lineEdit_2.text() + " is not integer")
        if self.others_others_1_price_lineEdit.text() == "":
            price = 0
        else:
            price = int(self.others_others_1_price_lineEdit.text())
        data.append(int(price))

        # fifty-fourth test in the lab
        checkbox_state.append(self.others_others_2_checkBox.isChecked())
        data.append(self.others_others_2_lineEdit.text())
        if self.others_others_2_lineEdit_2.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.others_others_2_lineEdit_2.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.others_others_2_lineEdit_2.text() + " is not integer")
        if self.others_others_2_price_lineEdit.text() == "":
            price = 0
        else:
            price = int(self.others_others_2_price_lineEdit.text())
        data.append(int(price))

        # fifty-fifth test in the lab
        checkbox_state.append(self.bovin_blv_checkBox.isChecked())
        data.append(self.bovin_blv_checkBox.text())
        if self.bovin_blv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.bovin_blv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.bovin_blv_lineEdit.text() + " is not integer")
        price = re.findall("\(.*\)", self.bovin_blv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fifty-sixth test in the lab
        checkbox_state.append(self.bovin_fmdv_checkBox.isChecked())
        data.append(self.bovin_fmdv_checkBox.text())
        if self.bovin_fmdv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.bovin_fmdv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.bovin_fmdv_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.bovin_fmdv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fifty-seventh test in the lab
        checkbox_state.append(self.bovin_lsdv_checkBox.isChecked())
        data.append(self.bovin_lsdv_checkBox.text())
        if self.bovin_lsdv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.bovin_lsdv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.bovin_lsdv_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.bovin_lsdv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fifty-eighth test in the lab
        checkbox_state.append(self.bovin_bvd_checkBox.isChecked())
        data.append(self.bovin_bvd_checkBox.text())
        if self.bovin_bvd_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.bovin_bvd_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.bovin_bvd_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.bovin_bvd_checkBox.text())[0][1:-1]
        data.append(int(price))

        # fifty-ninth test in the lab
        checkbox_state.append(self.aquatic_animal_khv_checkBox.isChecked())
        data.append(self.aquatic_animal_khv_checkBox.text())
        if self.aquatic_animal_khv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.aquatic_animal_khv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.aquatic_animal_khv_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.aquatic_animal_khv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # sixtieth test in the lab
        checkbox_state.append(self.aquatic_animal_tilv_checkBox.isChecked())
        data.append(self.aquatic_animal_tilv_checkBox.text())
        if self.aquatic_animal_tilv_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.aquatic_animal_tilv_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.aquatic_animal_tilv_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.aquatic_animal_tilv_checkBox.text())[0][1:-1]
        data.append(int(price))

        # sixty-first test in the lab
        checkbox_state.append(self.aquatic_animal_cev_checkBox.isChecked())
        data.append(self.aquatic_animal_cev_checkBox.text())
        if self.aquatic_animal_cev_lineEdit.text() == "":
            data.append(0)
        else:
            try:
                data.append(int(self.aquatic_animal_cev_lineEdit.text()))
            except ValueError:
                error_message.append(
                    "value in " + self.aquatic_animal_cev_lineEdit.text() + " is not integer")
        price = re.findall(
            "\(.*\)", self.aquatic_animal_cev_checkBox.text())[0][1:-1]
        data.append(int(price))

        # special request
        data.append(self.laboratory_cpcr_checkBox.isChecked())
        data.append(self.laboratory_pcr_checkBox.isChecked())
        data.append(self.laboratory_extraction_checkBox.isChecked())
        return data, error_message, checkbox_state

    def show_molecular_biology_page(self):
        """Show the molecular biology page."""
        self.stackedWidget.setCurrentIndex(12)

    def show_bacteria_biology_page(self):
        """Show the bacteria biology page."""
        self.stackedWidget.setCurrentIndex(13)

    def show_parasite_biology_page(self):
        """Show the parasite biology page."""
        self.stackedWidget.setCurrentIndex(14)

    def show_current_user_information(self, user_info):
        """Show the current user information."""
        self.current_user_label.setText(user_info)

    def add_data_to_listview_printerpage(self, data):
        """Add data to listview in printer page."""
        self.sticker_search_treeWidget.clear()
        for row in data:
            QTreeWidgetItem(self.sticker_search_treeWidget, row)

    def clear_new_customer_information(self):
        """Clear new customer information in customer register page."""
        self.new_customer_title_entry.clear()
        self.new_customer_name_entry.clear()
        self.new_customer_surname_entry.clear()
        self.new_customer_tax_entry.clear()
        self.new_customer_email_entry.clear()
        self.new_customer_line_entry.clear()
        self.new_customer_phone_entry.clear()
        self.new_customer_address_entry.clear()
        self.new_customer_address_for_bill_entry.clear()

    def clear_current_user_information(self):
        """Clear current user information."""
        self.current_user_label.clear()

    def add_customer_info_new_case(self, data):
        """Add customer information to new case page."""
        self.new_case_search_tree_view.clear()
        for row in data:
            QTreeWidgetItem(self.new_case_search_tree_view, row)

    def reset_widgets_in_job_register_page(self):
        # clear data in search tree view
        self.new_case_search_tree_view.clear()
        self.new_case_search_name_entry.setText("")

        # enable entry name and tree view
        self.new_case_search_name_entry.setEnabled(True)
        self.new_case_search_tree_view.setEnabled(True)

        # clear case number entry
        self.new_case_number_job_entry.setText("")

        # enable search button
        self.new_case_search_button.setEnabled(True)

        # disable sender and owner information
        self.new_case_name_sender_entry.setEnabled(False)
        self.new_case_surename_sender_entry.setEnabled(False)
        self.new_case_tax_sender_entry.setEnabled(False)
        self.new_case_name_owner_entry.setEnabled(False)
        self.new_case_surename_owner_entry.setEnabled(False)
        self.new_case_tax_owner_entry.setEnabled(False)

        # clear sender and owner information
        self.new_case_name_sender_entry.clear()
        self.new_case_surename_sender_entry.clear()
        self.new_case_tax_sender_entry.clear()
        self.new_case_name_owner_entry.clear()
        self.new_case_surename_owner_entry.clear()
        self.new_case_tax_owner_entry.clear()

        # enable project name entry
        self.new_case_name_project_entry.setEnabled(True)
        self.new_case_name_project_entry.clear()

        # enable buttons
        self.new_case_select_owner_button.setEnabled(True)
        self.new_case_select_sender_button.setEnabled(True)
        self.new_case_anonymous_owner_button.setEnabled(True)
        self.new_case_save_button.setEnabled(True)

        # disable add lab button
        self.new_case_add_data_specimen_button.setEnabled(
            False)
        self.new_case_delete_data_specimen_button.setEnabled(
            False)
        self.new_case_print_sticker_button.setEnabled(False)
        self.new_case_print_lab_report_button.setEnabled(False)

    def show_add_data_specimen_page(self):
        """Show the add data specimen page."""
        pass

    def clear_specimen_information(self):
        """Clear specimen information."""
        self.specimen_page_name_animal_entry.clear()
        self.specimen_page_number_id_opd_entry.clear()
        self.specimen_page_year_animal_entry.clear()
        self.specimen_page_month_animal_entry.clear()
        self.specimen_page_day_animal_entry.clear()
        self.another_type_animal_entry.clear()

        self.swine_radioButton.setChecked(True)
        self.specimen_page_normal_radioButton.setChecked(True)
        self.specimen_page_chill_specimen_radioButton.setChecked(True)

        self.specimen_page_record_heal_textEdit.clear()

    def enable_lab_buttons(self):
        """Enable lab buttons."""
        self.specimen_page_Fungal_pushButton.setEnabled(True)
        self.specimen_page_Serology_pushButton.setEnabled(True)
        self.specimen_page_water_quality_pushButton.setEnabled(True)
        self.specimen_page_Immunohistochemistry_pushButton.setEnabled(True)
        self.specimen_page_Necropsy_pushButton.setEnabled(True)
        self.specimen_page_histopathology_research_recut_pushButton.setEnabled(
            True)

        self.specimen_page_Microbiology_pushButton.setEnabled(True)
        self.specimen_page_Parasitology_pushButton.setEnabled(True)
        self.specimen_page_molecular_pushButton.setEnabled(True)
        self.specimen_page_surgical_pushButton.setEnabled(True)
        self.specimen_page_cytology_pushButton.setEnabled(True)
        self.specimen_page_histopathology_research_pushButton.setEnabled(True)

        self.virology_pushButton.setEnabled(True)
        self.specimen_page_feed_analysis_pushButton.setEnabled(True)
        self.specimen_page_hematology_pushButton.setEnabled(True)
        self.specimen_page_histopatology_pushButton.setEnabled(True)
        self.specimen_page_food_safty_pushButton.setEnabled(True)

    def disable_lab_buttons(self):
        """Disable lab buttons."""
        self.specimen_page_Fungal_pushButton.setEnabled(False)
        self.specimen_page_Serology_pushButton.setEnabled(False)
        self.specimen_page_water_quality_pushButton.setEnabled(False)
        self.specimen_page_Immunohistochemistry_pushButton.setEnabled(False)
        self.specimen_page_Necropsy_pushButton.setEnabled(False)
        self.specimen_page_histopathology_research_recut_pushButton.setEnabled(
            False)

        self.specimen_page_Microbiology_pushButton.setEnabled(False)
        self.specimen_page_Parasitology_pushButton.setEnabled(False)
        self.specimen_page_molecular_pushButton.setEnabled(False)
        self.specimen_page_surgical_pushButton.setEnabled(False)
        self.specimen_page_cytology_pushButton.setEnabled(False)
        self.specimen_page_histopathology_research_pushButton.setEnabled(False)

        self.virology_pushButton.setEnabled(False)
        self.specimen_page_feed_analysis_pushButton.setEnabled(False)
        self.specimen_page_hematology_pushButton.setEnabled(False)
        self.specimen_page_histopatology_pushButton.setEnabled(False)
        self.specimen_page_food_safty_pushButton.setEnabled(False)


if __name__ == '__main__':
    pass
