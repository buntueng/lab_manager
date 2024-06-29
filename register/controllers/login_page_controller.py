""" This module contains the controller for the login page. """
from PySide6.QtWidgets import QMessageBox
from models.login_page_model import user_sign_in
from views.login_page_view import clear_user_and_password

def login_page_event_bindings(controller):
    controller.view.login_pushButton.clicked.connect(lambda: signin_button_pressed(controller))
    controller.view.password_lineEdit.returnPressed.connect(lambda: signin_button_pressed(controller))
    controller.view.sign_out_pushButton.clicked.connect(lambda: user_sign_out(controller))
    
    
def signin_button_pressed(controller):
    """User sign in method"""
    # get username and password from the view
    username = controller.view.username_lineEdit.text()
    password = controller.view.password_lineEdit.text()

    # if username and password are not empty
    if username != "" and password != "":
        clear_user_and_password(controller.view)
        login_info = user_sign_in(controller.model,username, password)
        if login_info:
            controller.user_login_info = login_info
            current_name = login_info[0][3] + " " + \
                login_info[0][4] + " " + login_info[0][5]
            controller.view.show_current_user_information(current_name)
            controller.view.enable_all_buttons()
            controller.all_customer_names = controller.model.get_all_customer_names()
            controller.view.show_job_register_page()

    elif username == "" and password != "":
        controller.view.username_lineEdit.setFocus()
        QMessageBox.critical(controller.view, "Error",
                                "Username cannot be empty")
        # show message
    elif username != "" and password == "":
        controller.view.password_lineEdit.setFocus()
        # show message
        QMessageBox.critical(controller.view, "Error",
                                "Password cannot be empty")
    else:
        controller.view.username_lineEdit.setFocus()
        # show message
        QMessageBox.critical(controller.view, "Error",
                                "Username and Password cannot be empty")

def user_sign_out(controller):
    """User sign out method"""
    clear_user_and_password(controller.view)
    controller.view.clear_information()
    controller.user_login_info = []
    # disable all buttons
    controller.view.disable_all_buttons()
    controller.view.show_login_page()
    # clear user information on top right corner
    controller.view.clear_current_user_information()