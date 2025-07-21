# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PreparationPage.ui'
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
        MainWindow.resize(661, 349)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_Instructions = QLabel(self.centralwidget)
        self.label_Instructions.setObjectName(u"label_Instructions")
        self.label_Instructions.setGeometry(QRect(20, 60, 621, 191))
        font = QFont()
        font.setPointSize(9)
        self.label_Instructions.setFont(font)
        self.label_Title = QLabel(self.centralwidget)
        self.label_Title.setObjectName(u"label_Title")
        self.label_Title.setGeometry(QRect(20, 10, 431, 41))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.label_Title.setFont(font1)
        self.StartTestButton = QPushButton(self.centralwidget)
        self.StartTestButton.setObjectName(u"StartTestButton")
        self.StartTestButton.setGeometry(QRect(293, 270, 75, 31))
        self.StartTestButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 661, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Preparation Page", None))
        self.label_Instructions.setText(QCoreApplication.translate("MainWindow", u"Please prepare the patient for the test according to the following instructions:\n"
"\n"
"\u2022 Ensure the patient is standing upright behind the starting line with both feet fully behind it.\n"
"\u2022 Verify that the patient is wearing appropriate and comfortable footwear for walking.\n"
"\u2022 The test will begin once a sound is heard, and the patient should start walking at a natural pace.\n"
"\u2022 Emphasize that the patient should not rush or stop \u2014 they should maintain a steady and consistent walking speed.\n"
"\u2022 If necessary, demonstrate how the test should be performed or answer any questions before beginning.\n"
"\n"
"When everything is ready, click \"Start Test\" to proceed.", None))
        self.label_Title.setText(QCoreApplication.translate("MainWindow", u"Instructions before starting the test:", None))
        self.StartTestButton.setText(QCoreApplication.translate("MainWindow", u"Start Test", None))
    # retranslateUi

