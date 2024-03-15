from views.main_app_view import Ui_main_app_view
from PySide6.QtWidgets import QMainWindow


class MainAppView(QMainWindow, Ui_main_app_view):
    """"Main application view. Inherits from QMainWindow and Ui_main_app_view."""

    def __init__(self):
        super(MainAppView, self).__init__()
        self.setupUi(self)

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
        pass

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

    # ==================== job register page =====================
    def show_job_register_page(self):
        """Show the job register page."""
        self.stackedWidget.setCurrentIndex(2)
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


if __name__ == '__main__':
    pass
