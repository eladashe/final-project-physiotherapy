# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoveExistingPhysiotherapists.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 523)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_Register_New_Physiotherapist = QLabel(self.centralwidget)
        self.label_Register_New_Physiotherapist.setObjectName(u"label_Register_New_Physiotherapist")
        self.label_Register_New_Physiotherapist.setGeometry(QRect(20, 10, 491, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_Register_New_Physiotherapist.setFont(font)
        self.RemoveButton = QPushButton(self.centralwidget)
        self.RemoveButton.setObjectName(u"RemoveButton")
        self.RemoveButton.setGeometry(QRect(333, 400, 184, 31))
        self.RemoveButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.ReturnButton = QPushButton(self.centralwidget)
        self.ReturnButton.setObjectName(u"ReturnButton")
        self.ReturnButton.setGeometry(QRect(175, 455, 75, 24))
        self.ReturnButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.LogOffButton = QPushButton(self.centralwidget)
        self.LogOffButton.setObjectName(u"LogOffButton")
        self.LogOffButton.setGeometry(QRect(600, 455, 75, 24))
        self.LogOffButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.tableWidget_Physiotherapists = QTableWidget(self.centralwidget)
        if (self.tableWidget_Physiotherapists.columnCount() < 7):
            self.tableWidget_Physiotherapists.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_Physiotherapists.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_Physiotherapists.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_Physiotherapists.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_Physiotherapists.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_Physiotherapists.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_Physiotherapists.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_Physiotherapists.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_Physiotherapists.setObjectName(u"tableWidget_Physiotherapists")
        self.tableWidget_Physiotherapists.setGeometry(QRect(25, 65, 811, 321))
        self.tableWidget_Physiotherapists.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.OpenHandCursor))
        self.tableWidget_Physiotherapists.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comboBoxLanguage = QComboBox(self.centralwidget)
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.setObjectName(u"comboBoxLanguage")
        self.comboBoxLanguage.setGeometry(QRect(768, 20, 68, 22))
        self.comboBoxLanguage.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tableWidget_Physiotherapists, self.RemoveButton)
        QWidget.setTabOrder(self.RemoveButton, self.ReturnButton)
        QWidget.setTabOrder(self.ReturnButton, self.LogOffButton)

        self.retranslateUi(MainWindow)

        self.comboBoxLanguage.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Remove Existing Physiotherapist", None))
        self.label_Register_New_Physiotherapist.setText(QCoreApplication.translate("MainWindow", u"Remove Existing Physiotherapist", None))
        self.RemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove Existing Physiotherapist", None))
        self.ReturnButton.setText(QCoreApplication.translate("MainWindow", u"Return", None))
        self.LogOffButton.setText(QCoreApplication.translate("MainWindow", u"Log Off", None))
        ___qtablewidgetitem = self.tableWidget_Physiotherapists.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem1 = self.tableWidget_Physiotherapists.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem2 = self.tableWidget_Physiotherapists.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem3 = self.tableWidget_Physiotherapists.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem4 = self.tableWidget_Physiotherapists.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem5 = self.tableWidget_Physiotherapists.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem6 = self.tableWidget_Physiotherapists.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Is Admin", None));
        self.comboBoxLanguage.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBoxLanguage.setItemText(1, QCoreApplication.translate("MainWindow", u"\u05e2\u05d1\u05e8\u05d9\u05ea", None))

        self.comboBoxLanguage.setCurrentText("")
    # retranslateUi

