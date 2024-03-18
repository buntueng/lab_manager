# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_updater.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(560, 267)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.select_exe_pushButton = QPushButton(self.centralwidget)
        self.select_exe_pushButton.setObjectName(u"select_exe_pushButton")
        self.select_exe_pushButton.setGeometry(QRect(450, 60, 91, 24))
        self.test_server_pushButton = QPushButton(self.centralwidget)
        self.test_server_pushButton.setObjectName(u"test_server_pushButton")
        self.test_server_pushButton.setGeometry(QRect(20, 220, 131, 41))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 60, 311, 22))
        self.lineEdit.setReadOnly(True)
        self.description_textEdit = QTextEdit(self.centralwidget)
        self.description_textEdit.setObjectName(u"description_textEdit")
        self.description_textEdit.setGeometry(QRect(20, 120, 521, 91))
        self.config_file_comboBox = QComboBox(self.centralwidget)
        self.config_file_comboBox.setObjectName(u"config_file_comboBox")
        self.config_file_comboBox.setGeometry(QRect(120, 20, 421, 22))
        self.sever_config_label = QLabel(self.centralwidget)
        self.sever_config_label.setObjectName(u"sever_config_label")
        self.sever_config_label.setGeometry(QRect(10, 20, 101, 20))
        self.software_path_label = QLabel(self.centralwidget)
        self.software_path_label.setObjectName(u"software_path_label")
        self.software_path_label.setGeometry(QRect(10, 60, 81, 16))
        self.description_label = QLabel(self.centralwidget)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setGeometry(QRect(10, 100, 71, 16))
        self.confirm_pushButton = QPushButton(self.centralwidget)
        self.confirm_pushButton.setObjectName(u"confirm_pushButton")
        self.confirm_pushButton.setGeometry(QRect(410, 220, 131, 41))
        self.test_pushButton = QPushButton(self.centralwidget)
        self.test_pushButton.setObjectName(u"test_pushButton")
        self.test_pushButton.setGeometry(QRect(160, 220, 131, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Admin_updater", None))
        self.select_exe_pushButton.setText(QCoreApplication.translate("MainWindow", u"Select EXE", None))
        self.test_server_pushButton.setText(QCoreApplication.translate("MainWindow", u"Check Connection", None))
        self.sever_config_label.setText(QCoreApplication.translate("MainWindow", u"Server: Config file", None))
        self.software_path_label.setText(QCoreApplication.translate("MainWindow", u"Software path", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.confirm_pushButton.setText(QCoreApplication.translate("MainWindow", u"Confirm update", None))
        self.test_pushButton.setText(QCoreApplication.translate("MainWindow", u"Test update", None))
    # retranslateUi

