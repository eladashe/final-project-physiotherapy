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
    QFont, QFontDatabase, QGradient, QIcon, QAction,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)
from FirstUsePage import Ui_MainWindow as Ui_FirstUsePage
from TestParametersPage import Ui_MainWindow as Ui_TestParameters


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 380)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # ===== Title
        self.label_LoginPage = QLabel(self.centralwidget)
        self.label_LoginPage.setObjectName(u"label_LoginPage")
        self.label_LoginPage.setGeometry(QRect(80, 20, 191, 51))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label_LoginPage.setFont(font)

        # ===== Username
        self.label_Username = QLabel(self.centralwidget)
        self.label_Username.setObjectName(u"label_Username")
        self.label_Username.setGeometry(QRect(90, 100, 100, 16))

        self.lineEdit_Username = QLineEdit(self.centralwidget)
        self.lineEdit_Username.setObjectName(u"lineEdit_Username")
        self.lineEdit_Username.setGeometry(QRect(90, 120, 140, 21))

        self.error_Username = QLabel("", self.centralwidget)
        self.error_Username.setObjectName(u"error_Username")
        self.error_Username.setGeometry(QRect(90, 145, 200, 16))
        # self.error_Username.setStyleSheet("color: red")
        # self.error_Username.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # self.error_Username.hide()

        # ===== Password
        self.label_Password = QLabel(self.centralwidget)
        self.label_Password.setObjectName(u"label_Password")
        self.label_Password.setGeometry(QRect(90, 170, 100, 16))

        self.lineEdit_Password = QLineEdit(self.centralwidget)
        self.lineEdit_Password.setObjectName(u"lineEdit_Password")
        self.lineEdit_Password.setGeometry(QRect(90, 190, 140, 21))
        # self.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)

        self.error_Password = QLabel("", self.centralwidget)
        self.error_Password.setObjectName(u"error_Password")
        self.error_Password.setGeometry(QRect(90, 215, 200, 16))
        # self.error_Password.setStyleSheet("color: red")
        # self.error_Password.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # self.error_Password.hide()

        # ===== Login Button
        self.LoginButton = QPushButton(self.centralwidget)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(110, 260, 100, 30))
        # self.LoginButton.clicked.connect(self.load_test_parameters_page)
        self.LoginButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))

        # ===== First Use Button
        self.FirstUseButton = QPushButton(self.centralwidget)
        self.FirstUseButton.setObjectName(u"FirstUseButton")
        self.FirstUseButton.setGeometry(QRect(10, 300, 75, 24))
        # self.FirstUseButton.clicked.connect(self.load_first_use_page)
        self.FirstUseButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))

        # ===== Eye icon
        # self.icon_eye_open = QIcon("eye_open.png")
        # self.icon_eye_closed = QIcon("eye_closed.png")
        # self.eye_action = QAction()
        # self.eye_action.setIcon(self.icon_eye_closed)
        # self.eye_action.setCheckable(True)
        # self.eye_action.toggled.connect(self.toggle_password_visibility)
        # self.lineEdit_Password.addAction(self.eye_action, QLineEdit.ActionPosition.TrailingPosition)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_LoginPage.setText(QCoreApplication.translate("MainWindow", u"Login Page", None))
        self.label_Username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_Password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.error_Username.setText(QCoreApplication.translate("MainWindow", u"error_Username", None))
        self.error_Password.setText(QCoreApplication.translate("MainWindow", u"error_Password", None))
        self.LoginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.FirstUseButton.setText(QCoreApplication.translate("MainWindow", u"First Use", None))
    # retranslateUi

