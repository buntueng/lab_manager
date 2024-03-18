import sys
import os
import logging
import mariadb
import yaml
from admin_updater import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

# include logging to log the errors and info
log_file_path = os.path.join(os.path.dirname(__file__), 'admin_updater.log')
# create logger
logger = logging.getLogger(__name__)
# format the log and save it to a file
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# print the log to the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
# set the log level to debug
logger.setLevel(logging.DEBUG)


class MainUpdaterAdmin(QMainWindow, Ui_MainWindow):
    """Main window for the updater admin."""

    def __init__(self, parent=None):
        super(MainUpdaterAdmin, self).__init__(parent)
        self.basedir = ""
        self.yml_content = {}
        # Check if the script is run from EXE or from source and get the base directory
        if getattr(sys, 'frozen', False):
            # we are running in a bundle
            self.basedir = sys._MEIPASS
        else:
            # we are running in a normal Python environment
            self.basedir = os.path.dirname(__file__)
        # read all yml files in the basedir
        self.yml_files = [f for f in os.listdir(
            self.basedir) if f.endswith(".yml")]
        # Set up the user interface from Designer.
        self.setupUi(self)
        # clear form
        self.clear_form()
        # Connect the buttons to the functions
        self.select_exe_pushButton.clicked.connect(self.select_exe)
        self.test_server_pushButton.clicked.connect(self.test_server)
        self.confirm_pushButton.clicked.connect(self.confirm_update)
        self.test_pushButton.clicked.connect(self.test_update)
        # add the yml files to the combobox
        if len(self.yml_files) > 0:
            self.config_file_comboBox.addItems(self.yml_files)
        # set current index to 0
        self.config_file_comboBox.setCurrentIndex(0)
        self.config_file_comboBox.currentIndexChanged.connect(
            self.update_yml_content)
        self.update_yml_content()

    def update_yml_content(self):
        """Update the yml content when the combobox is changed."""
        yml_file = self.config_file_comboBox.currentText()
        if not yml_file == "":
            yml_file = os.path.join(self.basedir, yml_file)
            # get the yml file content
            self.yml_content = self.read_yml(yml_file)
        else:
            logger.error("No yml file selected")

    def clear_form(self):
        """Clear the form."""
        self.config_file_comboBox.clear()
        self.lineEdit.clear()
        self.description_textEdit.clear()

    def select_exe(self) -> None:
        """" Select the EXE file to update"""
        # check yml file in dialog
        yml_file = self.config_file_comboBox.currentText()
        if not yml_file == "":
            yml_file = os.path.join(self.basedir, yml_file)
            # get the yml file content
            self.yml_content = self.read_yml(yml_file)

            # open select file dialog
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file, _ = QFileDialog.getOpenFileName(self, "Select the EXE file to update", "",
                                                  "EXE Files (*.exe)", options=options)
            if file:
                self.lineEdit.setText(file)
            else:
                logger.info("No file selected")

        else:
            # show warning in QMessageBox
            QMessageBox.warning(
                self, "Warning", "There is no yml file. \n Please create a yml file first")

    def test_server(self):
        """Test the connection to the server."""
        database_ip = self.yml_content.get('database_ip')
        database_port = self.yml_content.get('database_port')
        database_user = self.yml_content.get('database_user')
        database_password = self.yml_content.get('database_password')
        database_name = self.yml_content.get('database_name')
        database_table = self.yml_content.get('database_table')

        # create a a connection to the database using mariadb
        try:
            conn = mariadb.connect(
                user=database_user,
                password=database_password,
                host=database_ip,
                # port=database_port,
                database=database_name
            )
            # create a cursor
            cur = conn.cursor()
            # execute a query
            cur.execute(self.yml_content['sql']['read_version'])
            # fetch the result
            result = cur.fetchall()
            # close the connection
            conn.close()
            print(result)
        except mariadb.Error as e:
            logger.error(f"Error connecting to MariaDB Platform: {e}")

    def confirm_update(self):
        """Confirm the update of the software."""
        print("Confirm update")

    def test_update(self):
        """Test the update of the software."""
        print("Test update")

    def read_yml(self, filename):
        """Read the content of the yml file."""
        with open(filename, 'r', encoding='UTF8') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUpdaterAdmin()
    window.show()
    sys.exit(app.exec())
