import os
import sys
from updater import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow


class MainUpdater(QMainWindow, Ui_MainWindow):
    """Main window for the updater application."""

    def __init__(self):
        super(MainUpdater, self).__init__()
        self.setupUi(self)
        self.reser_progress()
        self.show()

    def reser_progress(self):
        """Reset the progress bar to 0."""
        self.progressBar.setValue(0)

    def update_progress(self, value):
        """Update the progress bar to the given value."""
        self.progressBar.setValue(value)


if __name__ == "__main__":
    app = QApplication([])
    window = MainUpdater()
    app.exec()
