import os
import sys
import logging.config
from PySide6.QtWidgets import QApplication
from views.view import MainView
from models.model import ReportModel
from controllers.controller import ReportController

logging.config.fileConfig('./mainLogging/logging_config.ini')
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    working_directory = ""
    if getattr(sys, 'frozen', False):
        working_directory = os.path.dirname(sys.executable)
    elif __file__:
        working_directory = os.path.dirname(__file__)
    else:
        working_directory = os.getcwd()

    app = QApplication(sys.argv)
    main_view = MainView()
    main_model = ReportModel()
    main_controller = ReportController(main_view, main_model)
    main_view.show()
    sys.exit(app.exec())
