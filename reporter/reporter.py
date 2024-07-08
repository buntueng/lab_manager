import os
import sys
import logging.config
from PySide6.QtWidgets import QApplication
from views.view import MainView
from models.model import ReportModel
from controllers.controller import ReportController
from datetime import datetime

current_directory = ""
if getattr(sys, 'frozen', False):
    current_directory = os.path.dirname(sys.executable)
else:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
if not os.path.exists(current_directory + "/logs"):
    os.mkdir(current_directory + "/logs")

log_file_path = {'logfilename': f"./logs/{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"}
init_log_path = os.path.join(current_directory, "logging_config.conf")
logging.config.fileConfig(init_log_path, defaults=log_file_path, disable_existing_loggers=False)

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    app = QApplication(sys.argv)
    main_view = MainView()
    main_model = ReportModel()
    main_controller = ReportController(main_view, main_model)
    main_view.show()
    sys.exit(app.exec())
