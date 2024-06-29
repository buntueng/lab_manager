import os
import ftplib
import sys
import yaml
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLineEdit
from mainUI import Ui_MainWindow  # Import the generated UI class

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initUI()
                
        # bind  events
        self.loadConfigPushButton.clicked.connect(self.load_config_button_clicked)
        self.localPathPushButton.clicked.connect(self.local_path_button_clicked)
        self.configurePushButton.clicked.connect(self.configure_button_clicked)

    def initUI(self):
        # Initialize your UI components and connect signals/slots here
        # set title of the window
        self.setWindowTitle("Setup CVDTT software")

    def load_config_button_clicked(self):
        # open openFile dialog to load yml config file
        config_obj = QFileDialog.getOpenFileName(self, "Open File", "", "YML Files (*.yml)")
        # if open file dialog is cancelled
        if not config_obj[0]:
            print("No file selected")
        else:
            # load  yml file
            with open(config_obj[0], 'r') as stream:
                try:
                    data = yaml.safe_load(stream)
                    # add text to lineEdit
                    self.serverIPLineEdit.setText(data['server_ip'])
                    
                    self.usernameLineEdit.setText(data['server_username'])
                    # show password as *
                    # self.passwordLineEdit.setEchoMode(QLineEdit.Password)
                    self.passwordLineEdit.setText(data['server_password'])
                    self.serverPathLineEdit.setText(data['server_path'])
                except yaml.YAMLError as exc_error:
                    QMessageBox.critical(self, "Error", f"Error loading config file {exc_error}")
        
    def local_path_button_clicked(self):
        # open directory dialog to select local path
        local_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        # if open directory dialog is cancelled
        if not local_path:
            QMessageBox.critical(self, "Warning", "No directory selected")
        else:
            # add text to lineEdit
            self.localPathLineEdit.setText(local_path)
        
    def configure_button_clicked(self):
        # if any of the fields are empty show error message
        if not self.serverIPLineEdit.text() or not self.usernameLineEdit.text() or not self.passwordLineEdit.text() or not self.serverPathLineEdit.text() or not self.localPathLineEdit.text():
            QMessageBox.critical(self, "Error", "Please fill all fields")
        else:
            self.start_configure()
            
            
    def download_file(self,ftp, remote_file_path, local_file_path):
        with open(local_file_path, 'wb') as local_file:
            ftp.retrbinary(f'RETR {remote_file_path}', local_file.write)
        print(f"Downloaded: {remote_file_path} to {local_file_path}")

    def download_directory(self,ftp, remote_dir, local_dir):
        os.makedirs(local_dir, exist_ok=True)
        ftp.cwd(remote_dir)
        file_list = ftp.nlst()

        for file in file_list:
            local_file_path = os.path.join(local_dir, file)
            if self.is_ftp_dir(ftp, file):
                self.download_directory(ftp, file, local_file_path)
            else:
                self.download_file(ftp, file, local_file_path)
        
        ftp.cwd("..")

    def is_ftp_dir(self,ftp, path):
        current = ftp.pwd()
        try:
            ftp.cwd(path)
            ftp.cwd(current)
            return True
        except ftplib.error_perm as e:
            return False

    def connect_ftp(self,host, user, passwd):
        ftp = ftplib.FTP()
        ftp.connect(host)
        ftp.login(user=user, passwd=passwd)
        ftp.set_pasv(False)  # Disable passive mode, enable active mode
        return ftp
    
    def start_configure(self):
        template_folder = f"{self.localPathLineEdit.text()}/template"
        # check template folder exists
        if not os.path.exists(template_folder):
            os.makedirs(template_folder, exist_ok=True)
        # start configuration by read folder name on ftp server and then download files
        ftp = self.connect_ftp(self.serverIPLineEdit.text(), self.usernameLineEdit.text(), self.passwordLineEdit.text())
        try:
            # download files to template folder
            self.download_directory(ftp, self.serverPathLineEdit.text(), template_folder)
        finally:
            ftp.quit()
            QMessageBox.information(self, "Success", "Downloaded files successfully")
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
