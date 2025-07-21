# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginPage.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(320, 348)
        self.centralwidget = QWidget(LoginPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_LoginPage = QLabel(self.centralwidget)
        self.label_LoginPage.setObjectName(u"label_LoginPage")
        self.label_LoginPage.setGeometry(QRect(20, 20, 280, 20))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_LoginPage.setFont(font)
        self.label_Username = QLabel(self.centralwidget)
        self.label_Username.setObjectName(u"label_Username")
        self.label_Username.setGeometry(QRect(90, 70, 141, 16))
        self.label_Password = QLabel(self.centralwidget)
        self.label_Password.setObjectName(u"label_Password")
        self.label_Password.setGeometry(QRect(90, 140, 141, 16))
        self.error_Username_or_Password = QLabel(self.centralwidget)
        self.error_Username_or_Password.setObjectName(u"error_Username_or_Password")
        self.error_Username_or_Password.setGeometry(QRect(90, 185, 200, 16))
        self.lineEdit_Username = QLineEdit(self.centralwidget)
        self.lineEdit_Username.setObjectName(u"lineEdit_Username")
        self.lineEdit_Username.setGeometry(QRect(90, 90, 140, 21))
        self.lineEdit_Password = QLineEdit(self.centralwidget)
        self.lineEdit_Password.setObjectName(u"lineEdit_Password")
        self.lineEdit_Password.setGeometry(QRect(90, 160, 140, 21))
        self.LoginButton = QPushButton(self.centralwidget)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(110, 240, 100, 30))
        self.LoginButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.FirstUseButton = QPushButton(self.centralwidget)
        self.FirstUseButton.setObjectName(u"FirstUseButton")
        self.FirstUseButton.setGeometry(QRect(10, 280, 75, 24))
        self.FirstUseButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_goodbye_user = QLabel(self.centralwidget)
        self.label_goodbye_user.setObjectName(u"label_goodbye_user")
        self.label_goodbye_user.setGeometry(QRect(190, 20, 121, 20))
        self.label_Forgot_Password = QLabel(self.centralwidget)
        self.label_Forgot_Password.setObjectName(u"label_Forgot_Password")
        self.label_Forgot_Password.setGeometry(QRect(90, 210, 140, 16))
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoginPage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 320, 22))
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginPage)
        self.statusbar.setObjectName(u"statusbar")
        LoginPage.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_Username, self.lineEdit_Password)
        QWidget.setTabOrder(self.lineEdit_Password, self.LoginButton)
        QWidget.setTabOrder(self.LoginButton, self.FirstUseButton)

        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"Login Page", None))
        self.label_LoginPage.setText(QCoreApplication.translate("LoginPage", u"Login Page", None))
        self.label_Username.setText(QCoreApplication.translate("LoginPage", u"Username", None))
        self.label_Password.setText(QCoreApplication.translate("LoginPage", u"Password", None))
        self.error_Username_or_Password.setText(QCoreApplication.translate("LoginPage", u"error_Username_or_Password", None))
        self.LoginButton.setText(QCoreApplication.translate("LoginPage", u"Login", None))
        self.FirstUseButton.setText(QCoreApplication.translate("LoginPage", u"First Use", None))
        self.label_goodbye_user.setText(QCoreApplication.translate("LoginPage", u"Goodbye, User's Name", None))
        self.label_Forgot_Password.setText(QCoreApplication.translate("LoginPage", u"Forgot_Password", None))
    # retranslateUi

