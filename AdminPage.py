# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AdminPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_AdminPage(object):
    def setupUi(self, AdminPage):
        if not AdminPage.objectName():
            AdminPage.setObjectName(u"AdminPage")
        AdminPage.resize(435, 233)
        self.centralwidget = QWidget(AdminPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.AddButton = QPushButton(self.centralwidget)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setGeometry(QRect(10, 80, 151, 31))
        self.AddButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.RemoveButton = QPushButton(self.centralwidget)
        self.RemoveButton.setObjectName(u"RemoveButton")
        self.RemoveButton.setGeometry(QRect(230, 80, 181, 31))
        self.RemoveButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_Admin_Page = QLabel(self.centralwidget)
        self.label_Admin_Page.setObjectName(u"label_Admin_Page")
        self.label_Admin_Page.setGeometry(QRect(15, 20, 405, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_Admin_Page.setFont(font)
        self.LogOffButton = QPushButton(self.centralwidget)
        self.LogOffButton.setObjectName(u"LogOffButton")
        self.LogOffButton.setGeometry(QRect(280, 150, 75, 24))
        self.LogOffButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.ReturnButton = QPushButton(self.centralwidget)
        self.ReturnButton.setObjectName(u"ReturnButton")
        self.ReturnButton.setGeometry(QRect(50, 150, 75, 24))
        self.ReturnButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.comboBoxLanguage = QComboBox(self.centralwidget)
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.setObjectName(u"comboBoxLanguage")
        self.comboBoxLanguage.setGeometry(QRect(340, 20, 68, 22))
        self.comboBoxLanguage.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        AdminPage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AdminPage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 435, 22))
        AdminPage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AdminPage)
        self.statusbar.setObjectName(u"statusbar")
        AdminPage.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.AddButton, self.RemoveButton)
        QWidget.setTabOrder(self.RemoveButton, self.ReturnButton)
        QWidget.setTabOrder(self.ReturnButton, self.LogOffButton)

        self.retranslateUi(AdminPage)

        self.comboBoxLanguage.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(AdminPage)
    # setupUi

    def retranslateUi(self, AdminPage):
        AdminPage.setWindowTitle(QCoreApplication.translate("AdminPage", u"Admin Page", None))
        self.AddButton.setText(QCoreApplication.translate("AdminPage", u"Add New Physiotherapist", None))
        self.RemoveButton.setText(QCoreApplication.translate("AdminPage", u"Remove Existing Physiotherapist", None))
        self.label_Admin_Page.setText(QCoreApplication.translate("AdminPage", u"Admin Page", None))
        self.LogOffButton.setText(QCoreApplication.translate("AdminPage", u"Log Off", None))
        self.ReturnButton.setText(QCoreApplication.translate("AdminPage", u"Return", None))
        self.comboBoxLanguage.setItemText(0, QCoreApplication.translate("AdminPage", u"English", None))
        self.comboBoxLanguage.setItemText(1, QCoreApplication.translate("AdminPage", u"\u05e2\u05d1\u05e8\u05d9\u05ea", None))

        self.comboBoxLanguage.setCurrentText("")
    # retranslateUi

