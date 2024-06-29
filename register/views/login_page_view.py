"""This module contains the LoginPageView class."""
def clear_user_and_password(view):
    """Clear username and password in login page."""
    view.username_lineEdit.clear()
    view.password_lineEdit.clear()