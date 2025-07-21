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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
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
        if (self.tableWidget_Results.columnCount() < 2):
            self.tableWidget_Results.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_Results.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget_Results.rowCount() < 3):
            self.tableWidget_Results.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_Results.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_Results.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_Results.setVerticalHeaderItem(2, __qtablewidgetitem4)
        self.tableWidget_Results.setObjectName(u"tableWidget_Results")
        self.tableWidget_Results.setGeometry(QRect(16, 80, 400, 221))
        self.tableWidget_Results.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.OpenHandCursor))
        self.tableWidget_Results.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_Result_Page = QLabel(self.centralwidget)
        self.label_Result_Page.setObjectName(u"label_Result_Page")
        self.label_Result_Page.setGeometry(QRect(20, 10, 341, 51))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label_Result_Page.setFont(font)
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
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 432, 441))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 432, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget_Results.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Parameter", None));
        ___qtablewidgetitem1 = self.tableWidget_Results.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        ___qtablewidgetitem2 = self.tableWidget_Results.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fall Risk", None));
        ___qtablewidgetitem3 = self.tableWidget_Results.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Number of Steps", None));
        ___qtablewidgetitem4 = self.tableWidget_Results.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Error Steps", None));
        self.label_Result_Page.setText(QCoreApplication.translate("MainWindow", u"Result Analysis Page", None))
        self.HistoryResultsButton.setText(QCoreApplication.translate("MainWindow", u"History Results", None))
        self.NewTestButton.setText(QCoreApplication.translate("MainWindow", u"New Test", None))
        self.LogOffButton.setText(QCoreApplication.translate("MainWindow", u"Log Off", None))
    # retranslateUi

