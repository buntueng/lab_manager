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

    def bind_event_in_new_customer_page(self):
        """Bind event in new customer page"""
        self.view.save_new_customer_button.clicked.connect(
            self.save_new_customer)
        self.view.anonymous_tax_checkbox.stateChanged.connect(
            self.disable_tax_entry)
        self.view.new_customer_addres_for_bill_checkbox.stateChanged.connect(
            self.copy_address_to_bill_address)

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
