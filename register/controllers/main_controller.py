""" Main Controller class"""
# import QMessageBox from PySide6.QtWidgets
from PySide6.QtWidgets import QMessageBox


class Main_Controller:
    """Main Controller class"""

    def __init__(self, main_model, main_view):
        self.model = main_model
        self.view = main_view

        self.event_bindings()

    def event_bindings(self):
        """Event bindings for the main view"""
        self.view.login_pushButton.clicked.connect(self.user_sign_in)
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
