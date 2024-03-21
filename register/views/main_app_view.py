# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_app_view.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

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

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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

        self.verticalSpacer = QSpacerItem(5, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.employee_pushButton = QPushButton(self.page_widget)
        self.employee_pushButton.setObjectName(u"employee_pushButton")
        self.employee_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.employee_pushButton)

        self.personal_info_pushButton = QPushButton(self.page_widget)
        self.personal_info_pushButton.setObjectName(u"personal_info_pushButton")
        self.personal_info_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.personal_info_pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

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
        self.stackedWidget.setGeometry(QRect(0, 0, 1181, 831))
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
        self.legal_person_radioBT = QRadioButton(self.new_customer_page)
        self.legal_person_radioBT.setObjectName(u"legal_person_radioBT")
        self.legal_person_radioBT.setGeometry(QRect(250, 20, 161, 51))
        font2 = QFont()
        font2.setFamilies([u"TH Niramit AS"])
        font2.setPointSize(22)
        font2.setBold(True)
        self.legal_person_radioBT.setFont(font2)
        self.nomal_person_radioBT = QRadioButton(self.new_customer_page)
        self.nomal_person_radioBT.setObjectName(u"nomal_person_radioBT")
        self.nomal_person_radioBT.setGeometry(QRect(40, 20, 161, 51))
        self.nomal_person_radioBT.setFont(font2)
        self.internal_person_radioBT = QRadioButton(self.new_customer_page)
        self.internal_person_radioBT.setObjectName(u"internal_person_radioBT")
        self.internal_person_radioBT.setGeometry(QRect(420, 20, 221, 51))
        self.internal_person_radioBT.setFont(font2)
        self.professor_person_radioBT = QRadioButton(self.new_customer_page)
        self.professor_person_radioBT.setObjectName(u"professor_person_radioBT")
        self.professor_person_radioBT.setGeometry(QRect(660, 20, 161, 51))
        self.professor_person_radioBT.setFont(font2)
        self.student_person_radioBT = QRadioButton(self.new_customer_page)
        self.student_person_radioBT.setObjectName(u"student_person_radioBT")
        self.student_person_radioBT.setGeometry(QRect(880, 20, 161, 51))
        self.student_person_radioBT.setFont(font2)
        self.color_fram_new_custommer1 = QWidget(self.new_customer_page)
        self.color_fram_new_custommer1.setObjectName(u"color_fram_new_custommer1")
        self.color_fram_new_custommer1.setGeometry(QRect(40, 90, 941, 739))
        self.color_fram_new_custommer1.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0)\n"
"}")
        self.color_fram_new_custommer2 = QWidget(self.color_fram_new_custommer1)
        self.color_fram_new_custommer2.setObjectName(u"color_fram_new_custommer2")
        self.color_fram_new_custommer2.setGeometry(QRect(9, 9, 923, 721))
        self.color_fram_new_custommer2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(245, 255, 229)\n"
