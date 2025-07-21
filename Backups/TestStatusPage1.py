# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestStatusPage.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, controller=None):
        self.controller = controller
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(168, 163)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_Status = QLabel(self.centralwidget)
        self.label_Status.setObjectName(u"label_Status")
        self.label_Status.setGeometry(QRect(30, 20, 49, 16))
        self.pushButton_Ready = QPushButton(self.centralwidget)
        self.pushButton_Ready.setObjectName(u"pushButton_Ready")
        self.pushButton_Ready.setGeometry(QRect(40, 90, 75, 24))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 50, 118, 23))
        self.progressBar.setValue(24)
        self.label_Current_Status = QLabel(self.centralwidget)
        self.label_Current_Status.setObjectName(u"label_Current_Status")
        self.label_Current_Status.setGeometry(QRect(78, 20, 71, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 168, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Status.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.pushButton_Ready.setText(QCoreApplication.translate("MainWindow", u"Ready", None))
        self.label_Current_Status.setText("")
    # retranslateUi

