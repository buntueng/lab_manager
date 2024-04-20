""" Main Controller class"""
# import QMessageBox from PySide6.QtWidgets
from typing import Any
import time
from PySide6.QtWidgets import QMessageBox
from models.barcode_generator import BarcodeGenerator


class Main_Controller:
    """Main Controller class"""

    def __init__(self, main_model, main_view):
        self.model = main_model
        self.view = main_view

        self.user_login_info = []

        self.event_bindings()

    def event_bindings(self):
        """Event bindings for the main view"""
        self.view.login_pushButton.clicked.connect(self.user_sign_in)
        # bind enter key in login page
        self.view.password_lineEdit.returnPressed.connect(self.user_sign_in)
        self.view.sign_out_pushButton.clicked.connect(self.user_sign_out)

        self.view.customer_reg_pushButton.clicked.connect(
            self.view.show_customer_register_page)
        self.view.case_register_pushButton.clicked.connect(
            self.view.show_job_register_page)
        self.view.check_job_pushButton.clicked.connect(
            self.view.show_check_job_progress_page)
        self.view.barcode_pushButton.clicked.connect(
            self.view.show_print_barcode_page)
        self.view.lab_order_pushButton.clicked.connect(
            self.view.show_lab_order_report_page)
        self.view.bill_pushButton.clicked.connect(self.view.show_bill_page)
        self.view.check_report_pushButton.clicked.connect(
            self.view.show_check_report_page)

        self.view.employee_pushButton.clicked.connect(
            self.view.show_employee_page)
        self.view.personal_info_pushButton.clicked.connect(
            self.view.show_personal_information_page)

        self.view.update_prog_pushButton.clicked.connect(
            self.view.show_update_page)

        self.view.sign_out_pushButton.clicked.connect(
            self.view.show_login_page)
        # ==================== print barcode page ====================
        self.view.print_barcode_pushButton.clicked.connect(
            self.print_barcode)
        self.view.sticker_search_pushButton.clicked.connect(
            self.search_sticker)
        self.view.today_sticker_search_pushButton.clicked.connect(
            self.search_today_sticker)

        self.bind_event_in_new_customer_page()
        self.bind_event_in_case_register_page()
        self.bind_event_in_specimen_page()

    def bind_event_in_new_customer_page(self):
        """Bind event in new customer page"""
        self.view.save_new_customer_button.clicked.connect(
            self.save_new_customer)
        self.view.anonymous_tax_checkbox.stateChanged.connect(
            self.disable_tax_entry)
        self.view.new_customer_addres_for_bill_checkbox.stateChanged.connect(
            self.copy_address_to_bill_address)

    def bind_event_in_case_register_page(self):
        """Bind event in case register page"""
        self.view.new_case_search_button.clicked.connect(
            self.new_case_search_user)
        # self.view.new_case_save_button.clicked.connect(
        # self.save_case_register)
        self.view.new_case_select_sender_button.clicked.connect(
            self.new_case_add_sender_info)
        self.view.new_case_select_owner_button.clicked.connect(
            self.new_case_add_owner_info)
        self.view.new_case_anonymous_owner_button.clicked.connect(
            self.clear_new_case_owner_info)
        self.view.new_case_save_button.clicked.connect(
            self.register_new_case)

        self.view.new_case_add_data_specimen_button.clicked.connect(
            self.view.show_specimen_page)

    def bind_event_in_specimen_page(self):
        """Bind event in specimen page"""
        self.view.specimen_page_save_pushButton.clicked.connect(
            self.save_specimen_information)
        self.view.specimen_page_back_pushButton.clicked.connect(
            self.view.backto_job_register_page)

    def save_specimen_information(self):
        """Save specimen information
        """
        # get data from the view
        specimen_data = []
        specimen_data.append(int(self.view.new_case_number_job_entry.text()))
        specimen_data.append(
            self.view.specimen_page_name_animal_entry.text())
        specimen_data.append(
            self.view.specimen_page_number_id_opd_entry.text())
        specimen_data.append(
            self.view.specimen_page_sex_animal_comboBox.currentText())
        specimen_data.append(self.view.specimen_page_year_animal_entry.text())
        specimen_data.append(self.view.specimen_page_month_animal_entry.text())
        specimen_data.append(self.view.specimen_page_day_animal_entry.text())
        specimen_data.append(
            self.view.specimen_page_cause_of_death_comboBox.currentText())
        species = ""
        if self.view.swine_radioButton.isChecked():
            species = self.view.swine_radioButton.text()
        elif self.view.avian_radioButton.isChecked():
            species = self.view.avian_radioButton.text()
        elif self.view.bovine_radioButton.isChecked():
            species = self.view.bovine_radioButton.text()
        elif self.view.equine_radioButton.isChecked():
            species = self.view.equine_radioButton.text()
        elif self.view.canine_radioButton.isChecked():
            species = self.view.canine_radioButton.text()
        elif self.view.feline_radioButton.isChecked():
            species = self.view.feline_radioButton.text()
        elif self.view.elephant_radioButton.isChecked():
            species = self.view.elephant_radioButton.text()
        elif self.view.another_radioButton.isChecked():
            species = self.view.another_type_animal_entry.text()
        elif self.view.unknow_radioButton.isChecked():
            species = self.view.unknow_radioButton.text()
        else:
            species = "Unknow"
        specimen_data.append(species)
        specimen_data.append(self.view.specimen_page_breed_entry.text())

        sample_type = ""
        if self.view.specimen_page_most_argent_radioButton.isChecked():
            sample_type = self.view.specimen_page_most_argent_radioButton.text()
        elif self.view.specimen_page_normal_radioButton.isChecked():
            sample_type = self.view.specimen_page_normal_radioButton.text()
        specimen_data.append(sample_type)

        specimen_data.append(
            self.view.specimen_page_weight_animal_entry.text())
        specimen_data.append(
            self.view.specimen_page_day_of_death_dateTime.text())
        specimen_data.append(
            self.view.specimen_page_day_keep_sample_dateTime.text())

        keep_method = ""
        if self.view.specimen_page_chill_specimen_radioButton.isChecked():
            keep_method = self.view.specimen_page_chill_specimen_radioButton.text()
        elif self.view.specimen_page_freeze_specimen_radioButton.isChecked():
            keep_method = self.view.specimen_page_freeze_specimen_radioButton.text()
        elif self.view.specimen_page_room_temp_specimen_radioButton.isChecked():
            keep_method = self.view.specimen_page_room_temp_specimen_radioButton.text()
        else:
            keep_method = "Unknow"
        specimen_data.append(keep_method)

        sample_test_speed = ""
        if self.view.specimen_page_normal_radioButton.isChecked():
            sample_test_speed = self.view.specimen_page_normal_radioButton.text()
        elif self.view.specimen_page_most_argent_radioButton.isChecked():
            sample_test_speed = self.view.specimen_page_most_argent_radioButton.text()
        else:
            sample_test_speed = "Unknow"
        specimen_data.append(sample_test_speed)

        specimen_data.append(
            self.view.specimen_page_record_heal_textEdit.toPlainText())

        specimen_data.append(int(self.user_login_info[0][1]))
        if self.model.save_specimen_information(specimen_data):
            QMessageBox.information(self.view, "Success",
                                    "บันทึกข้อมูลตัวอย่างเรียบร้อย")
            # disable save button
            self.view.specimen_page_save_pushButton.setEnabled(False)
            # clear all entry
            self.view.clear_specimen_information()
            self.view.enable_lab_buttons()
            # ==================== enable lab buttons ====================
        else:
            QMessageBox.critical(self.view, "Error",
                                 "ไม่สามารถบันทึกข้อมูลตัวอย่างได้")

    def register_new_case(self):
        """register new case to the database"""
        skip = False
        # check if case number is empty
        if self.view.new_case_number_job_entry.text() == "":
            QMessageBox.critical(self.view, "Error",
                                 "กรุณาบันทึกข้อมูลลูกค้าก่อน")
        else:
            # if project name is empty, show warning message to confirm
            if self.view.new_case_name_project_entry.text() == "":
                reply = QMessageBox.warning(self.view, "Warning",
                                            "ต้องการดำเนินการต่อโดยไม่บันทึกชื่อโครงการหรือไม่?",
                                            QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.No:
                    self.view.new_case_name_project_entry.setFocus()
                    skip = True
            if not skip:
                # disable all add button
                self.view.new_case_select_sender_button.setEnabled(False)
                self.view.new_case_select_owner_button.setEnabled(False)
                self.view.new_case_anonymous_owner_button.setEnabled(False)
                self.view.new_case_save_button.setEnabled(False)

                # get data from the view
                case_data = []
                case_data.append(self.view.new_case_number_job_entry.text())
                case_data.append(self.view.new_case_name_sender_entry.text())
                case_data.append(
                    self.view.new_case_surename_sender_entry.text())
                case_data.append(self.view.new_case_tax_sender_entry.text())
                case_data.append(self.view.new_case_name_owner_entry.text())
                case_data.append(
                    self.view.new_case_surename_owner_entry.text())
                case_data.append(self.view.new_case_tax_owner_entry.text())
                case_data.append(self.view.new_case_name_project_entry.text())
                if self.model.save_new_case_register(case_data, self.user_login_info[0][1]):
                    QMessageBox.information(self.view, "Success",
                                            "บันทึกข้อมูลเรียบร้อย")
                    # clear data in search tree view
                    self.view.new_case_search_tree_view.clear()
                    self.view.new_case_search_name_entry.setText("")

                    # disable entry name and tree view
                    self.view.new_case_search_name_entry.setEnabled(False)
                    self.view.new_case_search_tree_view.setEnabled(False)

                    # disable case number entry
                    self.view.new_case_number_job_entry.setEnabled(False)

                    # disable search button
                    self.view.new_case_search_button.setEnabled(False)

                    # disable sender and owner information
                    self.view.new_case_name_sender_entry.setEnabled(False)
                    self.view.new_case_surename_sender_entry.setEnabled(False)
                    self.view.new_case_tax_sender_entry.setEnabled(False)
                    self.view.new_case_name_owner_entry.setEnabled(False)
                    self.view.new_case_surename_owner_entry.setEnabled(False)
                    self.view.new_case_tax_owner_entry.setEnabled(False)
                    self.view.new_case_name_project_entry.setEnabled(False)

                    # enable add lab button
                    self.view.new_case_add_data_specimen_button.setEnabled(
                        True)
                    self.view.new_case_delete_data_specimen_button.setEnabled(
                        True)
                    self.view.new_case_print_sticker_button.setEnabled(True)
                    self.view.new_case_print_lab_report_button.setEnabled(True)

    def clear_new_case_owner_info(self) -> None:
        """Clear owner information in the case register page"""
        self.view.new_case_name_owner_entry.setText("")
        self.view.new_case_surename_owner_entry.setText("")
        self.view.new_case_tax_owner_entry.setText("")

    def new_case_add_owner_info(self):
        """Add owner information to the case register"""
        # if case number is empty, read the last case number from the database
        if self.view.new_case_number_job_entry.text() == "":
            last_case_number = self.model.get_last_case_number()
            last_case_number = int(last_case_number) + 1
            self.view.new_case_number_job_entry.setText(str(last_case_number))

        if self.view.new_case_search_tree_view.selectedItems() == []:
            QMessageBox.critical(self.view, "Error",
                                 "Please select a row to add owner information")
        else:
            selected_item = self.view.new_case_search_tree_view.selectedItems()
            if len(selected_item) > 1:
                QMessageBox.critical(self.view, "Error",
                                     "Please select only one row to add owner information")
            else:
                for row in selected_item:
                    self.view.new_case_name_owner_entry.setText(row.text(0))
                    self.view.new_case_surename_owner_entry.setText(
                        row.text(1))
                    self.view.new_case_tax_owner_entry.setText(row.text(2))

    def new_case_add_sender_info(self):
        """Add sender information to the case register"""
        # if case number is empty, read the last case number from the database
        if self.view.new_case_number_job_entry.text() == "":
            last_case_number = self.model.get_last_case_number()
            last_case_number = int(last_case_number) + 1
            self.view.new_case_number_job_entry.setText(str(last_case_number))

        if self.view.new_case_search_tree_view.selectedItems() == []:
            QMessageBox.critical(self.view, "Error",
                                 "Please select a row to add sender information")
        else:
            selected_item = self.view.new_case_search_tree_view.selectedItems()
            if len(selected_item) > 1:
                QMessageBox.critical(self.view, "Error",
                                     "Please select only one row to add sender information")
            else:
                for row in selected_item:
                    self.view.new_case_name_sender_entry.setText(row.text(0))
                    self.view.new_case_surename_sender_entry.setText(
                        row.text(1))
                    self.view.new_case_tax_sender_entry.setText(row.text(2))

    def new_case_search_user(self):
        """Search case register"""
        keyword_search = self.view.new_case_search_name_entry.text()
        if keyword_search == "":
            QMessageBox.critical(self.view, "Error",
                                 "กรุณาป้อนชื่อหรือนามสกุลของลูกค้า")
        else:
            customer_information = self.model.new_case_search_customer(
                keyword_search)
            if customer_information == []:
                QMessageBox.critical(self.view, "Error",
                                     "ไม่พบข้อมูลลูกค้า")
            else:
                self.view.add_customer_info_new_case(customer_information)

    def save_case_register(self):
        """Save case register"""
        # get selected item from the QTreeWidget
        selected_item = self.view.new_case_detail_case_tree_view.selectedItems()
        if selected_item == []:
            QMessageBox.critical(self.view, "Error",
                                 "Please select a row to save case register")
        else:
            if len(selected_item) > 1:
                QMessageBox.critical(self.view, "Error",
                                     "Please select only one row to save case register")
            else:
                # get data from the selected item
                row_list = []
                for row in selected_item:
                    column_list = []
                    for col in range(self.view.new_case_detail_case_tree_view.columnCount()):
                        column_list.append(row.text(col))
                    row_list.append(column_list)
                # get updater id from the user_login_info
                updater = self.user_login_info[0][1]
                # save data to the database
                if self.model.save_case_register(row_list, updater):
                    QMessageBox.information(self.view, "Success",
                                            "บันทึกข้อมูลลูกค้าเรียบร้อย")
                    self.view.clear_information()
                else:
                    QMessageBox.critical(self.view, "Error",
                                         "ไม่สามารถบันทึกข้อมูลลูกค้าได้")

    def disable_tax_entry(self, state: int) -> None:
        """Disable tax entry if the checkbox is checked"""
        if state == 2:
            self.view.new_customer_tax_entry.setEnabled(False)
            self.view.new_customer_tax_entry.clear()
        else:
            self.view.new_customer_tax_entry.setEnabled(True)

    def copy_address_to_bill_address(self, state: int) -> None:
        """Copy address to bill address"""
        if state == 2:
            self.view.new_customer_address_for_bill_entry.setPlainText(
                self.view.new_customer_address_entry.toPlainText())
        else:
            self.view.new_customer_address_for_bill_entry.clear()

    def save_new_customer(self) -> None:
        """Save new customer to the database"""
        # check all fields are filled
        if self.view.new_customer_title_entry.text() == "" or self.view.new_customer_name_entry.text() == "" or self.view.new_customer_surname_entry.text() == "" or self.view.new_customer_phone_entry.text() == "" or self.view.new_customer_email_entry.text() == "":
            message = "กรุณากรอกข้อมูล \n คำนำหน้าชื่อ \n ชื่อ \n สกุล \n เบอร์โทร \n และ email ให้ครบถ้วน"
            QMessageBox.critical(self.view, "Error", message)
        else:
            # get all data from the view
            group_id = 0
            if self.view.new_customer_private_radioBT.isChecked():
                group_id = 1
            elif self.view.new_customer_public_radioBT.isChecked():
                group_id = 2
            elif self.view.new_customer_internal_radioBT.isChecked():
                group_id = 3
            elif self.view.new_customer_professor_radioBT.isChecked():
                group_id = 4
            elif self.view.new_customer_student_radioBT.isChecked():
                group_id = 5

            title = self.view.new_customer_title_entry.text()
            name = self.view.new_customer_name_entry.text()
            surname = self.view.new_customer_surname_entry.text()
            tax_id = self.view.new_customer_tax_entry.text()
            email = self.view.new_customer_email_entry.text()
            line_id = self.view.new_customer_line_entry.text()
            phone = self.view.new_customer_phone_entry.text()
            # get data from qtexedit
            contact_address = self.view.new_customer_address_entry.toPlainText()
            bill_address = self.view.new_customer_address_for_bill_entry.toPlainText()
            # get updater id from the user_login_info
            updater = self.user_login_info[0][1]
            # save data to the database
            if self.model.save_new_customer(group_id, title, name, surname, tax_id,
                                            email, line_id, phone, contact_address, bill_address, updater):
                QMessageBox.information(self.view, "Success",
                                        "บันทึกข้อมูลลูกค้าเรียบร้อย")
                self.view.clear_new_customer_information()
            else:
                QMessageBox.critical(self.view, "Error",
                                     "ไม่สามารถบันทึกข้อมูลลูกค้าได้")

    def search_today_sticker(self):
        """ serach all case that registered today. Sorting the result by date and time"""
        # add data to listview
        data = self.model.search_today_sticker()
        self.add_customer_case_to_view(data)

    def search_sticker(self):
        """ serach customer name to get a sticker information"""
        keyword_search = self.view.sticker_search_lineEdit.text()
        if keyword_search == "":
            QMessageBox.critical(self.view, "Error",
                                 "กรุณาป้อนชื่อหรือนามสกุลของลูกค้า")
        else:
            customer_information = self.model.search_customer_case(
                keyword_search)
            if customer_information == []:
                QMessageBox.critical(self.view, "Error",
                                     "ไม่พบข้อมูลลูกค้า")
            else:
                self.add_customer_case_to_view(customer_information)

    def add_customer_case_to_view(self, data):
        """Add customer case to the view"""
        if data == None or data == []:
            QMessageBox.critical(self.view, "Error",
                                 "ไม่พบข้อมูลลูกค้า")
            self.view.sticker_search_lineEdit.clear()

        else:
            sticker_list = []
            for item in data:
                # reformat the date and time
                lab_name = item[6] + "(" + item[5] + ")"
                # barcode number format is "yy" + barcode_number where the barcode_number is 10 digits.
                barcode_number = time.strftime(
                    "%Y", time.localtime())[-2:] + str(item[1]).zfill(10)

                # barcode_number = + str(item[1])
                reformat_data = [item[0].strftime(
                    "%d-%m-%Y %H:%M:%S"), barcode_number, item[2], lab_name, item[3], item[4], "Comments"]
                sticker_list.append(reformat_data)
            self.view.add_data_to_listview_printerpage(sticker_list)

    def print_barcode(self):
        """Print a selected information to barcode """
        # get selected item from the QTreeWidget
        selected_item = self.view.sticker_search_treeWidget.selectedItems()
        if selected_item == []:
            QMessageBox.critical(self.view, "Error",
                                 "Please select a row to print barcode")
        else:
            if len(selected_item) > 1:
                QMessageBox.critical(self.view, "Error",
                                     "Please select only one row to print barcode")
            else:
                barcode_obj = BarcodeGenerator()
                row_list = []
                for row in selected_item:
                    column_list = []
                    for col in range(self.view.sticker_search_treeWidget.columnCount()):
                        column_list.append(row.text(col))
                    row_list.append(column_list)
                barcode_obj.generate(row_list)
                barcode_obj.print_barcode()

        # generate barcode

    def user_sign_in(self):
        """User sign in method"""
        # get username and password from the view
        username = self.view.username_lineEdit.text()
        password = self.view.password_lineEdit.text()

        # if username and password are not empty
        if username != "" and password != "":
            self.view.clear_user_and_password()
            login_info = self.model.user_sign_in(username, password)
            if login_info:
                self.user_login_info = login_info
                current_name = login_info[0][3] + " " + \
                    login_info[0][4] + " " + login_info[0][5]
                self.view.show_current_user_information(current_name)
                self.view.enable_all_buttons()
                self.view.show_customer_register_page()

        elif username == "" and password != "":
            self.view.username_lineEdit.setFocus()
            QMessageBox.critical(self.view, "Error",
                                 "Username cannot be empty")
            # show message
        elif username != "" and password == "":
            self.view.password_lineEdit.setFocus()
            # show message
            QMessageBox.critical(self.view, "Error",
                                 "Password cannot be empty")
        else:
            self.view.username_lineEdit.setFocus()
            # show message
            QMessageBox.critical(self.view, "Error",
                                 "Username and Password cannot be empty")

    def user_sign_out(self):
        """User sign out method"""
        self.view.clear_user_and_password()
        self.view.clear_information()
        self.user_login_info = []
        # disable all buttons
        self.view.disable_all_buttons()
        self.view.show_login_page()
        # clear user information on top right corner
        self.view.clear_current_user_information()
