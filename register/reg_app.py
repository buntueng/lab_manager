import sys
import os
import yaml
import mariadb
from PySide6.QtWidgets import QApplication

from models.main_model import Main_Model
from controllers.main_controller import Main_Controller
from views.all_views import MainAppView

if __name__ == "__main__":
    main_application = QApplication(sys.argv)
    main_view = MainAppView()
    main_model = Main_Model()
    main_controller = Main_Controller(main_model, main_view)
    main_view.show_view()

    sys.exit(main_application.exec())
    
