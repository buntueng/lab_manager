from views.main_app_view import Ui_main_app_view
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QTreeWidgetItem
# import QTreeWidgetItem


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
    # ==================== check job progress ======================

    def show_check_job_progress_page(self):
        """Show the check job progress page."""
        self.stackedWidget.setCurrentIndex(3)

    # ===================== employee page ========================
    def show_employee_page(self):
        """Show the employee page."""
        self.stackedWidget.setCurrentIndex(4)

    # ===================== check report page =====================
    def show_check_report_page(self):
        """Show the check report page."""
        self.stackedWidget.setCurrentIndex(5)

    # ========================= bill page ========================
    def show_bill_page(self):
        """Show the bill page."""
        self.stackedWidget.setCurrentIndex(6)

    # ====================== print barcode page ========================
    def show_print_barcode_page(self):
        """Show the print barcode page."""
        self.stackedWidget.setCurrentIndex(7)
    # ====================== lab report page =========================

    def show_lab_order_report_page(self):
        """Show the lab report page."""
        self.stackedWidget.setCurrentIndex(8)

    # ====================== personal information page ====================
    def show_personal_information_page(self):
        """Show the personal information page."""
        self.stackedWidget.setCurrentIndex(9)
    # ==================== update page ====================

    def show_update_page(self):
        """Show the update page."""
        self.stackedWidget.setCurrentIndex(10)

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

if __name__ == '__main__':
    pass