"}")
        self.title_name_label = QLabel(self.color_fram_new_custommer2)
        self.title_name_label.setObjectName(u"title_name_label")
        self.title_name_label.setGeometry(QRect(10, 20, 111, 41))
        font3 = QFont()
        font3.setFamilies([u"TH Niramit AS"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.title_name_label.setFont(font3)
        self.name_label = QLabel(self.color_fram_new_custommer2)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(390, 20, 111, 41))
        self.name_label.setFont(font3)
        self.surename_label = QLabel(self.color_fram_new_custommer2)
        self.surename_label.setObjectName(u"surename_label")
        self.surename_label.setGeometry(QRect(10, 90, 111, 41))
        self.surename_label.setFont(font3)
        self.tax_label = QLabel(self.color_fram_new_custommer2)
        self.tax_label.setObjectName(u"tax_label")
        self.tax_label.setGeometry(QRect(10, 160, 201, 41))
        self.tax_label.setFont(font3)
        self.email_label = QLabel(self.color_fram_new_custommer2)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setGeometry(QRect(10, 280, 111, 41))
        self.email_label.setFont(font3)
        self.line_id_label = QLabel(self.color_fram_new_custommer2)
        self.line_id_label.setObjectName(u"line_id_label")
        self.line_id_label.setGeometry(QRect(500, 280, 111, 41))
        self.line_id_label.setFont(font3)
        self.phone_label = QLabel(self.color_fram_new_custommer2)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setGeometry(QRect(10, 360, 111, 41))
        self.phone_label.setFont(font3)
        self.address_label = QLabel(self.color_fram_new_custommer2)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(10, 430, 161, 41))
        self.address_label.setFont(font3)
        self.address_for_bill_label = QLabel(self.color_fram_new_custommer2)
        self.address_for_bill_label.setObjectName(u"address_for_bill_label")
        self.address_for_bill_label.setGeometry(QRect(10, 560, 201, 41))
        self.address_for_bill_label.setFont(font3)
        self.title_name_entry = QLineEdit(self.color_fram_new_custommer2)
        self.title_name_entry.setObjectName(u"title_name_entry")
        self.title_name_entry.setGeometry(QRect(170, 20, 211, 41))
        self.title_name_entry.setFont(font3)
        self.title_name_entry.setAutoFillBackground(False)
        self.title_name_entry.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.name_entry = QLineEdit(self.color_fram_new_custommer2)
        self.name_entry.setObjectName(u"name_entry")
        self.name_entry.setGeometry(QRect(480, 20, 431, 41))
        self.name_entry.setFont(font3)
        self.name_entry.setAutoFillBackground(False)
        self.name_entry.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.surename_entry = QLineEdit(self.color_fram_new_custommer2)
        self.surename_entry.setObjectName(u"surename_entry")
        self.surename_entry.setGeometry(QRect(170, 90, 561, 41))
        self.surename_entry.setFont(font3)
        self.surename_entry.setAutoFillBackground(False)
        self.surename_entry.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.tax_entry = QLineEdit(self.color_fram_new_custommer2)
        self.tax_entry.setObjectName(u"tax_entry")
        self.tax_entry.setGeometry(QRect(170, 210, 561, 41))
        self.tax_entry.setFont(font3)
        self.tax_entry.setAutoFillBackground(False)
        self.tax_entry.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.email_entry = QLineEdit(self.color_fram_new_custommer2)
        self.email_entry.setObjectName(u"email_entry")
        self.email_entry.setGeometry(QRect(170, 280, 321, 41))
        self.email_entry.setFont(font3)
        self.email_entry.setAutoFillBackground(False)
        self.email_entry.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.line_entry = QLineEdit(self.color_fram_new_custommer2)
        self.line_entry.setObjectName(u"line_entry")
        self.line_entry.setGeometry(QRect(580, 280, 321, 41))
        self.line_entry.setFont(font3)
        self.line_entry.setAutoFillBackground(False)
        self.line_entry.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.phone_entry = QLineEdit(self.color_fram_new_custommer2)
        self.phone_entry.setObjectName(u"phone_entry")
        self.phone_entry.setGeometry(QRect(170, 360, 561, 41))
        self.phone_entry.setFont(font3)
        self.phone_entry.setAutoFillBackground(False)
        self.phone_entry.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.address_entry = QTextEdit(self.color_fram_new_custommer2)
        self.address_entry.setObjectName(u"address_entry")
        self.address_entry.setGeometry(QRect(170, 440, 561, 101))
        self.address_entry.setFont(font3)
        self.address_entry.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.address_for_bill_entry = QTextEdit(self.color_fram_new_custommer2)
        self.address_for_bill_entry.setObjectName(u"address_for_bill_entry")
        self.address_for_bill_entry.setGeometry(QRect(170, 610, 561, 101))
        self.address_for_bill_entry.setFont(font3)
        self.address_for_bill_entry.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255)\n"
