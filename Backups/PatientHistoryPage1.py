# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PatientHistoryPage.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 689)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget_History = QTableWidget(self.centralwidget)
        if (self.tableWidget_History.columnCount() < 6):
            self.tableWidget_History.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_History.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_History.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_History.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_History.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_History.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_History.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_History.setObjectName(u"tableWidget_History")
        self.tableWidget_History.setGeometry(QRect(16, 60, 761, 161))
        self.tableWidget_History.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.OpenHandCursor))
        self.tableWidget_History.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_Patient_History_Page = QLabel(self.centralwidget)
        self.label_Patient_History_Page.setObjectName(u"label_Patient_History_Page")
        self.label_Patient_History_Page.setGeometry(QRect(20, 0, 341, 51))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label_Patient_History_Page.setFont(font)
        self.ExportToCSVButton = QPushButton(self.centralwidget)
        self.ExportToCSVButton.setObjectName(u"ExportToCSVButton")
        self.ExportToCSVButton.setGeometry(QRect(274, 570, 100, 30))
        self.ExportToCSVButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.NewTestButton = QPushButton(self.centralwidget)
        self.NewTestButton.setObjectName(u"NewTestButton")
        self.NewTestButton.setGeometry(QRect(58, 570, 100, 30))
        self.NewTestButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.LogOffButton = QPushButton(self.centralwidget)
        self.LogOffButton.setObjectName(u"LogOffButton")
        self.LogOffButton.setGeometry(QRect(178, 620, 75, 24))
        self.dateEdit_To = QDateEdit(self.centralwidget)
        self.dateEdit_To.setObjectName(u"dateEdit_To")
        self.dateEdit_To.setGeometry(QRect(630, 580, 110, 22))
        self.dateEdit_To.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.dateEdit_To.setWrapping(False)
        self.dateEdit_To.setCalendarPopup(True)
        self.label_To_Date = QLabel(self.centralwidget)
        self.label_To_Date.setObjectName(u"label_To_Date")
        self.label_To_Date.setGeometry(QRect(630, 560, 61, 16))
        self.dateEdit_From = QDateEdit(self.centralwidget)
        self.dateEdit_From.setObjectName(u"dateEdit_From")
        self.dateEdit_From.setGeometry(QRect(460, 580, 110, 22))
        self.dateEdit_From.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.dateEdit_From.setWrapping(False)
        self.dateEdit_From.setCalendarPopup(True)
        self.label_From_Date = QLabel(self.centralwidget)
        self.label_From_Date.setObjectName(u"label_From_Date")
        self.label_From_Date.setGeometry(QRect(460, 560, 61, 16))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(16, 230, 761, 321))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 804, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tableWidget_History, self.NewTestButton)
        QWidget.setTabOrder(self.NewTestButton, self.ExportToCSVButton)
        QWidget.setTabOrder(self.ExportToCSVButton, self.LogOffButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Patient History Page", None))
        ___qtablewidgetitem = self.tableWidget_History.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.tableWidget_History.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fall Risk", None));
        ___qtablewidgetitem2 = self.tableWidget_History.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Test Time", None));
        ___qtablewidgetitem3 = self.tableWidget_History.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Number Of Steps", None));
        ___qtablewidgetitem4 = self.tableWidget_History.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Incorrect Steps", None));
        ___qtablewidgetitem5 = self.tableWidget_History.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Physiotherapist Who Performed", None));
        self.label_Patient_History_Page.setText(QCoreApplication.translate("MainWindow", u"Patient History Page", None))
        self.ExportToCSVButton.setText(QCoreApplication.translate("MainWindow", u"Export to CSV", None))
        self.NewTestButton.setText(QCoreApplication.translate("MainWindow", u"New Test", None))
        self.LogOffButton.setText(QCoreApplication.translate("MainWindow", u"Log Off", None))
        self.label_To_Date.setText(QCoreApplication.translate("MainWindow", u"To Date:", None))
        self.label_From_Date.setText(QCoreApplication.translate("MainWindow", u"From Date:", None))
    # retranslateUi

