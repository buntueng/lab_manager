# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_app_view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_main_app_view(object):
    def setupUi(self, main_app_view):
        if not main_app_view.objectName():
            main_app_view.setObjectName(u"main_app_view")
        main_app_view.resize(1400, 900)
        main_app_view.setMinimumSize(QSize(1400, 900))
        main_app_view.setMaximumSize(QSize(1400, 900))
        self.actionCytology_Report = QAction(main_app_view)
        self.actionCytology_Report.setObjectName(u"actionCytology_Report")
        self.actionNecropsy_Report = QAction(main_app_view)
        self.actionNecropsy_Report.setObjectName(u"actionNecropsy_Report")
        self.actionSave_on_This_PC = QAction(main_app_view)
        self.actionSave_on_This_PC.setObjectName(u"actionSave_on_This_PC")
        self.actionSave_on_Server = QAction(main_app_view)
        self.actionSave_on_Server.setObjectName(u"actionSave_on_Server")
        self.actionLoad_from_this_PC = QAction(main_app_view)
        self.actionLoad_from_this_PC.setObjectName(u"actionLoad_from_this_PC")
        self.actionLoad_from_Server = QAction(main_app_view)
        self.actionLoad_from_Server.setObjectName(u"actionLoad_from_Server")
        self.actionConfirm_Report = QAction(main_app_view)
        self.actionConfirm_Report.setObjectName(u"actionConfirm_Report")
        self.actionApprove_Report = QAction(main_app_view)
        self.actionApprove_Report.setObjectName(u"actionApprove_Report")
        self.centralwidget = QWidget(main_app_view)
        self.centralwidget.setObjectName(u"centralwidget")
        self.page_widget = QWidget(self.centralwidget)
        self.page_widget.setObjectName(u"page_widget")
        self.page_widget.setGeometry(QRect(10, 10, 171, 881))
        self.page_widget.setAutoFillBackground(False)
        self.page_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(131, 216, 255)\n"
