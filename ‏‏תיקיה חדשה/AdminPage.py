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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(431, 225)
        self.centralwidget = QWidget(MainWindow)
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
        self.label_Admin_Page.setGeometry(QRect(125, 20, 181, 41))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 431, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.AddButton, self.RemoveButton)
        QWidget.setTabOrder(self.RemoveButton, self.ReturnButton)
        QWidget.setTabOrder(self.ReturnButton, self.LogOffButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.AddButton.setText(QCoreApplication.translate("MainWindow", u"Add New Physiotherapist", None))
        self.RemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove Existing Physiotherapist", None))
        self.label_Admin_Page.setText(QCoreApplication.translate("MainWindow", u"Admin Page", None))
        self.LogOffButton.setText(QCoreApplication.translate("MainWindow", u"Log Off", None))
        self.ReturnButton.setText(QCoreApplication.translate("MainWindow", u"Return", None))
    # retranslateUi

