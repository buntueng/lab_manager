# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1342, 885)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setGeometry(QRect(10, 10, 191, 861))
        self.menu_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.main_menu_label = QLabel(self.menu_frame)
        self.main_menu_label.setObjectName(u"main_menu_label")
        self.main_menu_label.setGeometry(QRect(10, 10, 91, 20))
        font = QFont()
        font.setFamilies([u"TH Niramit AS"])
        font.setPointSize(16)
        font.setBold(True)
        self.main_menu_label.setFont(font)
        self.main_menu_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.serum_pushButton = QPushButton(self.menu_frame)
        self.serum_pushButton.setObjectName(u"serum_pushButton")
        self.serum_pushButton.setGeometry(QRect(10, 40, 171, 41))
        self.serum_pushButton.setFont(font)
        self.bacteria_pushButton = QPushButton(self.menu_frame)
        self.bacteria_pushButton.setObjectName(u"bacteria_pushButton")
        self.bacteria_pushButton.setGeometry(QRect(10, 90, 171, 41))
        self.bacteria_pushButton.setFont(font)
        self.approve_report_pushButton = QPushButton(self.menu_frame)
        self.approve_report_pushButton.setObjectName(u"approve_report_pushButton")
        self.approve_report_pushButton.setGeometry(QRect(10, 750, 171, 41))
        self.approve_report_pushButton.setStyleSheet(u"background-color: rgb(170, 255, 255);")
        self.sign_out_pushButton = QPushButton(self.menu_frame)
        self.sign_out_pushButton.setObjectName(u"sign_out_pushButton")
        self.sign_out_pushButton.setGeometry(QRect(10, 810, 171, 41))
        self.sign_out_pushButton.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.molecularBio_pushButton = QPushButton(self.menu_frame)
        self.molecularBio_pushButton.setObjectName(u"molecularBio_pushButton")
        self.molecularBio_pushButton.setGeometry(QRect(10, 190, 171, 41))
        self.molecularBio_pushButton.setFont(font)
        self.parasite_pushButton = QPushButton(self.menu_frame)
        self.parasite_pushButton.setObjectName(u"parasite_pushButton")
        self.parasite_pushButton.setGeometry(QRect(10, 240, 171, 41))
        self.parasite_pushButton.setFont(font)
        self.water_quality_pushButton = QPushButton(self.menu_frame)
        self.water_quality_pushButton.setObjectName(u"water_quality_pushButton")
        self.water_quality_pushButton.setGeometry(QRect(10, 290, 171, 41))
        self.water_quality_pushButton.setFont(font)
        self.bacteriaVirtek_pushButton = QPushButton(self.menu_frame)
        self.bacteriaVirtek_pushButton.setObjectName(u"bacteriaVirtek_pushButton")
        self.bacteriaVirtek_pushButton.setGeometry(QRect(10, 140, 171, 41))
        self.bacteriaVirtek_pushButton.setFont(font)
        self.food_quality_pushButton = QPushButton(self.menu_frame)
        self.food_quality_pushButton.setObjectName(u"food_quality_pushButton")
        self.food_quality_pushButton.setGeometry(QRect(10, 340, 171, 41))
        self.food_quality_pushButton.setFont(font)
        self.sperm_pushButton = QPushButton(self.menu_frame)
        self.sperm_pushButton.setObjectName(u"sperm_pushButton")
        self.sperm_pushButton.setGeometry(QRect(10, 390, 171, 41))
        self.sperm_pushButton.setFont(font)
        self.virus_pushButton = QPushButton(self.menu_frame)
        self.virus_pushButton.setObjectName(u"virus_pushButton")
        self.virus_pushButton.setGeometry(QRect(10, 440, 171, 41))
        self.virus_pushButton.setFont(font)
        self.chemical_pushButton = QPushButton(self.menu_frame)
        self.chemical_pushButton.setObjectName(u"chemical_pushButton")
        self.chemical_pushButton.setGeometry(QRect(10, 490, 171, 41))
        self.chemical_pushButton.setFont(font)
        self.pathology_pushButton = QPushButton(self.menu_frame)
        self.pathology_pushButton.setObjectName(u"pathology_pushButton")
        self.pathology_pushButton.setGeometry(QRect(10, 540, 171, 41))
        self.pathology_pushButton.setFont(font)
        self.working_frame = QFrame(self.centralwidget)
        self.working_frame.setObjectName(u"working_frame")
        self.working_frame.setGeometry(QRect(200, 10, 1141, 861))
        self.working_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.working_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget = QStackedWidget(self.working_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 40, 1131, 821))
        self.stackedWidget.setStyleSheet(u"")
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
        self.frame = QFrame(self.login_page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(350, 90, 341, 171))
        self.frame.setStyleSheet(u"background-color: rgb(0,180, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget.addWidget(self.login_page)
        self.frame.raise_()
        self.login_username_label.raise_()
        self.login_username_lineEdit.raise_()
        self.login_password_label.raise_()
        self.login_password_lineEdit.raise_()
        self.login_pushButton.raise_()
        self.serum_page = QWidget()
        self.serum_page.setObjectName(u"serum_page")
        self.serum_page_label = QLabel(self.serum_page)
        self.serum_page_label.setObjectName(u"serum_page_label")
        self.serum_page_label.setGeometry(QRect(0, 0, 131, 41))
        self.serum_page_label.setFont(font)
        self.label_11 = QLabel(self.serum_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 70, 91, 16))
        self.label_11.setFont(font)
        self.stackedWidget.addWidget(self.serum_page)
        self.bactria_page = QWidget()
        self.bactria_page.setObjectName(u"bactria_page")
        self.label = QLabel(self.bactria_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 161, 41))
        self.label.setFont(font)
        self.stackedWidget.addWidget(self.bactria_page)
        self.bacteria_virtek_page = QWidget()
        self.bacteria_virtek_page.setObjectName(u"bacteria_virtek_page")
        self.label_2 = QLabel(self.bacteria_virtek_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 171, 41))
        self.label_2.setFont(font)
        self.stackedWidget.addWidget(self.bacteria_virtek_page)
        self.micro_bio_page = QWidget()
        self.micro_bio_page.setObjectName(u"micro_bio_page")
        self.label_3 = QLabel(self.micro_bio_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 0, 141, 41))
        self.label_3.setFont(font)
        self.treeWidget_2 = QTreeWidget(self.micro_bio_page)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setGeometry(QRect(20, 50, 941, 181))
        self.treeWidget_2.setFont(font)
        self.stackedWidget.addWidget(self.micro_bio_page)
        self.parasite_page = QWidget()
        self.parasite_page.setObjectName(u"parasite_page")
        self.parasitePageLabel = QLabel(self.parasite_page)
        self.parasitePageLabel.setObjectName(u"parasitePageLabel")
        self.parasitePageLabel.setGeometry(QRect(30, 190, 281, 31))
        self.parasitePageLabel.setFont(font)
        self.parasiteTreeWidget = QTreeWidget(self.parasite_page)
        self.parasiteTreeWidget.setObjectName(u"parasiteTreeWidget")
        self.parasiteTreeWidget.setGeometry(QRect(20, 20, 951, 111))
        font1 = QFont()
        font1.setFamilies([u"TH Niramit AS"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.parasiteTreeWidget.setFont(font1)
        self.parasiteTreeWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.parasiteSearchPushButton = QPushButton(self.parasite_page)
        self.parasiteSearchPushButton.setObjectName(u"parasiteSearchPushButton")
        self.parasiteSearchPushButton.setGeometry(QRect(980, 20, 141, 51))
        self.parasiteSearchPushButton.setFont(font)
        self.parasiteSearchPushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.parasiteSelectPushButton = QPushButton(self.parasite_page)
        self.parasiteSelectPushButton.setObjectName(u"parasiteSelectPushButton")
        self.parasiteSelectPushButton.setGeometry(QRect(980, 80, 141, 51))
        self.parasiteSelectPushButton.setFont(font)
        self.parasiteSelectPushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.parasiteCaseIDTextEdit = QTextEdit(self.parasite_page)
        self.parasiteCaseIDTextEdit.setObjectName(u"parasiteCaseIDTextEdit")
        self.parasiteCaseIDTextEdit.setGeometry(QRect(170, 140, 271, 31))
        self.parasiteCaseIDTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.parasiteCaseIDTextEdit.setReadOnly(True)
        self.parasiteCaseNumberLabel = QLabel(self.parasite_page)
        self.parasiteCaseNumberLabel.setObjectName(u"parasiteCaseNumberLabel")
        self.parasiteCaseNumberLabel.setGeometry(QRect(30, 150, 121, 16))
        self.parasiteCaseNumberLabel.setFont(font)
        self.parasiteSavePushButton = QPushButton(self.parasite_page)
        self.parasiteSavePushButton.setObjectName(u"parasiteSavePushButton")
        self.parasiteSavePushButton.setGeometry(QRect(980, 300, 141, 51))
        self.parasiteSavePushButton.setFont(font)
        self.parasiteSavePushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.parasiteResultTextEdit = QTextEdit(self.parasite_page)
        self.parasiteResultTextEdit.setObjectName(u"parasiteResultTextEdit")
        self.parasiteResultTextEdit.setGeometry(QRect(30, 230, 941, 451))
        font2 = QFont()
        font2.setFamilies([u"TH Sarabun New"])
        font2.setPointSize(16)
        self.parasiteResultTextEdit.setFont(font2)
        self.parasiteResultTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.commentLabel = QLabel(self.parasite_page)
        self.commentLabel.setObjectName(u"commentLabel")
        self.commentLabel.setGeometry(QRect(30, 700, 91, 31))
        self.commentLabel.setFont(font)
        self.parasiteCommentTextEdit = QTextEdit(self.parasite_page)
        self.parasiteCommentTextEdit.setObjectName(u"parasiteCommentTextEdit")
        self.parasiteCommentTextEdit.setGeometry(QRect(30, 730, 941, 71))
        font3 = QFont()
        font3.setFamilies([u"TH Niramit AS"])
        font3.setPointSize(14)
        self.parasiteCommentTextEdit.setFont(font3)
        self.parasiteCommentTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.parasiteInsertImagePushButton = QPushButton(self.parasite_page)
        self.parasiteInsertImagePushButton.setObjectName(u"parasiteInsertImagePushButton")
        self.parasiteInsertImagePushButton.setGeometry(QRect(980, 230, 141, 51))
        self.parasiteInsertImagePushButton.setFont(font)
        self.parasiteInsertImagePushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.parasite_page)
        self.water_quality_page = QWidget()
        self.water_quality_page.setObjectName(u"water_quality_page")
        self.label_5 = QLabel(self.water_quality_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 191, 41))
        self.label_5.setFont(font)
        self.stackedWidget.addWidget(self.water_quality_page)
        self.food_quality_page = QWidget()
        self.food_quality_page.setObjectName(u"food_quality_page")
        self.label_6 = QLabel(self.food_quality_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 211, 41))
        self.label_6.setFont(font)
        self.stackedWidget.addWidget(self.food_quality_page)
        self.sperm_quality_page = QWidget()
        self.sperm_quality_page.setObjectName(u"sperm_quality_page")
        self.label_7 = QLabel(self.sperm_quality_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 0, 171, 41))
        self.label_7.setFont(font)
        self.stackedWidget.addWidget(self.sperm_quality_page)
        self.virus_page = QWidget()
        self.virus_page.setObjectName(u"virus_page")
        self.label_8 = QLabel(self.virus_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 141, 41))
        self.label_8.setFont(font)
        self.stackedWidget.addWidget(self.virus_page)
        self.chemical_page = QWidget()
        self.chemical_page.setObjectName(u"chemical_page")
        self.label_9 = QLabel(self.chemical_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 211, 41))
        self.label_9.setFont(font)
        self.stackedWidget.addWidget(self.chemical_page)
        self.pathology_page = QWidget()
        self.pathology_page.setObjectName(u"pathology_page")
        self.label_10 = QLabel(self.pathology_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 191, 41))
        self.label_10.setFont(font)
        self.stackedWidget.addWidget(self.pathology_page)
        self.approve_report_page = QWidget()
        self.approve_report_page.setObjectName(u"approve_report_page")
        self.approve_report_page_label = QLabel(self.approve_report_page)
        self.approve_report_page_label.setObjectName(u"approve_report_page_label")
        self.approve_report_page_label.setGeometry(QRect(0, 0, 141, 41))
        self.approve_report_page_label.setFont(font)
        self.stackedWidget.addWidget(self.approve_report_page)
        self.user_info_label = QLabel(self.working_frame)
        self.user_info_label.setObjectName(u"user_info_label")
        self.user_info_label.setGeometry(QRect(888, 10, 211, 20))
        self.user_info_label.setFont(font)
        self.user_info_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Report Manager", None))
        self.main_menu_label.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e23\u0e49\u0e32\u0e07\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19", None))
        self.serum_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e0b\u0e35\u0e23\u0e31\u0e21\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        self.bacteria_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e41\u0e1a\u0e04\u0e17\u0e35\u0e40\u0e23\u0e35\u0e22\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        self.approve_report_pushButton.setText(QCoreApplication.translate("MainWindow", u"Approve \u0e23\u0e32\u0e22\u0e07\u0e32\u0e19", None))
        self.sign_out_pushButton.setText(QCoreApplication.translate("MainWindow", u"Sign Out", None))
        self.molecularBio_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e2d\u0e13\u0e39\u0e0a\u0e35\u0e27\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        self.parasite_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e1b\u0e23\u0e2a\u0e34\u0e15\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        self.water_quality_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e19\u0e49\u0e33", None))
        self.bacteriaVirtek_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e41\u0e1a\u0e04\u0e17\u0e35\u0e40\u0e23\u0e35\u0e22\u0e27\u0e34\u0e17\u0e22\u0e32 Virtek", None))
        self.food_quality_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e2d\u0e32\u0e2b\u0e32\u0e23\u0e2a\u0e31\u0e15\u0e27\u0e4c", None))
        self.sperm_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e19\u0e49\u0e33\u0e40\u0e0a\u0e37\u0e49\u0e2d", None))
        self.virus_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e44\u0e27\u0e23\u0e31\u0e2a\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        self.chemical_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e15\u0e23\u0e27\u0e08\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e40\u0e04\u0e21\u0e35", None))
        self.pathology_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e1e\u0e22\u0e32\u0e18\u0e34\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        self.login_username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.login_password_label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.serum_page_label.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e0b\u0e35\u0e23\u0e31\u0e21\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0e1c\u0e25\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08 ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e41\u0e1a\u0e04\u0e17\u0e35\u0e40\u0e23\u0e35\u0e22\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e41\u0e1a\u0e04\u0e17\u0e35\u0e40\u0e23\u0e35\u0e22 Virtek", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e2d\u0e13\u0e39\u0e0a\u0e35\u0e27\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        ___qtreewidgetitem = self.treeWidget_2.headerItem()
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e48\u0e07\u0e14\u0e48\u0e27\u0e19", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"\u0e01\u0e32\u0e23\u0e40\u0e01\u0e47\u0e1a\u0e23\u0e31\u0e01\u0e29\u0e32", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"\u0e2b\u0e49\u0e2d\u0e07\u0e1b\u0e0f\u0e34\u0e1a\u0e31\u0e15\u0e34\u0e01\u0e32\u0e23", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"\u0e0a\u0e19\u0e34\u0e14\u0e2a\u0e31\u0e15\u0e27\u0e4c", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e25\u0e02\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e23\u0e31\u0e1a\u0e40\u0e04\u0e2a", None));
        self.parasitePageLabel.setText(QCoreApplication.translate("MainWindow", u"\u0e1c\u0e25\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08\u0e17\u0e32\u0e07\u0e2b\u0e49\u0e2d\u0e07\u0e1b\u0e0f\u0e34\u0e1a\u0e31\u0e15\u0e34\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e2a\u0e34\u0e15\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        ___qtreewidgetitem1 = self.parasiteTreeWidget.headerItem()
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("MainWindow", u"\u0e2a\u0e16\u0e32\u0e19\u0e30", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("MainWindow", u"\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e48\u0e07\u0e14\u0e48\u0e27\u0e19", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"\u0e01\u0e32\u0e23\u0e40\u0e01\u0e47\u0e1a\u0e23\u0e31\u0e01\u0e29\u0e32", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"\u0e2b\u0e49\u0e2d\u0e07\u0e1b\u0e0f\u0e34\u0e1a\u0e31\u0e15\u0e34\u0e01\u0e32\u0e23", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"\u0e0a\u0e19\u0e34\u0e14\u0e2a\u0e31\u0e15\u0e27\u0e4c", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e25\u0e02\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e23\u0e31\u0e1a\u0e40\u0e04\u0e2a", None));
        self.parasiteSearchPushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e49\u0e19\u0e2b\u0e32", None))
        self.parasiteSelectPushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e40\u0e04\u0e2a", None))
        self.parasiteCaseNumberLabel.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e25\u0e02\u0e01\u0e32\u0e23\u0e15\u0e23\u0e27\u0e08", None))
        self.parasiteSavePushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25", None))
        self.commentLabel.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e2b\u0e15\u0e38", None))
        self.parasiteInsertImagePushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e23\u0e39\u0e1b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e19\u0e49\u0e33", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e2d\u0e32\u0e2b\u0e32\u0e23\u0e2a\u0e31\u0e15\u0e27\u0e4c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e04\u0e38\u0e13\u0e20\u0e32\u0e1e\u0e19\u0e49\u0e33\u0e40\u0e0a\u0e37\u0e49\u0e2d", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e44\u0e27\u0e23\u0e31\u0e2a\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e15\u0e23\u0e27\u0e08\u0e27\u0e34\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e40\u0e04\u0e21\u0e35", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e1e\u0e22\u0e32\u0e18\u0e34\u0e27\u0e34\u0e17\u0e22\u0e32", None))
        self.approve_report_page_label.setText(QCoreApplication.translate("MainWindow", u"Approve \u0e23\u0e32\u0e22\u0e07\u0e32\u0e19", None))
        self.user_info_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