"}")
        self.verticalLayout = QVBoxLayout(self.page_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 9, -1)
        self.label = QLabel(self.page_widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"TH Niramit AS"])
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.customer_reg_pushButton = QPushButton(self.page_widget)
        self.customer_reg_pushButton.setObjectName(u"customer_reg_pushButton")
        font1 = QFont()
        font1.setFamilies([u"TH Niramit AS"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.customer_reg_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.customer_reg_pushButton)

        self.case_register_pushButton = QPushButton(self.page_widget)
        self.case_register_pushButton.setObjectName(u"case_register_pushButton")
        self.case_register_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.case_register_pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.check_job_pushButton = QPushButton(self.page_widget)
        self.check_job_pushButton.setObjectName(u"check_job_pushButton")
        self.check_job_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.check_job_pushButton)

        self.barcode_pushButton = QPushButton(self.page_widget)
        self.barcode_pushButton.setObjectName(u"barcode_pushButton")
        self.barcode_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.barcode_pushButton)

        self.lab_order_pushButton = QPushButton(self.page_widget)
        self.lab_order_pushButton.setObjectName(u"lab_order_pushButton")
        self.lab_order_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.lab_order_pushButton)

        self.bill_pushButton = QPushButton(self.page_widget)
        self.bill_pushButton.setObjectName(u"bill_pushButton")
        self.bill_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.bill_pushButton)

        self.check_report_pushButton = QPushButton(self.page_widget)
        self.check_report_pushButton.setObjectName(u"check_report_pushButton")
        self.check_report_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.check_report_pushButton)

        self.verticalSpacer = QSpacerItem(5, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.employee_pushButton = QPushButton(self.page_widget)
        self.employee_pushButton.setObjectName(u"employee_pushButton")
        self.employee_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.employee_pushButton)

        self.personal_info_pushButton = QPushButton(self.page_widget)
        self.personal_info_pushButton.setObjectName(u"personal_info_pushButton")
        self.personal_info_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.personal_info_pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.update_prog_pushButton = QPushButton(self.page_widget)
        self.update_prog_pushButton.setObjectName(u"update_prog_pushButton")
        self.update_prog_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.update_prog_pushButton)

        self.sign_out_pushButton = QPushButton(self.page_widget)
        self.sign_out_pushButton.setObjectName(u"sign_out_pushButton")
        self.sign_out_pushButton.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/icons/icons/log_out_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sign_out_pushButton.setIcon(icon)

        self.verticalLayout.addWidget(self.sign_out_pushButton)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(190, 40, 1201, 851))
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 10, 1181, 831))
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.username_lineEdit = QLineEdit(self.login_page)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setGeometry(QRect(460, 260, 241, 22))
        self.password_lineEdit = QLineEdit(self.login_page)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setGeometry(QRect(460, 310, 241, 22))
        self.password_lineEdit.setEchoMode(QLineEdit.Password)
        self.login_pushButton = QPushButton(self.login_page)
        self.login_pushButton.setObjectName(u"login_pushButton")
        self.login_pushButton.setGeometry(QRect(590, 340, 111, 31))
        self.label_2 = QLabel(self.login_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 240, 71, 16))
        self.label_3 = QLabel(self.login_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 290, 49, 16))
        self.groupBox = QGroupBox(self.login_page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(430, 210, 291, 191))
        self.groupBox.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.stackedWidget.addWidget(self.login_page)
        self.groupBox.raise_()
        self.username_lineEdit.raise_()
        self.password_lineEdit.raise_()
        self.login_pushButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.new_customer_page = QWidget()
        self.new_customer_page.setObjectName(u"new_customer_page")
        self.label_11 = QLabel(self.new_customer_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 81, 16))
        self.stackedWidget.addWidget(self.new_customer_page)
        self.new_job_page = QWidget()
        self.new_job_page.setObjectName(u"new_job_page")
        self.label_12 = QLabel(self.new_job_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 10, 49, 16))
        self.stackedWidget.addWidget(self.new_job_page)
        self.check_job_page = QWidget()
        self.check_job_page.setObjectName(u"check_job_page")
        self.label_6 = QLabel(self.check_job_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 111, 16))
        self.stackedWidget.addWidget(self.check_job_page)
        self.employee_page = QWidget()
        self.employee_page.setObjectName(u"employee_page")
        self.label_9 = QLabel(self.employee_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 61, 16))
        self.stackedWidget.addWidget(self.employee_page)
        self.check_report_page = QWidget()
        self.check_report_page.setObjectName(u"check_report_page")
        self.label_7 = QLabel(self.check_report_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 81, 16))
        self.stackedWidget.addWidget(self.check_report_page)
        self.bill_page = QWidget()
        self.bill_page.setObjectName(u"bill_page")
        self.label_5 = QLabel(self.bill_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 49, 16))
        self.stackedWidget.addWidget(self.bill_page)
        self.barcode_page = QWidget()
        self.barcode_page.setObjectName(u"barcode_page")
        self.label_4 = QLabel(self.barcode_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 81, 16))
        self.stackedWidget.addWidget(self.barcode_page)
        self.lab_report_page = QWidget()
        self.lab_report_page.setObjectName(u"lab_report_page")
        self.label_10 = QLabel(self.lab_report_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 71, 16))
        self.stackedWidget.addWidget(self.lab_report_page)
        self.edit_personal_page = QWidget()
        self.edit_personal_page.setObjectName(u"edit_personal_page")
        self.label_8 = QLabel(self.edit_personal_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 49, 16))
        self.stackedWidget.addWidget(self.edit_personal_page)
        self.update_page = QWidget()
        self.update_page.setObjectName(u"update_page")
        self.label_13 = QLabel(self.update_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 10, 71, 16))
        self.stackedWidget.addWidget(self.update_page)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setGeometry(QRect(190, 10, 1201, 31))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.current_user_label = QLabel(self.top_frame)
        self.current_user_label.setObjectName(u"current_user_label")
        self.current_user_label.setGeometry(QRect(1140, 10, 49, 16))
        main_app_view.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_app_view)

        self.stackedWidget.setCurrentIndex(10)


        QMetaObject.connectSlotsByName(main_app_view)
    # setupUi

    def retranslateUi(self, main_app_view):
        main_app_view.setWindowTitle(QCoreApplication.translate("main_app_view", u"Report generator", None))
        self.actionCytology_Report.setText(QCoreApplication.translate("main_app_view", u"Cytology Report", None))
        self.actionNecropsy_Report.setText(QCoreApplication.translate("main_app_view", u"Necropsy Report", None))
        self.actionSave_on_This_PC.setText(QCoreApplication.translate("main_app_view", u"Save on This PC", None))
        self.actionSave_on_Server.setText(QCoreApplication.translate("main_app_view", u"Save on Server", None))
        self.actionLoad_from_this_PC.setText(QCoreApplication.translate("main_app_view", u"Load from this PC", None))
        self.actionLoad_from_Server.setText(QCoreApplication.translate("main_app_view", u"Load from Server", None))
        self.actionConfirm_Report.setText(QCoreApplication.translate("main_app_view", u"Confirm Report", None))
        self.actionApprove_Report.setText(QCoreApplication.translate("main_app_view", u"Approve Report", None))
        self.label.setText(QCoreApplication.translate("main_app_view", u"\u0e23\u0e30\u0e1a\u0e1a\u0e25\u0e07\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19", None))
        self.customer_reg_pushButton.setText(QCoreApplication.translate("main_app_view", u"\u0e25\u0e07\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32\u0e43\u0e2b\u0e21\u0e48", None))
        self.case_register_pushButton.setText(QCoreApplication.translate("main_app_view", u"\u0e23\u0e31\u0e1a\u0e07\u0e32\u0e19\u0e43\u0e2b\u0e21\u0e48", None))
        self.check_job_pushButton.setText(QCoreApplication.translate("main_app_view", u"\u0e15\u0e23\u0e27\u0e08\u0e2a\u0e2d\u0e1a\u0e07\u0e32\u0e19", None))
        self.barcode_pushButton.setText(QCoreApplication.translate("main_app_view", u"\u0e1b\u0e23\u0e34\u0e49\u0e19\u0e1a\u0e32\u0e23\u0e4c\u0e42\u0e04\u0e49\u0e14", None))
        self.lab_order_pushButton.setText(QCoreApplication.translate("main_app_view", u"\u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e43\u0e1a\u0e2a\u0e48\u0e07\u0e41\u0e25\u0e1b", None))
        self.bill_pushButton.setText(QCoreApplication.translate("main_app_view", u"\u0e2d\u0e2d\u0e01\u0e43\u0e1a\u0e40\u0e2a\u0e23\u0e47\u0e08", None))
        self.check_report_pushButton.setText(QCoreApplication.translate("main_app_view", u"\u0e23\u0e32\u0e22\u0e07\u0e32\u0e19\u0e17\u0e35\u0e48\u0e2a\u0e48\u0e07\u0e41\u0e25\u0e49\u0e27", None))
        self.employee_pushButton.setText(QCoreApplication.translate("main_app_view", u"\u0e08\u0e31\u0e14\u0e01\u0e32\u0e23\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e1a\u0e38\u0e04\u0e25\u0e32\u0e01\u0e23", None))
        self.personal_info_pushButton.setText(QCoreApplication.translate("main_app_view", u"\u0e41\u0e01\u0e49\u0e44\u0e02\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e48\u0e27\u0e19\u0e15\u0e31\u0e27", None))
        self.update_prog_pushButton.setText(QCoreApplication.translate("main_app_view", u"UPDATE", None))
        self.sign_out_pushButton.setText(QCoreApplication.translate("main_app_view", u"Sign Out", None))
        self.login_pushButton.setText(QCoreApplication.translate("main_app_view", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("main_app_view", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("main_app_view", u"Password", None))
        self.groupBox.setTitle("")
        self.label_11.setText(QCoreApplication.translate("main_app_view", u"New customer", None))
        self.label_12.setText(QCoreApplication.translate("main_app_view", u"New job", None))
        self.label_6.setText(QCoreApplication.translate("main_app_view", u"Check Job progress", None))
        self.label_9.setText(QCoreApplication.translate("main_app_view", u"Employee", None))
        self.label_7.setText(QCoreApplication.translate("main_app_view", u"Check report", None))
        self.label_5.setText(QCoreApplication.translate("main_app_view", u"Bill page", None))
        self.label_4.setText(QCoreApplication.translate("main_app_view", u"Barcode page", None))
        self.label_10.setText(QCoreApplication.translate("main_app_view", u"Lab report", None))
        self.label_8.setText(QCoreApplication.translate("main_app_view", u"Personal", None))
        self.label_13.setText(QCoreApplication.translate("main_app_view", u"Update page", None))
        self.current_user_label.setText("")
    # retranslateUi

