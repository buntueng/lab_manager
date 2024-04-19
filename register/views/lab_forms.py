"""Create other forms for the lab app."""
from views.F1_molecular_biology import Ui_MainWindow as Ui_molecular_biology
from views.F2_bacterie_biology import Ui_BACTERIE as Ui_bacterie_biology
from views.F3_parasite_biology import Ui_UI_parasite as Ui_parasite_biology

from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QFileDialog


class Molecular_Biology_Form(QWidget, Ui_molecular_biology):
    """Lab forms class. Inherits from QWidget, Ui_molecular_biology."""

    def __init__(self):
        super(Molecular_Biology_Form, self).__init__()
        self.setupUi(self)

    def show(self):
        """Show the molecular biology form."""
        self.show()

    def hide(self):
        """Hide the form."""
        self.hide()


class Bacterie_Biology_Form:
    """Lab forms class. Inherits from QWidget, Ui_bacterie_biology."""

    def __init__(self):
        super(Bacterie_Biology_Form, self).__init__()
        self.setupUi(self)

    def show(self):
        """Show the molecular biology form."""
        self.show()

    def hide(self):
        """Hide the form."""
        self.hide()


class Parasite_Biology_Form:
    """Lab forms class. Inherits from QWidget, Ui_parasite_biology."""

    def __init__(self):
        super(Parasite_Biology_Form, self).__init__()
        self.setupUi(self)

    def show(self):
        """Show the molecular biology form."""
        self.show()

    def hide(self):
        """Hide the form."""
        self.hide()
