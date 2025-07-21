# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ResultsAnalysisPage.ui'
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
        MainWindow.resize(432, 441)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget_Results = QTableWidget(self.centralwidget)
        if (self.tableWidget_Results.columnCount() < 1):
            self.tableWidget_Results.setColumnCount(1)
        font = QFont()
        font.setPointSize(15)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget_Results.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget_Results.rowCount() < 4):
            self.tableWidget_Results.setRowCount(4)
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setStrikeOut(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget_Results.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget_Results.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget_Results.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tableWidget_Results.setVerticalHeaderItem(3, __qtablewidgetitem4)
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.tableWidget_Results.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.tableWidget_Results.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.tableWidget_Results.setItem(2, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.tableWidget_Results.setItem(3, 0, __qtablewidgetitem8)
        self.tableWidget_Results.setObjectName(u"tableWidget_Results")
        self.tableWidget_Results.setGeometry(QRect(16, 80, 400, 221))
        self.tableWidget_Results.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.OpenHandCursor))
        self.tableWidget_Results.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_Result_Page = QLabel(self.centralwidget)
        self.label_Result_Page.setObjectName(u"label_Result_Page")
        self.label_Result_Page.setGeometry(QRect(20, 10, 341, 51))
        font3 = QFont()
        font3.setPointSize(26)
        font3.setBold(True)
        self.label_Result_Page.setFont(font3)
        self.HistoryResultsButton = QPushButton(self.centralwidget)
        self.HistoryResultsButton.setObjectName(u"HistoryResultsButton")
        self.HistoryResultsButton.setGeometry(QRect(274, 320, 100, 30))
        self.HistoryResultsButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.NewTestButton = QPushButton(self.centralwidget)
        self.NewTestButton.setObjectName(u"NewTestButton")
        self.NewTestButton.setGeometry(QRect(58, 320, 100, 30))
        self.NewTestButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.LogOffButton = QPushButton(self.centralwidget)
        self.LogOffButton.setObjectName(u"LogOffButton")
        self.LogOffButton.setGeometry(QRect(178, 370, 75, 24))
        self.LogOffButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.comboBoxLanguage = QComboBox(self.centralwidget)
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.setObjectName(u"comboBoxLanguage")
        self.comboBoxLanguage.setGeometry(QRect(348, 20, 68, 22))
        self.comboBoxLanguage.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 432, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tableWidget_Results, self.NewTestButton)
        QWidget.setTabOrder(self.NewTestButton, self.HistoryResultsButton)
        QWidget.setTabOrder(self.HistoryResultsButton, self.LogOffButton)

        self.retranslateUi(MainWindow)

        self.comboBoxLanguage.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Result Analysis Page", None))
        ___qtablewidgetitem = self.tableWidget_Results.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem1 = self.tableWidget_Results.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fall Risk", None));
        ___qtablewidgetitem2 = self.tableWidget_Results.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Test Time", None));
        ___qtablewidgetitem3 = self.tableWidget_Results.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Number of Steps", None));
        ___qtablewidgetitem4 = self.tableWidget_Results.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Error Steps", None));

        __sortingEnabled = self.tableWidget_Results.isSortingEnabled()
        self.tableWidget_Results.setSortingEnabled(False)
        self.tableWidget_Results.setSortingEnabled(__sortingEnabled)

        self.label_Result_Page.setText(QCoreApplication.translate("MainWindow", u"Result Analysis Page", None))
        self.HistoryResultsButton.setText(QCoreApplication.translate("MainWindow", u"History Results", None))
        self.NewTestButton.setText(QCoreApplication.translate("MainWindow", u"New Test", None))
        self.LogOffButton.setText(QCoreApplication.translate("MainWindow", u"Log Off", None))
        self.comboBoxLanguage.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBoxLanguage.setItemText(1, QCoreApplication.translate("MainWindow", u"\u05e2\u05d1\u05e8\u05d9\u05ea", None))

        self.comboBoxLanguage.setCurrentText("")
    # retranslateUi

