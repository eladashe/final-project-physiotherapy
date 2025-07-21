# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResetPasswordPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_ResetPasswordPage(object):
    def setupUi(self, ResetPasswordPage):
        if not ResetPasswordPage.objectName():
            ResetPasswordPage.setObjectName(u"ResetPasswordPage")
        ResetPasswordPage.resize(340, 268)
        self.centralwidget = QWidget(ResetPasswordPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_Title = QLabel(self.centralwidget)
        self.label_Title.setObjectName(u"label_Title")
        self.label_Title.setGeometry(QRect(20, 20, 300, 21))
        font = QFont()
        font.setBold(True)
        self.label_Title.setFont(font)
        self.ResetPasswordButton = QPushButton(self.centralwidget)
        self.ResetPasswordButton.setObjectName(u"ResetPasswordButton")
        self.ResetPasswordButton.setGeometry(QRect(120, 190, 100, 31))
        self.ResetPasswordButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.lineEdit_Password = QLineEdit(self.centralwidget)
        self.lineEdit_Password.setObjectName(u"lineEdit_Password")
        self.lineEdit_Password.setGeometry(QRect(160, 100, 160, 21))
        self.error_Password = QLabel(self.centralwidget)
        self.error_Password.setObjectName(u"error_Password")
        self.error_Password.setGeometry(QRect(160, 120, 160, 16))
        self.label_Password_Confirmation = QLabel(self.centralwidget)
        self.label_Password_Confirmation.setObjectName(u"label_Password_Confirmation")
        self.label_Password_Confirmation.setGeometry(QRect(20, 140, 300, 21))
        self.label_Password = QLabel(self.centralwidget)
        self.label_Password.setObjectName(u"label_Password")
        self.label_Password.setGeometry(QRect(20, 100, 300, 21))
        self.label_Email = QLabel(self.centralwidget)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setGeometry(QRect(20, 60, 300, 21))
        self.lineEdit_Email = QLineEdit(self.centralwidget)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setGeometry(QRect(160, 60, 160, 21))
        self.error_Email = QLabel(self.centralwidget)
        self.error_Email.setObjectName(u"error_Email")
        self.error_Email.setGeometry(QRect(160, 80, 160, 16))
        self.lineEdit_Password_Confirmation = QLineEdit(self.centralwidget)
        self.lineEdit_Password_Confirmation.setObjectName(u"lineEdit_Password_Confirmation")
        self.lineEdit_Password_Confirmation.setGeometry(QRect(160, 140, 160, 21))
        self.error_Password_Confirmation = QLabel(self.centralwidget)
        self.error_Password_Confirmation.setObjectName(u"error_Password_Confirmation")
        self.error_Password_Confirmation.setGeometry(QRect(160, 160, 160, 16))
        self.comboBoxLanguage = QComboBox(self.centralwidget)
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.setObjectName(u"comboBoxLanguage")
        self.comboBoxLanguage.setGeometry(QRect(252, 20, 68, 22))
        self.comboBoxLanguage.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        ResetPasswordPage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ResetPasswordPage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 340, 22))
        ResetPasswordPage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ResetPasswordPage)
        self.statusbar.setObjectName(u"statusbar")
        ResetPasswordPage.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_Email, self.lineEdit_Password)
        QWidget.setTabOrder(self.lineEdit_Password, self.lineEdit_Password_Confirmation)
        QWidget.setTabOrder(self.lineEdit_Password_Confirmation, self.ResetPasswordButton)

        self.retranslateUi(ResetPasswordPage)

        self.comboBoxLanguage.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(ResetPasswordPage)
    # setupUi

    def retranslateUi(self, ResetPasswordPage):
        ResetPasswordPage.setWindowTitle(QCoreApplication.translate("ResetPasswordPage", u"Reset Password", None))
        self.label_Title.setText(QCoreApplication.translate("ResetPasswordPage", u"Reset Password", None))
        self.ResetPasswordButton.setText(QCoreApplication.translate("ResetPasswordPage", u"Reset Password", None))
        self.error_Password.setText(QCoreApplication.translate("ResetPasswordPage", u"error_Password", None))
        self.label_Password_Confirmation.setText(QCoreApplication.translate("ResetPasswordPage", u"Password Confirmation:", None))
        self.label_Password.setText(QCoreApplication.translate("ResetPasswordPage", u"Password:", None))
        self.label_Email.setText(QCoreApplication.translate("ResetPasswordPage", u"Email:", None))
        self.error_Email.setText(QCoreApplication.translate("ResetPasswordPage", u"error_Email", None))
        self.error_Password_Confirmation.setText(QCoreApplication.translate("ResetPasswordPage", u"error_Password_Confirmation", None))
        self.comboBoxLanguage.setItemText(0, QCoreApplication.translate("ResetPasswordPage", u"English", None))
        self.comboBoxLanguage.setItemText(1, QCoreApplication.translate("ResetPasswordPage", u"\u05e2\u05d1\u05e8\u05d9\u05ea", None))

        self.comboBoxLanguage.setCurrentText("")
    # retranslateUi