"}")
        self.addres_for_bill_checkbox = QCheckBox(self.color_fram_new_custommer2)
        self.addres_for_bill_checkbox.setObjectName(u"addres_for_bill_checkbox")
        self.addres_for_bill_checkbox.setGeometry(QRect(230, 560, 391, 41))
        self.addres_for_bill_checkbox.setFont(font3)
        self.anonymous_tax_checkbox = QCheckBox(self.color_fram_new_custommer2)
        self.anonymous_tax_checkbox.setObjectName(u"anonymous_tax_checkbox")
        self.anonymous_tax_checkbox.setGeometry(QRect(230, 160, 391, 41))
        self.anonymous_tax_checkbox.setFont(font3)
        self.save_data_button = QPushButton(self.new_customer_page)
        self.save_data_button.setObjectName(u"save_data_button")
        self.save_data_button.setGeometry(QRect(1000, 90, 181, 81))
        self.save_data_button.setFont(font3)
        self.back_to_home_button = QPushButton(self.new_customer_page)
        self.back_to_home_button.setObjectName(u"back_to_home_button")
        self.back_to_home_button.setGeometry(QRect(1000, 180, 181, 81))
        self.back_to_home_button.setFont(font3)
        self.stackedWidget.addWidget(self.new_customer_page)
        self.new_job_page = QWidget()
        self.new_job_page.setObjectName(u"new_job_page")
        self.search_label = QLabel(self.new_job_page)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setGeometry(QRect(0, 0, 181, 31))
        self.search_label.setFont(font3)
        self.search_name_entry = QLineEdit(self.new_job_page)
        self.search_name_entry.setObjectName(u"search_name_entry")
        self.search_name_entry.setGeometry(QRect(140, 40, 391, 31))
        self.search_name_entry.setFont(font)
        self.search_name_label = QLabel(self.new_job_page)
        self.search_name_label.setObjectName(u"search_name_label")
        self.search_name_label.setGeometry(QRect(0, 40, 141, 31))
        self.search_name_label.setFont(font3)
        self.search_button = QPushButton(self.new_job_page)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(540, 22, 111, 51))
        font4 = QFont()
        font4.setFamilies([u"TH Niramit AS"])
        font4.setPointSize(24)
        font4.setBold(True)
        self.search_button.setFont(font4)
        self.search_tree_view = QTreeWidget(self.new_job_page)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font1);
        self.search_tree_view.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.search_tree_view)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.search_tree_view)
        QTreeWidgetItem(__qtreewidgetitem2)
        self.search_tree_view.setObjectName(u"search_tree_view")
        self.search_tree_view.setGeometry(QRect(0, 90, 651, 171))
        font5 = QFont()
        font5.setFamilies([u"TH Niramit AS"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.search_tree_view.setFont(font5)
        self.search_tree_view.setAutoScrollMargin(18)
        self.search_tree_view.setTextElideMode(Qt.ElideRight)
        self.search_tree_view.setIndentation(15)
        self.search_tree_view.setColumnCount(5)
        self.search_tree_view.header().setMinimumSectionSize(38)
        self.search_tree_view.header().setDefaultSectionSize(129)
        self.number_job_label = QLabel(self.new_job_page)
        self.number_job_label.setObjectName(u"number_job_label")
        self.number_job_label.setGeometry(QRect(0, 280, 91, 31))
        self.number_job_label.setFont(font3)
        self.number_job_entry = QLineEdit(self.new_job_page)
        self.number_job_entry.setObjectName(u"number_job_entry")
        self.number_job_entry.setGeometry(QRect(150, 280, 151, 31))
        self.number_job_entry.setFont(font)
        self.number_sender_label = QLabel(self.new_job_page)
        self.number_sender_label.setObjectName(u"number_sender_label")
        self.number_sender_label.setGeometry(QRect(0, 320, 121, 31))
        self.number_sender_label.setFont(font3)
        self.number_sender_entry = QLineEdit(self.new_job_page)
        self.number_sender_entry.setObjectName(u"number_sender_entry")
        self.number_sender_entry.setGeometry(QRect(150, 320, 131, 31))
        self.number_sender_entry.setFont(font)
        self.name_sender_label = QLabel(self.new_job_page)
        self.name_sender_label.setObjectName(u"name_sender_label")
        self.name_sender_label.setGeometry(QRect(290, 320, 31, 31))
        self.name_sender_label.setFont(font3)
        self.name_sender_entry = QLineEdit(self.new_job_page)
        self.name_sender_entry.setObjectName(u"name_sender_entry")
        self.name_sender_entry.setGeometry(QRect(320, 320, 211, 31))
        self.name_sender_entry.setFont(font)
        self.surename_sender_label = QLabel(self.new_job_page)
        self.surename_sender_label.setObjectName(u"surename_sender_label")
        self.surename_sender_label.setGeometry(QRect(540, 320, 81, 31))
        self.surename_sender_label.setFont(font3)
        self.surename_sender_entry = QLineEdit(self.new_job_page)
        self.surename_sender_entry.setObjectName(u"surename_sender_entry")
        self.surename_sender_entry.setGeometry(QRect(620, 320, 231, 31))
        self.surename_sender_entry.setFont(font)
        self.tax_sender_label = QLabel(self.new_job_page)
        self.tax_sender_label.setObjectName(u"tax_sender_label")
        self.tax_sender_label.setGeometry(QRect(860, 320, 101, 31))
        self.tax_sender_label.setFont(font3)
        self.tax_sender_entry = QLineEdit(self.new_job_page)
        self.tax_sender_entry.setObjectName(u"tax_sender_entry")
        self.tax_sender_entry.setGeometry(QRect(970, 320, 211, 31))
        self.tax_sender_entry.setFont(font)
        self.number_owner_label = QLabel(self.new_job_page)
        self.number_owner_label.setObjectName(u"number_owner_label")
        self.number_owner_label.setGeometry(QRect(0, 360, 151, 31))
        self.number_owner_label.setFont(font3)
        self.number_owner_entry = QLineEdit(self.new_job_page)
        self.number_owner_entry.setObjectName(u"number_owner_entry")
        self.number_owner_entry.setGeometry(QRect(150, 360, 131, 31))
        self.number_owner_entry.setFont(font)
        self.name_owner_label = QLabel(self.new_job_page)
        self.name_owner_label.setObjectName(u"name_owner_label")
        self.name_owner_label.setGeometry(QRect(290, 360, 31, 31))
        self.name_owner_label.setFont(font3)
        self.name_owner_entry = QLineEdit(self.new_job_page)
        self.name_owner_entry.setObjectName(u"name_owner_entry")
        self.name_owner_entry.setGeometry(QRect(320, 360, 211, 31))
        self.name_owner_entry.setFont(font)
        self.surename_owner_label = QLabel(self.new_job_page)
        self.surename_owner_label.setObjectName(u"surename_owner_label")
        self.surename_owner_label.setGeometry(QRect(540, 360, 81, 31))
        self.surename_owner_label.setFont(font3)
        self.surename_owner_entry = QLineEdit(self.new_job_page)
        self.surename_owner_entry.setObjectName(u"surename_owner_entry")
        self.surename_owner_entry.setGeometry(QRect(620, 360, 231, 31))
        self.surename_owner_entry.setFont(font)
        self.tax_owner_label = QLabel(self.new_job_page)
        self.tax_owner_label.setObjectName(u"tax_owner_label")
        self.tax_owner_label.setGeometry(QRect(860, 360, 101, 31))
        self.tax_owner_label.setFont(font3)
        self.tax_owner_entry = QLineEdit(self.new_job_page)
        self.tax_owner_entry.setObjectName(u"tax_owner_entry")
        self.tax_owner_entry.setGeometry(QRect(970, 360, 211, 31))
        self.tax_owner_entry.setFont(font)
        self.name_projact_label = QLabel(self.new_job_page)
        self.name_projact_label.setObjectName(u"name_projact_label")
        self.name_projact_label.setGeometry(QRect(0, 410, 101, 31))
        self.name_projact_label.setFont(font3)
        self.name_projact_entry = QLineEdit(self.new_job_page)
        self.name_projact_entry.setObjectName(u"name_projact_entry")
        self.name_projact_entry.setGeometry(QRect(150, 410, 1031, 31))
        self.name_projact_entry.setFont(font)
        self.detail_case_tree_view = QTreeWidget(self.new_job_page)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setTextAlignment(6, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(5, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(4, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(3, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem3.setTextAlignment(0, Qt.AlignCenter);
        self.detail_case_tree_view.setHeaderItem(__qtreewidgetitem3)
        __qtreewidgetitem4 = QTreeWidgetItem(self.detail_case_tree_view)
        QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5 = QTreeWidgetItem(self.detail_case_tree_view)
        QTreeWidgetItem(__qtreewidgetitem5)
        self.detail_case_tree_view.setObjectName(u"detail_case_tree_view")
        self.detail_case_tree_view.setGeometry(QRect(10, 460, 991, 371))
        self.detail_case_tree_view.setFont(font1)
        self.detail_case_tree_view.header().setDefaultSectionSize(144)
        self.select_sender_button = QPushButton(self.new_job_page)
        self.select_sender_button.setObjectName(u"select_sender_button")
        self.select_sender_button.setGeometry(QRect(790, 20, 181, 61))
        self.select_sender_button.setFont(font4)
        self.select_owner_button = QPushButton(self.new_job_page)
        self.select_owner_button.setObjectName(u"select_owner_button")
        self.select_owner_button.setGeometry(QRect(790, 110, 181, 61))
        self.select_owner_button.setFont(font4)
        self.anonymous_owner_button = QPushButton(self.new_job_page)
        self.anonymous_owner_button.setObjectName(u"anonymous_owner_button")
        self.anonymous_owner_button.setGeometry(QRect(790, 200, 181, 61))
        self.anonymous_owner_button.setFont(font4)
        self.save_button = QPushButton(self.new_job_page)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(990, 20, 181, 61))
        self.save_button.setFont(font4)
        self.add_data_specimen_button = QPushButton(self.new_job_page)
        self.add_data_specimen_button.setObjectName(u"add_data_specimen_button")
        self.add_data_specimen_button.setGeometry(QRect(1010, 460, 171, 61))
        self.add_data_specimen_button.setFont(font1)
        self.delete_data_specimen_button = QPushButton(self.new_job_page)
        self.delete_data_specimen_button.setObjectName(u"delete_data_specimen_button")
        self.delete_data_specimen_button.setGeometry(QRect(1010, 530, 171, 61))
        self.delete_data_specimen_button.setFont(font1)
        self.print_sticker_button = QPushButton(self.new_job_page)
        self.print_sticker_button.setObjectName(u"print_sticker_button")
        self.print_sticker_button.setGeometry(QRect(1010, 600, 171, 61))
        self.print_sticker_button.setFont(font1)
        self.print_lab_report_button = QPushButton(self.new_job_page)
        self.print_lab_report_button.setObjectName(u"print_lab_report_button")
        self.print_lab_report_button.setGeometry(QRect(1010, 670, 171, 61))
        self.print_lab_report_button.setFont(font1)
        self.back_to_home = QPushButton(self.new_job_page)
        self.back_to_home.setObjectName(u"back_to_home")
        self.back_to_home.setGeometry(QRect(1010, 770, 171, 61))
        self.back_to_home.setFont(font1)
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
        self.current_user_label.setGeometry(QRect(748, 10, 441, 20))
        self.current_user_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        main_app_view.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_app_view)

        self.stackedWidget.setCurrentIndex(2)


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
        self.legal_person_radioBT.setText(QCoreApplication.translate("main_app_view", u"\u0e19\u0e34\u0e15\u0e34\u0e1a\u0e38\u0e04\u0e04\u0e25", None))
        self.nomal_person_radioBT.setText(QCoreApplication.translate("main_app_view", u"\u0e1a\u0e38\u0e04\u0e04\u0e25\u0e18\u0e23\u0e23\u0e21\u0e14\u0e32", None))
        self.internal_person_radioBT.setText(QCoreApplication.translate("main_app_view", u"\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e07\u0e32\u0e19\u0e20\u0e32\u0e22\u0e43\u0e19", None))
        self.professor_person_radioBT.setText(QCoreApplication.translate("main_app_view", u"\u0e2d\u0e32\u0e08\u0e32\u0e23\u0e22\u0e4c\u0e43\u0e19\u0e04\u0e13\u0e30", None))
        self.student_person_radioBT.setText(QCoreApplication.translate("main_app_view", u"\u0e19\u0e31\u0e01\u0e28\u0e36\u0e01\u0e29\u0e32", None))
        self.title_name_label.setText(QCoreApplication.translate("main_app_view", u"\u0e04\u0e33\u0e19\u0e33\u0e2b\u0e19\u0e49\u0e32\u0e0a\u0e37\u0e48\u0e2d", None))
        self.name_label.setText(QCoreApplication.translate("main_app_view", u"\u0e0a\u0e37\u0e48\u0e2d\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32", None))
        self.surename_label.setText(QCoreApplication.translate("main_app_view", u"\u0e19\u0e32\u0e21\u0e2a\u0e01\u0e38\u0e25", None))
        self.tax_label.setText(QCoreApplication.translate("main_app_view", u"\u0e40\u0e25\u0e02\u0e1b\u0e23\u0e30\u0e08\u0e33\u0e15\u0e31\u0e27\u0e1c\u0e39\u0e49\u0e40\u0e2a\u0e35\u0e22\u0e20\u0e32\u0e29\u0e35", None))
        self.email_label.setText(QCoreApplication.translate("main_app_view", u"EMAIL", None))
        self.line_id_label.setText(QCoreApplication.translate("main_app_view", u"LINE ID", None))
        self.phone_label.setText(QCoreApplication.translate("main_app_view", u"\u0e40\u0e1a\u0e2d\u0e23\u0e4c\u0e42\u0e17\u0e23", None))
        self.address_label.setText(QCoreApplication.translate("main_app_view", u"\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d", None))
        self.address_for_bill_label.setText(QCoreApplication.translate("main_app_view", u"\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e2d\u0e2d\u0e01\u0e43\u0e1a\u0e40\u0e2a\u0e23\u0e47\u0e08", None))
        self.addres_for_bill_checkbox.setText(QCoreApplication.translate("main_app_view", u"\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e40\u0e14\u0e35\u0e22\u0e27\u0e01\u0e31\u0e1a\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e2a\u0e33\u0e2b\u0e23\u0e31\u0e1a\u0e15\u0e34\u0e14\u0e15\u0e48\u0e2d", None))
        self.anonymous_tax_checkbox.setText(QCoreApplication.translate("main_app_view", u"\u0e44\u0e21\u0e48\u0e23\u0e30\u0e1a\u0e38\u0e40\u0e25\u0e02\u0e1b\u0e23\u0e30\u0e08\u0e33\u0e15\u0e31\u0e27\u0e1c\u0e39\u0e49\u0e40\u0e2a\u0e35\u0e22\u0e20\u0e32\u0e29\u0e35", None))
        self.save_data_button.setText(QCoreApplication.translate("main_app_view", u"\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32", None))
        self.back_to_home_button.setText(QCoreApplication.translate("main_app_view", u"\u0e01\u0e25\u0e31\u0e1a\u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e25\u0e31\u0e01", None))
        self.search_label.setText(QCoreApplication.translate("main_app_view", u"\u0e04\u0e49\u0e19\u0e2b\u0e32\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32", None))
        self.search_name_label.setText(QCoreApplication.translate("main_app_view", u"\u0e0a\u0e37\u0e48\u0e2d\u0e2b\u0e23\u0e37\u0e2d\u0e19\u0e32\u0e21\u0e2a\u0e01\u0e38\u0e25", None))
        self.search_button.setText(QCoreApplication.translate("main_app_view", u"\u0e04\u0e49\u0e19\u0e2b\u0e32", None))
        ___qtreewidgetitem = self.search_tree_view.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("main_app_view", u"\u0e40\u0e25\u0e02\u0e1c\u0e39\u0e49\u0e40\u0e2a\u0e35\u0e22\u0e20\u0e32\u0e29\u0e35", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("main_app_view", u"\u0e2d\u0e32\u0e22\u0e38", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("main_app_view", u"\u0e19\u0e32\u0e21\u0e2a\u0e01\u0e38\u0e25", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("main_app_view", u"\u0e0a\u0e37\u0e48\u0e2d", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("main_app_view", u"\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e25\u0e02\u0e1b\u0e23\u0e30\u0e08\u0e33\u0e15\u0e31\u0e27", None));

        __sortingEnabled = self.search_tree_view.isSortingEnabled()
        self.search_tree_view.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.search_tree_view.topLevelItem(0)
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("main_app_view", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("main_app_view", u"111", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("main_app_view", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("main_app_view", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("main_app_view", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("main_app_view", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a1", None));
        ___qtreewidgetitem3 = self.search_tree_view.topLevelItem(1)
        ___qtreewidgetitem3.setText(4, QCoreApplication.translate("main_app_view", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a2", None));
        ___qtreewidgetitem3.setText(3, QCoreApplication.translate("main_app_view", u"222", None));
        ___qtreewidgetitem3.setText(2, QCoreApplication.translate("main_app_view", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a2", None));
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("main_app_view", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a2", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("main_app_view", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a2", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem3.child(0)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("main_app_view", u"\u0e17\u0e14\u0e2a\u0e2d\u0e1a2", None));
        self.search_tree_view.setSortingEnabled(__sortingEnabled)

        self.number_job_label.setText(QCoreApplication.translate("main_app_view", u"\u0e40\u0e25\u0e02\u0e17\u0e35\u0e48\u0e07\u0e32\u0e19", None))
        self.number_sender_label.setText(QCoreApplication.translate("main_app_view", u"\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e25\u0e02\u0e1c\u0e39\u0e49\u0e2a\u0e48\u0e07", None))
        self.name_sender_label.setText(QCoreApplication.translate("main_app_view", u"\u0e0a\u0e37\u0e48\u0e2d", None))
        self.surename_sender_label.setText(QCoreApplication.translate("main_app_view", u"\u0e19\u0e32\u0e21\u0e2a\u0e01\u0e38\u0e25", None))
        self.tax_sender_label.setText(QCoreApplication.translate("main_app_view", u"\u0e40\u0e25\u0e02\u0e40\u0e2a\u0e35\u0e22\u0e20\u0e32\u0e29\u0e35", None))
        self.number_owner_label.setText(QCoreApplication.translate("main_app_view", u"\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e25\u0e02\u0e40\u0e08\u0e49\u0e32\u0e02\u0e2d\u0e07", None))
        self.name_owner_label.setText(QCoreApplication.translate("main_app_view", u"\u0e0a\u0e37\u0e48\u0e2d", None))
        self.surename_owner_label.setText(QCoreApplication.translate("main_app_view", u"\u0e19\u0e32\u0e21\u0e2a\u0e01\u0e38\u0e25", None))
        self.tax_owner_label.setText(QCoreApplication.translate("main_app_view", u"\u0e40\u0e25\u0e02\u0e40\u0e2a\u0e35\u0e22\u0e20\u0e32\u0e29\u0e35", None))
        self.name_projact_label.setText(QCoreApplication.translate("main_app_view", u"\u0e0a\u0e37\u0e48\u0e2d\u0e42\u0e04\u0e23\u0e07\u0e01\u0e32\u0e23", None))
        ___qtreewidgetitem5 = self.detail_case_tree_view.headerItem()
        ___qtreewidgetitem5.setText(6, QCoreApplication.translate("main_app_view", u"\u0e04\u0e33\u0e2d\u0e18\u0e34\u0e1a\u0e32\u0e22", None));
        ___qtreewidgetitem5.setText(5, QCoreApplication.translate("main_app_view", u"\u0e2b\u0e49\u0e2d\u0e07\u0e1b\u0e0f\u0e34\u0e1a\u0e31\u0e15\u0e34\u0e01\u0e32\u0e23", None));
        ___qtreewidgetitem5.setText(4, QCoreApplication.translate("main_app_view", u"\u0e01\u0e32\u0e23\u0e40\u0e01\u0e47\u0e1a\u0e23\u0e31\u0e01\u0e29\u0e32", None));
        ___qtreewidgetitem5.setText(3, QCoreApplication.translate("main_app_view", u"\u0e2a\u0e16\u0e32\u0e19\u0e30", None));
        ___qtreewidgetitem5.setText(2, QCoreApplication.translate("main_app_view", u"\u0e1b\u0e23\u0e30\u0e40\u0e20\u0e17\u0e2a\u0e31\u0e15\u0e27\u0e4c", None));
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("main_app_view", u"Barcode", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("main_app_view", u"\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e23\u0e31\u0e1a", None));

        __sortingEnabled1 = self.detail_case_tree_view.isSortingEnabled()
        self.detail_case_tree_view.setSortingEnabled(False)
        ___qtreewidgetitem6 = self.detail_case_tree_view.topLevelItem(0)
        ___qtreewidgetitem6.setText(6, QCoreApplication.translate("main_app_view", u"refsdfewf", None));
        ___qtreewidgetitem6.setText(5, QCoreApplication.translate("main_app_view", u"eeeee", None));
        ___qtreewidgetitem6.setText(4, QCoreApplication.translate("main_app_view", u"wwwww", None));
        ___qtreewidgetitem6.setText(3, QCoreApplication.translate("main_app_view", u"qqqq", None));
        ___qtreewidgetitem6.setText(2, QCoreApplication.translate("main_app_view", u"aaaaaa", None));
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("main_app_view", u"02847493", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("main_app_view", u"1111", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem6.child(0)
        ___qtreewidgetitem7.setText(6, QCoreApplication.translate("main_app_view", u"77", None));
        ___qtreewidgetitem7.setText(5, QCoreApplication.translate("main_app_view", u"666", None));
        ___qtreewidgetitem7.setText(4, QCoreApplication.translate("main_app_view", u"555", None));
        ___qtreewidgetitem7.setText(3, QCoreApplication.translate("main_app_view", u"444", None));
        ___qtreewidgetitem7.setText(2, QCoreApplication.translate("main_app_view", u"333", None));
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("main_app_view", u"333", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("main_app_view", u"222", None));
        ___qtreewidgetitem8 = self.detail_case_tree_view.topLevelItem(1)
        ___qtreewidgetitem8.setText(6, QCoreApplication.translate("main_app_view", u"dfgdfg", None));
        ___qtreewidgetitem8.setText(5, QCoreApplication.translate("main_app_view", u"jjjjj", None));
        ___qtreewidgetitem8.setText(4, QCoreApplication.translate("main_app_view", u"hhhh", None));
        ___qtreewidgetitem8.setText(3, QCoreApplication.translate("main_app_view", u"ggggg", None));
        ___qtreewidgetitem8.setText(2, QCoreApplication.translate("main_app_view", u"fffff", None));
        ___qtreewidgetitem8.setText(1, QCoreApplication.translate("main_app_view", u"324234234", None));
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("main_app_view", u"2222", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem8.child(0)
        ___qtreewidgetitem9.setText(6, QCoreApplication.translate("main_app_view", u"xxxx", None));
        ___qtreewidgetitem9.setText(5, QCoreApplication.translate("main_app_view", u"cccc", None));
        ___qtreewidgetitem9.setText(4, QCoreApplication.translate("main_app_view", u"hhhh", None));
        ___qtreewidgetitem9.setText(3, QCoreApplication.translate("main_app_view", u"b  bbb", None));
        ___qtreewidgetitem9.setText(2, QCoreApplication.translate("main_app_view", u"dddd", None));
        ___qtreewidgetitem9.setText(1, QCoreApplication.translate("main_app_view", u"hfff", None));
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("main_app_view", u"hhh", None));
        self.detail_case_tree_view.setSortingEnabled(__sortingEnabled1)

        self.select_sender_button.setText(QCoreApplication.translate("main_app_view", u"\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e1c\u0e39\u0e49\u0e2a\u0e48\u0e07", None))
        self.select_owner_button.setText(QCoreApplication.translate("main_app_view", u"\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e40\u0e08\u0e49\u0e32\u0e02\u0e2d\u0e07", None))
        self.anonymous_owner_button.setText(QCoreApplication.translate("main_app_view", u"\u0e44\u0e21\u0e48\u0e23\u0e30\u0e1a\u0e38\u0e40\u0e08\u0e49\u0e32\u0e02\u0e2d\u0e07", None))
        self.save_button.setText(QCoreApplication.translate("main_app_view", u"\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))
        self.add_data_specimen_button.setText(QCoreApplication.translate("main_app_view", u"\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e2a\u0e34\u0e48\u0e07\u0e2a\u0e48\u0e07\u0e15\u0e23\u0e27\u0e08", None))
        self.delete_data_specimen_button.setText(QCoreApplication.translate("main_app_view", u"\u0e25\u0e1a\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e2a\u0e34\u0e48\u0e07\u0e2a\u0e48\u0e07\u0e15\u0e23\u0e27\u0e08", None))
        self.print_sticker_button.setText(QCoreApplication.translate("main_app_view", u"\u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e2a\u0e15\u0e34\u0e01\u0e40\u0e01\u0e2d\u0e23\u0e4c", None))
        self.print_lab_report_button.setText(QCoreApplication.translate("main_app_view", u"\u0e1e\u0e34\u0e21\u0e1e\u0e4c\u0e43\u0e1a\u0e2a\u0e48\u0e07\u0e41\u0e25\u0e1b", None))
        self.back_to_home.setText(QCoreApplication.translate("main_app_view", u"\u0e01\u0e25\u0e31\u0e1a\u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e25\u0e31\u0e01", None))
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

