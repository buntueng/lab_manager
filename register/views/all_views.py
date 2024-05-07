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

        # set treewidget column width
        self.new_case_search_tree_view.setColumnWidth(0, 300)
        self.new_case_search_tree_view.setColumnWidth(1, 300)

        # set treewidget column width
        self.barcode_page_customertreeWidget.setColumnWidth(0, 300)
        self.barcode_page_customertreeWidget.setColumnWidth(1, 300)

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

    def back_to_specimen_page(self):
        """Back to the specimen page."""
        self.stackedWidget.setCurrentIndex(3)

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
        self.enable_widgets_in_specimen_page()
        self.specimen_page_save_pushButton.setEnabled(True)
        self.disable_lab_buttons()

    def reload_specimen_page(self):
        """Reload the specimen page."""
        self.stackedWidget.setCurrentIndex(3)
    # ==================== update page ====================

    def show_update_page(self):
        """Show the update page."""
        self.stackedWidget.setCurrentIndex(11)
    # ==================== Molecular biology page ====================

    def show_Microbiology_page(self):
        """Show the Molecular biology page."""
        self.stackedWidget.setCurrentIndex(13)
    # =======================================================

    def reload_new_job_page(self):
        """Reload the new job page."""
        self.stackedWidget.setCurrentIndex(2)

    def show_Parasitology_page(self):
        """Show the Parasitology page."""
        self.stackedWidget.setCurrentIndex(14)

    def get_parasite_data(self) -> list:
        data_list = []
        checkbox_state = []

        data_list.append(self.PCV_checkBox.text())
        price = re.findall("\(.*\)", self.PCV_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.PCV_checkBox.isChecked())

        data_list.append(self.Floatation_checkBox.text())
        price = re.findall("\(.*\)", self.Floatation_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.Floatation_checkBox.isChecked())

        data_list.append(self.Parasite_in_meat_checkBox.text())
        price = re.findall(
            "\(.*\)", self.Parasite_in_meat_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.Parasite_in_meat_checkBox.isChecked())

        data_list.append(self.Parasite_iden_checkBox.text())
        price = re.findall(
            "\(.*\)", self.Parasite_iden_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.Parasite_iden_checkBox.isChecked())

        data_list.append(self.Floatation_for_dog_checkBox.text())
        price = re.findall(
            "\(.*\)", self.Floatation_for_dog_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.Floatation_for_dog_checkBox.isChecked())

        data_list.append(self.Stained_blood_smear_checkBox.text())
        price = re.findall(
            "\(.*\)", self.Stained_blood_smear_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.Stained_blood_smear_checkBox.isChecked())

        data_list.append(self.Centrifugal_checkBox.text())
        price = re.findall(
            "\(.*\)", self.Centrifugal_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.Centrifugal_checkBox.isChecked())

        data_list.append(self.Floatation_centrifugal_checkBox.text())
        price = re.findall(
            "\(.*\)", self.Floatation_centrifugal_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.Floatation_centrifugal_checkBox.isChecked())

        data_list.append(self.Stained_checkBox.text())
        price = re.findall(
            "\(.*\)", self.Stained_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.Stained_checkBox.isChecked())

        data_list.append(self.Sedimentation_checkBox.text())
        price = re.findall(
            "\(.*\)", self.Sedimentation_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.Sedimentation_checkBox.isChecked())

        data_list.append(self.woo_s_checkBox.text())
        price = re.findall(
            "\(.*\)", self.woo_s_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.woo_s_checkBox.isChecked())

        data_list.append(self.MC_master_checkBox.text())
        price = re.findall(
            "\(.*\)", self.MC_master_checkBox.text())[0][1:-1]
        data_list.append(int(price))
        checkbox_state.append(self.MC_master_checkBox.isChecked())

        return data_list, checkbox_state

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
        """Reset widgets in job register page."""
        # clear data in search tree view
        self.new_case_search_tree_view.clear()
        self.new_case_search_name_entry.setText("")

        # enable entry name and tree view
        self.new_case_search_name_entry.setEnabled(True)
        self.new_case_search_tree_view.setEnabled(True)

        # clear case number entry
        self.new_case_number_job_entry.setEnabled(False)
        self.new_case_number_job_entry.clear()

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

        self.new_case_detail_case_tree_view.clear()

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

    def get_bacteria_lab_data(self):
        sample_preparation = []
        preparation_name = []
        preparation_amount = []
        sample_preparation.append(self.swab_LT_checkBox.isChecked())
        preparation_name.append(self.swab_LT_checkBox.text())
        if self.swab_LT_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.swab_LT_lineEdit.text())

        sample_preparation.append(self.swab_RT_checkBox.isChecked())
        preparation_name.append(self.swab_RT_checkBox.text())
        if self.swab_RT_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.swab_RT_lineEdit.text())

        sample_preparation.append(self.wound_checkBox.isChecked())
        preparation_name.append(self.wound_checkBox.text())
        if self.wound_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.wound_lineEdit.text())

        sample_preparation.append(self.Aspirate_LT_checkBox.isChecked())
        preparation_name.append(self.Aspirate_LT_checkBox.text())
        if self.Aspirate_LT_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.Aspirate_LT_lineEdit.text())

        sample_preparation.append(self.Aspirate_RT_checkBox.isChecked())
        preparation_name.append(self.Aspirate_RT_checkBox.text())
        if self.Aspirate_RT_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.Aspirate_RT_lineEdit.text())

        sample_preparation.append(self.urine_checkBox.isChecked())
        preparation_name.append(self.urine_checkBox.text())
        if self.urine_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.urine_lineEdit.text())

        sample_preparation.append(self.Midstream_checkBox.isChecked())
        preparation_name.append(self.Midstream_checkBox.text())
        if self.Midstream_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.Midstream_lineEdit.text())

        sample_preparation.append(self.Catheterization_checkBox.isChecked())
        preparation_name.append(self.Catheterization_checkBox.text())
        if self.Catheterization_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.Catheterization_lineEdit.text())

        sample_preparation.append(self.Cystocentesis_checkBox.isChecked())
        preparation_name.append(self.Cystocentesis_checkBox.text())
        if self.Cystocentesis_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.Cystocentesis_lineEdit.text())

        sample_preparation.append(self.Tissues_LT_checkBox.isChecked())
        preparation_name.append(self.Tissues_LT_checkBox.text())
        if self.Tissues_LT_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.Tissues_LT_lineEdit.text())

        sample_preparation.append(self.Tissues_RT_checkBox.isChecked())
        preparation_name.append(self.Tissues_RT_checkBox.text())
        if self.Tissues_RT_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.Tissues_RT_lineEdit.text())

        sample_preparation.append(self.biopsy_LT_checkBox.isChecked())
        preparation_name.append(self.biopsy_LT_checkBox.text())
        if self.biopsy_LT_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.biopsy_LT_lineEdit.text())

        sample_preparation.append(self.biopsy_RT_checkBox.isChecked())
        preparation_name.append(self.biopsy_RT_checkBox.text())
        if self.biopsy_RT_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.biopsy_RT_lineEdit.text())

        sample_preparation.append(self.body_fluid_LT_checkBox.isChecked())
        preparation_name.append(self.body_fluid_LT_checkBox.text())
        if self.body_fluid_LT_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.body_fluid_LT_lineEdit.text())

        sample_preparation.append(self.body_fluid_RT_checkBox.isChecked())
        preparation_name.append(self.body_fluid_RT_checkBox.text())
        if self.body_fluid_RT_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.body_fluid_RT_lineEdit.text())

        sample_preparation.append(self.csf_checkBox.isChecked())
        preparation_name.append(self.csf_checkBox.text())
        if self.csf_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.csf_lineEdit.text())

        sample_preparation.append(self.feces_checkBox.isChecked())
        preparation_name.append(self.feces_checkBox.text())
        if self.feces_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.feces_lineEdit.text())

        sample_preparation.append(self.PUS_checkBox.isChecked())
        preparation_name.append(self.PUS_checkBox.text())
        if self.PUS_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.PUS_lineEdit.text())

        sample_preparation.append(self.Blood_checkBox.isChecked())
        preparation_name.append(self.Blood_checkBox.text())
        if self.Blood_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.Blood_lineEdit.text())

        sample_preparation.append(self.Blood_agar_checkBox.isChecked())
        preparation_name.append(self.Blood_agar_checkBox.text())
        if self.Blood_agar_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.Blood_agar_lineEdit.text())

        sample_preparation.append(self.Skin_scraping_checkBox.isChecked())
        preparation_name.append(self.Skin_scraping_checkBox.text())
        if self.Skin_scraping_lineEdit.text() == "":
            preparation_amount.append(0)
        else:
            preparation_amount.append(self.Skin_scraping_lineEdit.text())

        drug_sensitivity_status = []
        drug_sensitivity_name = []

        drug_sensitivity_status.append(self.amikacin_AK_checkBox.isChecked())
        drug_sensitivity_name.append(self.amikacin_AK_checkBox.text())

        drug_sensitivity_status.append(
            self.Ampicillin_AMP_checkBox.isChecked())
        drug_sensitivity_name.append(self.Ampicillin_AMP_checkBox.text())

        drug_sensitivity_status.append(
            self.Ceftazidime_CAZ_checkBox.isChecked())
        drug_sensitivity_name.append(self.Ceftazidime_CAZ_checkBox.text())

        drug_sensitivity_status.append(self.Cephalexin_CL_checkBox.isChecked())
        drug_sensitivity_name.append(self.Cephalexin_CL_checkBox.text())

        drug_sensitivity_status.append(
            self.Chloramphenicol_C_checkBox.isChecked())
        drug_sensitivity_name.append(self.Chloramphenicol_C_checkBox.text())

        drug_sensitivity_status.append(
            self.Cloxacillin_OB_checkBox.isChecked())
        drug_sensitivity_name.append(self.Cloxacillin_OB_checkBox.text())

        drug_sensitivity_status.append(
            self.Enrofloxacin_ENR_checkBox.isChecked())
        drug_sensitivity_name.append(self.Enrofloxacin_ENR_checkBox.text())

        drug_sensitivity_status.append(self.Gentamycin_CN_checkBox.isChecked())
        drug_sensitivity_name.append(self.Gentamycin_CN_checkBox.text())

        drug_sensitivity_status.append(self.Lincomycin_MY_checkBox.isChecked())
        drug_sensitivity_name.append(self.Lincomycin_MY_checkBox.text())

        drug_sensitivity_status.append(
            self.Norfloxacin_NOR_checkBox.isChecked())
        drug_sensitivity_name.append(self.Norfloxacin_NOR_checkBox.text())

        drug_sensitivity_status.append(self.Oxacillin_OX_checkBox.isChecked())
        drug_sensitivity_name.append(self.Oxacillin_OX_checkBox.text())

        drug_sensitivity_status.append(
            self.PolymyxcinB_PB_checkBox.isChecked())
        drug_sensitivity_name.append(self.PolymyxcinB_PB_checkBox.text())

        drug_sensitivity_status.append(
            self.Sulfa_trimetroprom_STX_checkBox.isChecked())
        drug_sensitivity_name.append(
            self.Sulfa_trimetroprom_STX_checkBox.text())

        drug_sensitivity_status.append(self.Vancomycin_VA_checkBox.isChecked())
        drug_sensitivity_name.append(self.Vancomycin_VA_checkBox.text())

        drug_sensitivity_status.append(
            self.Amoxycillin_AML_checkBox.isChecked())
        drug_sensitivity_name.append(self.Amoxycillin_AML_checkBox.text())

        drug_sensitivity_status.append(self.Bactracin_B_checkBox.isChecked())
        drug_sensitivity_name.append(self.Bactracin_B_checkBox.text())

        drug_sensitivity_status.append(self.Ceftiofur_EFT_checkBox.isChecked())
        drug_sensitivity_name.append(self.Ceftiofur_EFT_checkBox.text())

        drug_sensitivity_status.append(
            self.Cephalothin_KF_checkBox.isChecked())
        drug_sensitivity_name.append(self.Cephalothin_KF_checkBox.text())

        drug_sensitivity_status.append(
            self.Ciprofloxacin_CIP_checkBox.isChecked())
        drug_sensitivity_name.append(self.Ciprofloxacin_CIP_checkBox.text())

        drug_sensitivity_status.append(self.Colistin_CT_checkBox.isChecked())
        drug_sensitivity_name.append(self.Colistin_CT_checkBox.text())

        drug_sensitivity_status.append(
            self.Erythromycin_E_checkBox.isChecked())
        drug_sensitivity_name.append(self.Erythromycin_E_checkBox.text())

        drug_sensitivity_status.append(self.Imipenem_IPM_checkBox.isChecked())
        drug_sensitivity_name.append(self.Imipenem_IPM_checkBox.text())

        drug_sensitivity_status.append(self.Neomycin_N_checkBox.isChecked())
        drug_sensitivity_name.append(self.Neomycin_N_checkBox.text())

        drug_sensitivity_status.append(self.Novobiocin_NV_checkBox.isChecked())
        drug_sensitivity_name.append(self.Novobiocin_NV_checkBox.text())

        drug_sensitivity_status.append(
            self.Oxytetracycline_OT_checkBox.isChecked())
        drug_sensitivity_name.append(self.Oxytetracycline_OT_checkBox.text())

        drug_sensitivity_status.append(self.Rifampicin_RD_checkBox.isChecked())
        drug_sensitivity_name.append(self.Rifampicin_RD_checkBox.text())

        drug_sensitivity_status.append(
            self.Tetracycline_TE_checkBox.isChecked())
        drug_sensitivity_name.append(self.Tetracycline_TE_checkBox.text())

        drug_sensitivity_status.append(self.others_checkBox.isChecked())
        drug_sensitivity_name.append(self.bacteria_page_others_lineEdit.text())

        drug_sensitivity_status.append(self.Amoxy_AMC_checkBox.isChecked())
        drug_sensitivity_name.append(self.Amoxy_AMC_checkBox.text())

        drug_sensitivity_status.append(self.Clav_AMC_checkBox.isChecked())
        drug_sensitivity_name.append(self.Clav_AMC_checkBox.text())

        drug_sensitivity_status.append(
            self.Ceftriaxone_cro_checkBox.isChecked())
        drug_sensitivity_name.append(self.Ceftriaxone_cro_checkBox.text())

        drug_sensitivity_status.append(self.Cephazolin_KZ_checkBox.isChecked())
        drug_sensitivity_name.append(self.Cephazolin_KZ_checkBox.text())

        drug_sensitivity_status.append(
            self.Clindamicin_DA_checkBox.isChecked())
        drug_sensitivity_name.append(self.Clindamicin_DA_checkBox.text())

        drug_sensitivity_status.append(
            self.Doxycycline_DO_checkBox.isChecked())
        drug_sensitivity_name.append(self.Doxycycline_DO_checkBox.text())

        drug_sensitivity_status.append(
            self.Fosfomycin_FOS_checkBox.isChecked())
        drug_sensitivity_name.append(self.Fosfomycin_FOS_checkBox.text())

        drug_sensitivity_status.append(self.Kanamycin_K_checkBox.isChecked())
        drug_sensitivity_name.append(self.Kanamycin_K_checkBox.text())

        drug_sensitivity_status.append(
            self.Nitrofurantoin_F_checkBox.isChecked())
        drug_sensitivity_name.append(self.Nitrofurantoin_F_checkBox.text())

        drug_sensitivity_status.append(self.Optocin_OP_checkBox.isChecked())
        drug_sensitivity_name.append(self.Optocin_OP_checkBox.text())

        drug_sensitivity_status.append(self.PeniciliinG_P_checkBox.isChecked())
        drug_sensitivity_name.append(self.PeniciliinG_P_checkBox.text())

        drug_sensitivity_status.append(
            self.Streptomycin_S_checkBox.isChecked())
        drug_sensitivity_name.append(self.Streptomycin_S_checkBox.text())

        drug_sensitivity_status.append(
            self.Tobramycin_TOB_checkBox.isChecked())
        drug_sensitivity_name.append(self.Tobramycin_TOB_checkBox.text())

        bacteria_identification_name = []
        bacteria_identification_status = []

        bacteria_identification_status.append(
            self.Actinobacillus_checkBox.isChecked())
        bacteria_identification_name.append(
            self.Actinobacillus_checkBox.text())

        bacteria_identification_status.append(
            self.Corynebacterium_checkBox.isChecked())
        bacteria_identification_name.append(
            self.Corynebacterium_checkBox.text())

        bacteria_identification_status.append(
            self.Klebsiella_checkBox.isChecked())
        bacteria_identification_name.append(self.Klebsiella_checkBox.text())

        bacteria_identification_status.append(
            self.Streptococus_checkBox.isChecked())
        bacteria_identification_name.append(self.Streptococus_checkBox.text())

        bacteria_identification_status.append(
            self.Aeromonas_checkBox.isChecked())
        bacteria_identification_name.append(self.Aeromonas_checkBox.text())

        bacteria_identification_status.append(
            self.Enterobacter_checkBox.isChecked())
        bacteria_identification_name.append(self.Enterobacter_checkBox.text())

        bacteria_identification_status.append(
            self.Pasteurella_checkBox.isChecked())
        bacteria_identification_name.append(self.Pasteurella_checkBox.text())

        bacteria_identification_status.append(
            self.Staphylococcus_checkBox.isChecked())
        bacteria_identification_name.append(
            self.Staphylococcus_checkBox.text())

        bacteria_identification_status.append(
            self.Bordetella_checkBox.isChecked())
        bacteria_identification_name.append(self.Bordetella_checkBox.text())

        bacteria_identification_status.append(
            self.Escherichia_checkBox.isChecked())
        bacteria_identification_name.append(self.Escherichia_checkBox.text())

        bacteria_identification_status.append(
            self.Salmonella_checkBox.isChecked())
        bacteria_identification_name.append(self.Salmonella_checkBox.text())

        bacteria_identification_status.append(
            self.iden_others_checkBox.isChecked())
        bacteria_identification_name.append(
            self.bacterial_others_lineEdit.text())

        lab_request_name = []
        lab_request_status = []
        lab_request_price = []

        lab_request_status.append(self.Fungal_cul_checkBox.isChecked())
        lab_request_name.append(self.Fungal_cul_checkBox.text())
        price = re.findall(
            "\(.*\)", self.Fungal_cul_checkBox.text())[0][1:-1]
        lab_request_price.append(int(price))

        lab_request_status.append(self.Bacterial_iden_checkBox.isChecked())
        lab_request_name.append(self.Bacterial_iden_checkBox.text())
        price = re.findall(
            "\(.*\)", self.Bacterial_iden_checkBox.text())[0][1:-1]
        lab_request_price.append(int(price))

        lab_request_status.append(self.VITEK2_with_checkBox.isChecked())
        lab_request_name.append(self.VITEK2_with_checkBox.text())
        price = re.findall(
            "\(.*\)", self.VITEK2_with_checkBox.text())[0][1:-1]
        lab_request_price.append(int(price))

        lab_request_status.append(self.VITEK2_iden_checkBox.isChecked())
        lab_request_name.append(self.VITEK2_iden_checkBox.text())
        price = re.findall(
            "\(.*\)", self.VITEK2_iden_checkBox.text())[0][1:-1]
        lab_request_price.append(int(price))

        lab_request_status.append(self.MIC_checkBox.isChecked())
        lab_request_name.append(self.MIC_checkBox.text())
        price = re.findall(
            "\(.*\)", self.MIC_checkBox.text())[0][1:-1]
        lab_request_price.append(int(price))

        remark = self.bacteria_page_remark_textEdit.toPlainText()

        return sample_preparation, preparation_name, preparation_amount, drug_sensitivity_status, drug_sensitivity_name, bacteria_identification_name, bacteria_identification_status, lab_request_name, lab_request_status, lab_request_price, remark

    def disable_widgets_in_specimen_page(self):
        """Disable widgets in specimen page."""
        self.specimen_page_name_animal_entry.setEnabled(False)
        self.specimen_page_sex_animal_comboBox.setEnabled(False)
        self.specimen_page_cause_of_death_comboBox.setEnabled(False)
        self.specimen_page_number_id_opd_entry.setEnabled(False)
        self.specimen_page_year_animal_entry.setEnabled(False)
        self.specimen_page_month_animal_entry.setEnabled(False)
        self.specimen_page_day_animal_entry.setEnabled(False)
        self.specimen_page_unknow_age_animal_checkbox.setEnabled(False)
        self.swine_radioButton.setEnabled(False)
        self.avian_radioButton.setEnabled(False)
        self.bovine_radioButton.setEnabled(False)
        self.equine_radioButton.setEnabled(False)
        self.canine_radioButton.setEnabled(False)
        self.elephant_radioButton.setEnabled(False)
        self.feline_radioButton.setEnabled(False)
        self.another_radioButton.setEnabled(False)
        self.another_type_animal_entry.setEnabled(False)
        self.unknow_radioButton.setEnabled(False)
        self.specimen_page_normal_radioButton.setEnabled(False)
        self.specimen_page_most_argent_radioButton.setEnabled(False)
        self.specimen_page_breed_entry.setEnabled(False)
        self.specimen_page_weight_animal_entry.setEnabled(False)
        self.specimen_page_day_of_death_dateTime.setEnabled(False)
        self.specimen_page_day_keep_sample_dateTime.setEnabled(False)
        self.specimen_page_chill_specimen_radioButton.setEnabled(False)
        self.specimen_page_freeze_specimen_radioButton.setEnabled(False)
        self.specimen_page_room_temp_specimen_radioButton.setEnabled(False)
        self.specimen_page_record_heal_textEdit.setEnabled(False)
        self.specimen_page_save_pushButton.setEnabled(False)

    def enable_widgets_in_specimen_page(self):
        """Enable widgets in specimen page."""
        self.specimen_page_name_animal_entry.setEnabled(True)
        self.specimen_page_cause_of_death_comboBox.setEnabled(True)
        self.specimen_page_sex_animal_comboBox.setEnabled(True)
        self.specimen_page_number_id_opd_entry.setEnabled(True)
        self.specimen_page_year_animal_entry.setEnabled(True)
        self.specimen_page_month_animal_entry.setEnabled(True)
        self.specimen_page_day_animal_entry.setEnabled(True)
        self.specimen_page_unknow_age_animal_checkbox.setEnabled(True)
        self.swine_radioButton.setEnabled(True)
        self.avian_radioButton.setEnabled(True)
        self.bovine_radioButton.setEnabled(True)
        self.equine_radioButton.setEnabled(True)
        self.canine_radioButton.setEnabled(True)
        self.elephant_radioButton.setEnabled(True)
        self.feline_radioButton.setEnabled(True)
        self.another_radioButton.setEnabled(True)
        self.another_type_animal_entry.setEnabled(True)
        self.unknow_radioButton.setEnabled(True)
        self.specimen_page_normal_radioButton.setEnabled(True)
        self.specimen_page_most_argent_radioButton.setEnabled(True)
        self.specimen_page_breed_entry.setEnabled(True)
        self.specimen_page_weight_animal_entry.setEnabled(True)
        self.specimen_page_day_of_death_dateTime.setEnabled(True)
        self.specimen_page_day_keep_sample_dateTime.setEnabled(True)
        self.specimen_page_chill_specimen_radioButton.setEnabled(True)
        self.specimen_page_freeze_specimen_radioButton.setEnabled(True)
        self.specimen_page_room_temp_specimen_radioButton.setEnabled(True)
        self.specimen_page_record_heal_textEdit.setEnabled(True)
        self.specimen_page_save_pushButton.setEnabled(True)

    def add_customer_info_to_barcode_page(self, data):
        """Add customer information to barcode page."""
        self.barcode_page_customertreeWidget.clear()
        for row in data:
            QTreeWidgetItem(self.barcode_page_customertreeWidget, row)

    def reload_lab_order_detail_to_tree_view(self, data):
        """Reload lab order detail to tree view."""
        self.new_case_detail_case_tree_view.clear()
        for row in data:
            QTreeWidgetItem(self.new_case_detail_case_tree_view, row)

    def reset_print_barcode_page(self):
        """Reset print barcode page."""
        self.sticker_search_lineEdit.clear()
        self.barcode_page_customertreeWidget.clear()
        self.sticker_search_treeWidget.clear()

        self.today_sticker_search_pushButton.setEnabled(True)
        self.sticker_search_pushButton.setEnabled(True)
        self.print_barcode_pushButton.setEnabled(True)

    def clear_molecular_biology_page(self):
        """Clear molecular biology page."""
        self.avian_AI_1_checkBox.setChecked(False)
        self.avian_AI_1_lineEdit.clear()
        self.avian_AI_2_checkBox.setChecked(False)
        self.avian_AI_2_lineEdit.clear()
        self.avian_ibv_checkBox.setChecked(False)
        self.avian_ibdv_lineEdit.clear()
        self.avian_ibdv_checkBox.setChecked(False)
        self.avian_ibdv_lineEdit.clear()
        self.avian_ilt_checkBox.setChecked(False)
        self.avian_ilt_lineEdit.clear()
        self.avian_ndv_checkBox.setChecked(False)
        self.avian_ndv_lineEdit.clear()
        self.avian_ndv_2_checkBox.setChecked(False)
        self.avian_ndv_2_lineEdit.clear()
        self.avian_pdd_checkBox.setChecked(False)
        self.avian_pdd_lineEdit.clear()
        self.avian_pbfdv_checkBox.setChecked(False)
        self.avian_pbfdv_lineEdit.clear()
        self.avian_chlamydia_checkBox.setChecked(False)
        self.avian_chlamydia_lineEdit.clear()
        self.avian_pasteurella_checkBox.setChecked(False)
        self.avian_pasteurella_lineEdit.clear()
        self.avian_mg_checkBox.setChecked(False)
        self.avian_mg_lineEdit.clear()

        self.feline_felv_checkBox.setChecked(False)
        self.feline_felv_lineEdit.clear()
        self.feline_fip_checkBox.setChecked(False)
        self.feline_fip_lineEdit.clear()
        self.feline_fiv_checkBox.setChecked(False)
        self.feline_fiv_lineEdit.clear()
        self.feline_panleukopenia_checkBox.setChecked(False)
        self.feline_panleukopenia_lineEdit.clear()

        self.canine_cdv_checkBox.setChecked(False)
        self.canine_cdv_lineEdit.clear()
        self.canine_cpv_checkBox.setChecked(False)
        self.canine_cpv_lineEdit.clear()

        self.equine_ehv_checkBox.setChecked(False)
        self.equine_ehv_lineEdit.clear()
        self.equine_ahs_checkBox.setChecked(False)
        self.equine_ahs_lineEdit.clear()

        self.blood_1_ana_checkBox.setChecked(False)
        self.blood_1_ana_lineEdit.clear()
        self.blood_1_babe_checkBox.setChecked(False)
        self.blood_1_babe_lineEdit.clear()
        self.blood_1_ehr_checkBox.setChecked(False)
        self.blood_1_ehr_lineEdit.clear()
        self.blood_1_the_checkBox.setChecked(False)
        self.blood_1_the_lineEdit.clear()
        self.blood_1_haem_checkBox.setChecked(False)
        self.blood_1_haem_lineEdit.clear()
        self.blood_1_ecanis_checkBox.setChecked(False)
        self.blood_1_ecanis_lineEdit.clear()
        self.blood_1_leis_checkBox.setChecked(False)
        self.blood_1_leis_lineEdit.clear()
        self.blood_1_try_checkBox.setChecked(False)
        self.blood_1_try_lineEdit.clear()

        self.blood_2_asf_1_checkBox.setChecked(False)
        self.blood_2_asf_1_lineEdit.clear()
        self.blood_2_asf_2_checkBox.setChecked(False)
        self.blood_2_asf_2_lineEdit.clear()
        self.blood_2_asf_3_checkBox.setChecked(False)
        self.blood_2_asf_3_lineEdit.clear()
        self.blood_2_csf_checkBox.setChecked(False)
        self.blood_2_csf_lineEdit.clear()
        self.blood_2_hp_checkBox.setChecked(False)
        self.blood_2_hp_lineEdit.clear()
        self.blood_2_prrsv_checkBox.setChecked(False)
        self.blood_2_prrsv_lineEdit.clear()
        self.blood_2_pcv_checkBox.setChecked(False)
        self.blood_2_pcv_lineEdit.clear()
        self.blood_2_ped_checkBox.setChecked(False)
        self.blood_2_ped_lineEdit.clear()

        self.elephant_eehv1a_4_checkBox.setChecked(False)
        self.elephant_eehv1a_4_lineEdit.clear()
        self.elephant_eehv1a_1_checkBox.setChecked(False)
        self.elephant_eehv1a_1_lineEdit.clear()
        self.elephant_eehv1a_2_checkBox.setChecked(False)
        self.elephant_eehv1a_2_lineEdit.clear()
        self.elephant_eehv4_1_checkBox.setChecked(False)
        self.elephant_eehv4_1_lineEdit.clear()
        self.elephant_eehv4_2_checkBox.setChecked(False)
        self.elephant_eehv4_2_lineEdit.clear()

        self.others_bird_1_checkBox.setChecked(False)
        self.others_bird_1_lineEdit.clear()
        self.others_bird_2_checkBox.setChecked(False)
        self.others_bird_2_lineEdit.clear()
        self.others_clos_checkBox.setChecked(False)
        self.others_clos_lineEdit.clear()
        self.others_lep_checkBox.setChecked(False)
        self.others_lep_lineEdit.clear()
        self.others_toxo_checkBox.setChecked(False)
        self.others_toxo_lineEdit.clear()
        self.others_melio_checkBox.setChecked(False)
        self.others_melio_lineEdit.clear()
        self.others_myco_checkBox.setChecked(False)
        self.others_myco_lineEdit.clear()
        self.others_mavium_checkBox.setChecked(False)
        self.others_mavium_lineEdit.clear()
        self.others_mbovis_checkBox.setChecked(False)
        self.others_mbovis_lineEdit.clear()
        self.others_mtube_checkBox.setChecked(False)
        self.others_mtube_lineEdit.clear()
        self.others_ahs_checkBox.setChecked(False)
        self.others_ahs_lineEdit.clear()
        self.others_others_1_checkBox.setChecked(False)
        self.others_others_1_lineEdit_2.clear()
        self.others_others_1_lineEdit.clear()
        self.others_others_1_price_lineEdit.clear()
        self.others_others_2_checkBox.setChecked(False)
        self.others_others_2_lineEdit.clear()
        self.others_others_2_price_lineEdit.clear()
        self.others_others_2_lineEdit_2.clear()

        self.bovin_blv_checkBox.setChecked(False)
        self.bovin_blv_lineEdit.clear()
        self.bovin_fmdv_checkBox.setChecked(False)
        self.bovin_fmdv_lineEdit.clear()
        self.bovin_lsdv_checkBox.setChecked(False)
        self.bovin_lsdv_lineEdit.clear()
        self.bovin_bvd_checkBox.setChecked(False)
        self.bovin_bvd_lineEdit.clear()

        self.aquatic_animal_khv_checkBox.setChecked(False)
        self.aquatic_animal_khv_lineEdit.clear()
        self.aquatic_animal_tilv_checkBox.setChecked(False)
        self.aquatic_animal_tilv_lineEdit.clear()
        self.aquatic_animal_cev_checkBox.setChecked(False)
        self.aquatic_animal_cev_lineEdit.clear()

        self.laboratory_cpcr_checkBox.setChecked(False)
        self.laboratory_pcr_checkBox.setChecked(False)
        self.laboratory_extraction_checkBox.setChecked(False)

        self.number_item_lineEdit.clear()
        self.cost_item_lineEdit.clear()


if __name__ == '__main__':
    pass
