# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CheckSystemPage.ui'
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
        MainWindow.resize(428, 217)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ExplorerButton = QPushButton(self.centralwidget)
        self.ExplorerButton.setObjectName(u"ExplorerButton")
        self.ExplorerButton.setGeometry(QRect(71, 80, 72, 31))
        self.ExplorerButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.DiagnosticButton = QPushButton(self.centralwidget)
        self.DiagnosticButton.setObjectName(u"DiagnosticButton")
        self.DiagnosticButton.setGeometry(QRect(285, 80, 72, 31))
        self.DiagnosticButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_Check_System_Page = QLabel(self.centralwidget)
        self.label_Check_System_Page.setObjectName(u"label_Check_System_Page")
        self.label_Check_System_Page.setGeometry(QRect(73, 20, 291, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_Check_System_Page.setFont(font)
        self.LogOffButton = QPushButton(self.centralwidget)
        self.LogOffButton.setObjectName(u"LogOffButton")
        self.LogOffButton.setGeometry(QRect(322, 150, 75, 24))
        self.LogOffButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.ReturnButton = QPushButton(self.centralwidget)
        self.ReturnButton.setObjectName(u"ReturnButton")
        self.ReturnButton.setGeometry(QRect(22, 150, 69, 24))
        self.ReturnButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 428, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.ExplorerButton, self.DiagnosticButton)
        QWidget.setTabOrder(self.DiagnosticButton, self.ReturnButton)
        QWidget.setTabOrder(self.ReturnButton, self.LogOffButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ExplorerButton.setText(QCoreApplication.translate("MainWindow", u"Explorer", None))
        self.DiagnosticButton.setText(QCoreApplication.translate("MainWindow", u"Diagnostic", None))
        self.label_Check_System_Page.setText(QCoreApplication.translate("MainWindow", u"Check System Page", None))
        self.LogOffButton.setText(QCoreApplication.translate("MainWindow", u"Log Off", None))
        self.ReturnButton.setText(QCoreApplication.translate("MainWindow", u"Return", None))
    # retranslateUi

