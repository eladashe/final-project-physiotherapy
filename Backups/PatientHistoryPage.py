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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1522, 691)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_Patient_History_Page = QLabel(self.centralwidget)
        self.label_Patient_History_Page.setObjectName(u"label_Patient_History_Page")
        self.label_Patient_History_Page.setGeometry(QRect(10, 10, 341, 51))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label_Patient_History_Page.setFont(font)
        self.tableWidget_History = QTableWidget(self.centralwidget)
        if (self.tableWidget_History.columnCount() < 7):
            self.tableWidget_History.setColumnCount(7)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_History.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_History.setObjectName(u"tableWidget_History")
        self.tableWidget_History.setGeometry(QRect(10, 70, 721, 484))
        self.tableWidget_History.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.OpenHandCursor))
        self.tableWidget_History.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ExportToCSVButton = QPushButton(self.centralwidget)
        self.ExportToCSVButton.setObjectName(u"ExportToCSVButton")
        self.ExportToCSVButton.setGeometry(QRect(254, 570, 100, 30))
        self.ExportToCSVButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.dateEdit_From = QDateEdit(self.centralwidget)
        self.dateEdit_From.setObjectName(u"dateEdit_From")
        self.dateEdit_From.setGeometry(QRect(420, 580, 110, 22))
        self.dateEdit_From.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.dateEdit_From.setWrapping(False)
        self.dateEdit_From.setCalendarPopup(True)
        self.NewTestButton = QPushButton(self.centralwidget)
        self.NewTestButton.setObjectName(u"NewTestButton")
        self.NewTestButton.setGeometry(QRect(38, 570, 100, 30))
        self.NewTestButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.dateEdit_To = QDateEdit(self.centralwidget)
        self.dateEdit_To.setObjectName(u"dateEdit_To")
        self.dateEdit_To.setGeometry(QRect(590, 580, 110, 22))
        self.dateEdit_To.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.dateEdit_To.setWrapping(False)
        self.dateEdit_To.setCalendarPopup(True)
        self.label_To_Date = QLabel(self.centralwidget)
        self.label_To_Date.setObjectName(u"label_To_Date")
        self.label_To_Date.setGeometry(QRect(590, 560, 61, 16))
        self.LogOffButton = QPushButton(self.centralwidget)
        self.LogOffButton.setObjectName(u"LogOffButton")
        self.LogOffButton.setGeometry(QRect(158, 620, 75, 24))
        self.LogOffButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_From_Date = QLabel(self.centralwidget)
        self.label_From_Date.setObjectName(u"label_From_Date")
        self.label_From_Date.setGeometry(QRect(420, 560, 61, 16))
        self.widget_Gauge = QWidget(self.centralwidget)
        self.widget_Gauge.setObjectName(u"widget_Gauge")
        self.widget_Gauge.setGeometry(QRect(740, 70, 386, 242))
        self.layoutWidget = QWidget(self.widget_Gauge)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 5, 381, 231))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_Gauge_Title = QLabel(self.layoutWidget)
        self.label_Gauge_Title.setObjectName(u"label_Gauge_Title")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Gauge_Title.sizePolicy().hasHeightForWidth())
        self.label_Gauge_Title.setSizePolicy(sizePolicy)
        self.label_Gauge_Title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_Gauge_Title)

        self.widget_Gauge_Canvas = QWidget(self.layoutWidget)
        self.widget_Gauge_Canvas.setObjectName(u"widget_Gauge_Canvas")

        self.verticalLayout.addWidget(self.widget_Gauge_Canvas)

        self.label_Gauge_Percentage = QLabel(self.layoutWidget)
        self.label_Gauge_Percentage.setObjectName(u"label_Gauge_Percentage")
        sizePolicy.setHeightForWidth(self.label_Gauge_Percentage.sizePolicy().hasHeightForWidth())
        self.label_Gauge_Percentage.setSizePolicy(sizePolicy)
        self.label_Gauge_Percentage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_Gauge_Percentage)

        self.widget_FallRisk = QWidget(self.centralwidget)
        self.widget_FallRisk.setObjectName(u"widget_FallRisk")
        self.widget_FallRisk.setGeometry(QRect(1127, 70, 386, 242))
        self.widget_StepCount = QWidget(self.centralwidget)
        self.widget_StepCount.setObjectName(u"widget_StepCount")
        self.widget_StepCount.setGeometry(QRect(740, 313, 386, 242))
        self.widget_ErrorSteps = QWidget(self.centralwidget)
        self.widget_ErrorSteps.setObjectName(u"widget_ErrorSteps")
        self.widget_ErrorSteps.setGeometry(QRect(1127, 313, 386, 242))
        self.comboBoxLanguage = QComboBox(self.centralwidget)
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.addItem("")
        self.comboBoxLanguage.setObjectName(u"comboBoxLanguage")
        self.comboBoxLanguage.setGeometry(QRect(1430, 20, 68, 22))
        self.comboBoxLanguage.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1522, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBoxLanguage.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Patient History Page", None))
        self.label_Patient_History_Page.setText(QCoreApplication.translate("MainWindow", u"Patient History Page", None))
        ___qtablewidgetitem = self.tableWidget_History.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Test Date", None));
        ___qtablewidgetitem1 = self.tableWidget_History.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fall Risk", None));
        ___qtablewidgetitem2 = self.tableWidget_History.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Total Steps", None));
        ___qtablewidgetitem3 = self.tableWidget_History.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Error Steps", None));
        ___qtablewidgetitem4 = self.tableWidget_History.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Start Time", None));
        ___qtablewidgetitem5 = self.tableWidget_History.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"End Time", None));
        ___qtablewidgetitem6 = self.tableWidget_History.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Test Time (sec)", None));
        self.ExportToCSVButton.setText(QCoreApplication.translate("MainWindow", u"Export to CSV", None))
        self.NewTestButton.setText(QCoreApplication.translate("MainWindow", u"New Test", None))
        self.label_To_Date.setText(QCoreApplication.translate("MainWindow", u"To Date:", None))
        self.LogOffButton.setText(QCoreApplication.translate("MainWindow", u"Log Off", None))
        self.label_From_Date.setText(QCoreApplication.translate("MainWindow", u"From Date:", None))
        self.label_Gauge_Title.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_Gauge_Percentage.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.comboBoxLanguage.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBoxLanguage.setItemText(1, QCoreApplication.translate("MainWindow", u"\u05e2\u05d1\u05e8\u05d9\u05ea", None))

        self.comboBoxLanguage.setCurrentText("")
    # retranslateUi

