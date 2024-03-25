# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1341, 885)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setGeometry(QRect(10, 10, 141, 861))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.main_menu_label = QLabel(self.menu_frame)
        self.main_menu_label.setObjectName(u"main_menu_label")
        self.main_menu_label.setGeometry(QRect(10, 10, 121, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.main_menu_label.setFont(font)
        self.main_menu_label.setAlignment(Qt.AlignCenter)
        self.cytology_pushButton = QPushButton(self.menu_frame)
        self.cytology_pushButton.setObjectName(u"cytology_pushButton")
        self.cytology_pushButton.setGeometry(QRect(10, 40, 121, 41))
        self.nocropsy_pushButton = QPushButton(self.menu_frame)
        self.nocropsy_pushButton.setObjectName(u"nocropsy_pushButton")
        self.nocropsy_pushButton.setGeometry(QRect(10, 90, 121, 41))
        self.check_report_pushButton = QPushButton(self.menu_frame)
        self.check_report_pushButton.setObjectName(u"check_report_pushButton")
        self.check_report_pushButton.setGeometry(QRect(10, 140, 121, 41))
        self.sign_out_pushButton = QPushButton(self.menu_frame)
        self.sign_out_pushButton.setObjectName(u"sign_out_pushButton")
        self.sign_out_pushButton.setGeometry(QRect(10, 810, 121, 41))
        self.working_frame = QFrame(self.centralwidget)
        self.working_frame.setObjectName(u"working_frame")
        self.working_frame.setGeometry(QRect(160, 10, 1171, 861))
        self.working_frame.setFrameShape(QFrame.StyledPanel)
        self.working_frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.working_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 1151, 841))
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.login_username_label = QLabel(self.login_page)
        self.login_username_label.setObjectName(u"login_username_label")
        self.login_username_label.setGeometry(QRect(400, 110, 81, 16))
        self.login_username_lineEdit = QLineEdit(self.login_page)
        self.login_username_lineEdit.setObjectName(u"login_username_lineEdit")
        self.login_username_lineEdit.setGeometry(QRect(400, 130, 241, 22))
        self.login_password_label = QLabel(self.login_page)
        self.login_password_label.setObjectName(u"login_password_label")
        self.login_password_label.setGeometry(QRect(400, 160, 49, 16))
        self.login_password_lineEdit = QLineEdit(self.login_page)
        self.login_password_lineEdit.setObjectName(u"login_password_lineEdit")
        self.login_password_lineEdit.setGeometry(QRect(400, 180, 241, 22))
        self.login_pushButton = QPushButton(self.login_page)
        self.login_pushButton.setObjectName(u"login_pushButton")
        self.login_pushButton.setGeometry(QRect(540, 210, 101, 31))
        self.stackedWidget.addWidget(self.login_page)
        self.cytology_page = QWidget()
        self.cytology_page.setObjectName(u"cytology_page")
        self.cytology_page_label = QLabel(self.cytology_page)
        self.cytology_page_label.setObjectName(u"cytology_page_label")
        self.cytology_page_label.setGeometry(QRect(10, 6, 101, 20))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.cytology_page_label.setFont(font1)
        self.stackedWidget.addWidget(self.cytology_page)
        self.nocropsy_page = QWidget()
        self.nocropsy_page.setObjectName(u"nocropsy_page")
        self.label = QLabel(self.nocropsy_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 16))
        self.label.setFont(font1)
        self.stackedWidget.addWidget(self.nocropsy_page)
        self.check_report_page = QWidget()
        self.check_report_page.setObjectName(u"check_report_page")
        self.check_report_page_label = QLabel(self.check_report_page)
        self.check_report_page_label.setObjectName(u"check_report_page_label")
        self.check_report_page_label.setGeometry(QRect(10, 10, 91, 16))
        self.check_report_page_label.setFont(font1)
        self.stackedWidget.addWidget(self.check_report_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Report Manager", None))
        self.main_menu_label.setText(QCoreApplication.translate("MainWindow", u"Main Menu", None))
        self.cytology_pushButton.setText(QCoreApplication.translate("MainWindow", u"New Cytology", None))
        self.nocropsy_pushButton.setText(QCoreApplication.translate("MainWindow", u"New Nocropsy", None))
        self.check_report_pushButton.setText(QCoreApplication.translate("MainWindow", u"Check reports", None))
        self.sign_out_pushButton.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.login_username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.login_password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.cytology_page_label.setText(QCoreApplication.translate("MainWindow", u"Cytology Report", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nocropsy report", None))
        self.check_report_page_label.setText(QCoreApplication.translate("MainWindow", u"Check report", None))
    # retranslateUi

