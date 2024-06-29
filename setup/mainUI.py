# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(671, 248)
        font = QFont()
        font.setFamilies([u"TH Niramit AS"])
        font.setPointSize(16)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.serverIPLabel = QLabel(self.centralwidget)
        self.serverIPLabel.setObjectName(u"serverIPLabel")
        self.serverIPLabel.setGeometry(QRect(20, 30, 91, 21))
        self.serverIPLabel.setFont(font)
        self.loadConfigPushButton = QPushButton(self.centralwidget)
        self.loadConfigPushButton.setObjectName(u"loadConfigPushButton")
        self.loadConfigPushButton.setGeometry(QRect(500, 20, 161, 51))
        self.usernameLabel = QLabel(self.centralwidget)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(20, 70, 91, 21))
        self.usernameLabel.setFont(font)
        self.passwordLabel = QLabel(self.centralwidget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(20, 110, 91, 21))
        self.passwordLabel.setFont(font)
        self.serverPathLabel = QLabel(self.centralwidget)
        self.serverPathLabel.setObjectName(u"serverPathLabel")
        self.serverPathLabel.setGeometry(QRect(20, 150, 91, 21))
        self.serverPathLabel.setFont(font)
        self.serverIPLineEdit = QLineEdit(self.centralwidget)
        self.serverIPLineEdit.setObjectName(u"serverIPLineEdit")
        self.serverIPLineEdit.setGeometry(QRect(110, 20, 361, 31))
        self.serverIPLineEdit.setReadOnly(True)
        self.usernameLineEdit = QLineEdit(self.centralwidget)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setGeometry(QRect(110, 60, 361, 31))
        self.usernameLineEdit.setReadOnly(True)
        self.passwordLineEdit = QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setGeometry(QRect(110, 100, 361, 31))
        self.passwordLineEdit.setReadOnly(True)
        self.serverPathLineEdit = QLineEdit(self.centralwidget)
        self.serverPathLineEdit.setObjectName(u"serverPathLineEdit")
        self.serverPathLineEdit.setGeometry(QRect(110, 140, 361, 31))
        self.serverPathLineEdit.setReadOnly(True)
        self.localPathPushButton = QPushButton(self.centralwidget)
        self.localPathPushButton.setObjectName(u"localPathPushButton")
        self.localPathPushButton.setGeometry(QRect(500, 80, 161, 51))
        self.configurePushButton = QPushButton(self.centralwidget)
        self.configurePushButton.setObjectName(u"configurePushButton")
        self.configurePushButton.setGeometry(QRect(500, 160, 161, 51))
        self.localPathLabel = QLabel(self.centralwidget)
        self.localPathLabel.setObjectName(u"localPathLabel")
        self.localPathLabel.setGeometry(QRect(20, 180, 91, 21))
        self.localPathLabel.setFont(font)
        self.localPathLineEdit = QLineEdit(self.centralwidget)
        self.localPathLineEdit.setObjectName(u"localPathLineEdit")
        self.localPathLineEdit.setGeometry(QRect(110, 180, 361, 31))
        self.localPathLineEdit.setReadOnly(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.serverIPLabel.setText(QCoreApplication.translate("MainWindow", u"Server ip", None))
        self.loadConfigPushButton.setText(QCoreApplication.translate("MainWindow", u"Load Config", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.serverPathLabel.setText(QCoreApplication.translate("MainWindow", u"Server path", None))
        self.localPathPushButton.setText(QCoreApplication.translate("MainWindow", u"Local Path", None))
        self.configurePushButton.setText(QCoreApplication.translate("MainWindow", u"Configure", None))
        self.localPathLabel.setText(QCoreApplication.translate("MainWindow", u"Local path", None))
    # retranslateUi

