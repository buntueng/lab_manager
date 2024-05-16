import os
import sys
import logging
import logging.config
from PySide6.QtWidgets import QApplication
from views.view import MainView
from models.model import ReportModel
from controllers.controller import ReportController


if __name__ == "__main__":
    working_directory = ""
    if getattr(sys, 'frozen', False):
        working_directory = os.path.dirname(sys.executable)
    elif __file__:
        working_directory = os.path.dirname(__file__)
    else:
        working_directory = os.getcwd()
    config_file = os.path.join(
        working_directory, "models", "log_config.ini")
    logging.config.fileConfig(config_file)  # load logging configuration
    logger = logging.getLogger('sLogger')
    app = QApplication(sys.argv)
    main_view = MainView()
    main_model = ReportModel()
    main_controller = ReportController(main_view, main_model,logger)
    main_view.show()
    sys.exit(app.exec())
