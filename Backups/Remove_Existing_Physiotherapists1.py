from PySide6.QtWidgets import (
    QApplication, QLabel, QTableWidget, QTableWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QStatusBar, QWidget, QMessageBox, QAbstractItemView
)
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, controller=None):
        self.controller = controller
        self.current_user_email = getattr(controller, "current_user", None)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 450)
        self.centralwidget = QWidget(MainWindow)

        font = QFont()
        font.setPointSize(24)
        font.setBold(True)

        self.label_Register_New_Physiotherapist = QLabel("Remove Existing Physiotherapist", self.centralwidget)
        self.label_Register_New_Physiotherapist.setFont(font)
        self.label_Register_New_Physiotherapist.setGeometry(QRect(20, 10, 661, 41))


        self.tableWidget_Existing_Physiotherapists = QTableWidget(self.centralwidget)
        self.tableWidget_Existing_Physiotherapists.setGeometry(QRect(20, 60, 660, 260))
        self.tableWidget_Existing_Physiotherapists.setColumnCount(5)
        self.tableWidget_Existing_Physiotherapists.setHorizontalHeaderLabels(
            ["Email", "First Name", "Last Name", "Gender", "Age", "Is Admin"])
        self.tableWidget_Existing_Physiotherapists.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_Existing_Physiotherapists.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_Existing_Physiotherapists.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.pushButton_Remove_Existing_Physiotherapists = QPushButton("Remove Existing Physiotherapist", self.centralwidget)
        self.pushButton_Remove_Existing_Physiotherapists.setGeometry(QRect(180, 260, 181, 31))
        self.pushButton_Remove_Existing_Physiotherapists.clicked.connect(self.remove_selected_physio)

        self.pushButton_Return = QPushButton("Return", self.centralwidget)
        self.pushButton_Return.setGeometry(QRect(150, 390, 75, 24))
        self.pushButton_Return.clicked.connect(self.return_to_admin)

        self.pushButton_Log_Off = QPushButton("Log Off", self.centralwidget)
        self.pushButton_Log_Off.setGeometry(QRect(450, 390, 75, 24))
        self.pushButton_Log_Off.clicked.connect(self.log_off)

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setMenuBar(QMenuBar(MainWindow))
        MainWindow.setStatusBar(QStatusBar(MainWindow))




