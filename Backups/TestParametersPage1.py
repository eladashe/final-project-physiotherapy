# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TestParametersPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)
from datetime import datetime
import pypyodbc as odbc
import csv
import os

# Database login details
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'ELAD-COMPUTER\\SQLEXPRESS'
DATABASE_NAME = 'DB_Final_Project'

connection_string = (
    f"DRIVER={{{DRIVER_NAME}}};"
    f"SERVER={SERVER_NAME};"
    f"DATABASE={DATABASE_NAME};"
    f"Trusted_Connection=yes;"
)

# Queries the PATIENTS table by ID and returns gender and date of birth.
def get_patient_info(patient_id):
    try:
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("SELECT Gender, Date_Of_Birth FROM PATIENTS WHERE Patient_ID = ?", (patient_id,))
        result = cursor.fetchone()
        conn.close()
        return {"gender": result[0], "dob": result[1]} if result else None

    except Exception as e:
        print("❌ Error fetching patient info:", e)
        return None


# Returns a dictionary with parameter names and values
def get_recent_parameters(patient_id, days):
    try:
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT TP.Parameter_Name, PP.Param_Value
            FROM PATIENTPARAMETER AS PP JOIN TOTALPARAMETERS AS TP ON PP.Param_ID = TP.Parameter_ID
            WHERE PP.Patient_ID = ?
              AND PP.Updated_At >= DATEADD(DAY, -?, CAST(GETDATE() AS DATE))
            """,
            (patient_id, days)
        )
        rows = cursor.fetchall()
        conn.close()
        return {name: value for name, value in rows} if rows else None
    except Exception as e:
        print("❌ Error fetching parameters:", e)
        return None

# Receives a username and returns his first name.
def get_first_name_from_username(username: str):
    try:
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()

        if '@' in username:
            # Search by full email
            query = "SELECT First_Name FROM PHYSIOTHERAPISTS WHERE Email = ?"
            cursor.execute(query, (username,))
        else:
            # Search by email prefix only (before the @)
            query = """
                SELECT First_Name 
                FROM PHYSIOTHERAPISTS 
                WHERE LEFT(Email, CHARINDEX('@', Email) - 1) = ?
            """
            cursor.execute(query, (username.lower(),))

        result = cursor.fetchone()
        conn.close()

        return result[0] if result else None # Returns the first name

    except Exception as e:
        print("❌ Error fetching first name:", e)
        return None


def save_test_result_to_csv(patient_id, test_time_sec, risk_level, test_notes=None):
    # Location to save the file
    folder = 'C:\\Users\\elada\\Desktop\\לימודים\\שנה ד\\סמסטר ב\\פרויקט מסכם א\\בדיקות'
    if os.path.exists(folder):
        print("התיקייה קיימת!")
    else:
        print("התיקייה לא קיימת.")
    os.makedirs(folder, exist_ok=True)

    # File name by patient ID
    filename = f"{folder}/patient_{patient_id}_results.csv"

    # Does the file already exist
    file_exists = os.path.isfile(filename)

    # Writing the data
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Title only if the file is new
        if not file_exists:
            writer.writerow(["Date", "Time", "Patient ID", "Test Duration (s)", "Fall Risk", "Notes"])

        now = datetime.now()
        writer.writerow([
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S"),
            patient_id,
            f"{test_time_sec:.2f}",
            risk_level,
            test_notes or ""
        ])



class Ui_MainWindow(object):
    def setupUi(self, MainWindow, controller=None, is_admin=None):
        self.controller = controller
        self.is_admin = is_admin
        self.first_name = get_first_name_from_username(self.controller)
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(539, 561)
        MainWindow.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_Start_Test = QPushButton(self.centralwidget)
        self.pushButton_Start_Test.setObjectName(u"pushButton_Start_Test")
        self.pushButton_Start_Test.setGeometry(QRect(219, 443, 101, 31))
        self.pushButton_Start_Test.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.comboBox_Gender = QComboBox(self.centralwidget)
        self.comboBox_Gender.addItem("")
        self.comboBox_Gender.addItem("")
        self.comboBox_Gender.addItem("")
        self.comboBox_Gender.setObjectName(u"comboBox_Gender")
        self.comboBox_Gender.setGeometry(QRect(190, 110, 160, 21))
        self.comboBox_Gender.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_Patient_ID = QLabel(self.centralwidget)
        self.label_Patient_ID.setObjectName(u"label_Patient_ID")
        self.label_Patient_ID.setGeometry(QRect(100, 70, 61, 21))
        self.label_Gender = QLabel(self.centralwidget)
        self.label_Gender.setObjectName(u"label_Gender")
        self.label_Gender.setGeometry(QRect(100, 110, 49, 21))
        self.label_Test_Parameters_Page = QLabel(self.centralwidget)
        self.label_Test_Parameters_Page.setObjectName(u"label_Test_Parameters_Page")
        self.label_Test_Parameters_Page.setGeometry(QRect(18, 10, 331, 41))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_Test_Parameters_Page.setFont(font)
        self.label_Date_Of_Birth = QLabel(self.centralwidget)
        self.label_Date_Of_Birth.setObjectName(u"label_Date_Of_Birth")
        self.label_Date_Of_Birth.setGeometry(QRect(100, 150, 71, 21))
        self.label_Pelvic_Width = QLabel(self.centralwidget)
        self.label_Pelvic_Width.setObjectName(u"label_Pelvic_Width")
        self.label_Pelvic_Width.setGeometry(QRect(100, 230, 71, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 270, 211, 21))
        self.lineEdit_Patient_ID = QLineEdit(self.centralwidget)
        self.lineEdit_Patient_ID.setObjectName(u"lineEdit_Patient_ID")
        self.lineEdit_Patient_ID.setGeometry(QRect(190, 70, 160, 21))
        self.comboBox_Has_Fallen = QComboBox(self.centralwidget)
        self.comboBox_Has_Fallen.addItem("")
        self.comboBox_Has_Fallen.addItem("")
        self.comboBox_Has_Fallen.setObjectName(u"comboBox_Has_Fallen")
        self.comboBox_Has_Fallen.setGeometry(QRect(190, 300, 160, 21))
        self.comboBox_Has_Fallen.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.lineEdit_Pelvic_Width = QLineEdit(self.centralwidget)
        self.lineEdit_Pelvic_Width.setObjectName(u"lineEdit_Pelvic_Width")
        self.lineEdit_Pelvic_Width.setGeometry(QRect(190, 230, 160, 21))
        self.dateEdit_Date_Of_Birth = QDateEdit(self.centralwidget)
        self.dateEdit_Date_Of_Birth.setObjectName(u"dateEdit_Date_Of_Birth")
        self.dateEdit_Date_Of_Birth.setEnabled(True)
        self.dateEdit_Date_Of_Birth.setGeometry(QRect(190, 150, 160, 21))
        self.dateEdit_Date_Of_Birth.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.dateEdit_Date_Of_Birth.setMouseTracking(False)
        self.dateEdit_Date_Of_Birth.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.dateEdit_Date_Of_Birth.setCalendarPopup(True)
        self.pushButton_Log_Off = QPushButton(self.centralwidget)
        self.pushButton_Log_Off.setObjectName(u"pushButton_Log_Off")
        self.pushButton_Log_Off.setGeometry(QRect(440, 490, 75, 24))
        self.lineEdit_Shoe_Width = QLineEdit(self.centralwidget)
        self.lineEdit_Shoe_Width.setObjectName(u"lineEdit_Shoe_Width")
        self.lineEdit_Shoe_Width.setGeometry(QRect(190, 190, 160, 21))
        self.label_Shoe_Width = QLabel(self.centralwidget)
        self.label_Shoe_Width.setObjectName(u"label_Shoe_Width")
        self.label_Shoe_Width.setGeometry(QRect(100, 190, 71, 21))
        self.label_Notes = QLabel(self.centralwidget)
        self.label_Notes.setObjectName(u"label_Notes")
        self.label_Notes.setGeometry(QRect(100, 340, 71, 21))
        self.textEdit_Notes = QTextEdit(self.centralwidget)
        self.textEdit_Notes.setObjectName(u"textEdit_Notes")
        self.textEdit_Notes.setGeometry(QRect(190, 340, 160, 71))
        self.pushButton_Admin_Page = QPushButton(self.centralwidget)
        self.pushButton_Admin_Page.setObjectName(u"pushButton_Admin_Page")
        self.pushButton_Admin_Page.setGeometry(QRect(20, 490, 75, 24))
        self.pushButton_Log_Off_2 = QPushButton(self.centralwidget)
        self.pushButton_Log_Off_2.setObjectName(u"pushButton_Log_Off_2")
        self.pushButton_Log_Off_2.setGeometry(QRect(229, 490, 81, 24))
        self.label_welcome_user = QLabel(self.centralwidget)
        self.label_welcome_user.setObjectName(u"label_welcome_user")
        self.label_welcome_user.setGeometry(QRect(390, 20, 121, 16))
        self.pushButton_Patient_History = QPushButton(self.centralwidget)
        self.pushButton_Patient_History.setObjectName(u"pushButton_Log_Off_3")
        self.pushButton_Patient_History.setGeometry(QRect(390, 68, 95, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 539, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox_Gender.setCurrentIndex(-1)
        self.comboBox_Has_Fallen.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Start_Test.setText(QCoreApplication.translate("MainWindow", u"Start Test", None))
        self.comboBox_Gender.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.comboBox_Gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))
        self.comboBox_Gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Other", None))

        self.label_Patient_ID.setText(QCoreApplication.translate("MainWindow", u"Patient ID:", None))
        self.label_Gender.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.label_Test_Parameters_Page.setText(QCoreApplication.translate("MainWindow", u"Test Parameters Page", None))
        self.label_Date_Of_Birth.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth:", None))
        self.label_Pelvic_Width.setText(QCoreApplication.translate("MainWindow", u"Pelvic Width:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Has the patient fallen in the last year?", None))
        self.comboBox_Has_Fallen.setItemText(0, QCoreApplication.translate("MainWindow", u"Yes", None))
        self.comboBox_Has_Fallen.setItemText(1, QCoreApplication.translate("MainWindow", u"No", None))

        self.pushButton_Log_Off.setText(QCoreApplication.translate("MainWindow", u"Log Off", None))
        self.label_Shoe_Width.setText(QCoreApplication.translate("MainWindow", u"Shoe Width:", None))
        self.label_Notes.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.pushButton_Admin_Page.setText(QCoreApplication.translate("MainWindow", u"Admin Page", None))
        self.pushButton_Log_Off_2.setText(QCoreApplication.translate("MainWindow", u"Check System", None))
        self.label_welcome_user.setText(QCoreApplication.translate("MainWindow", u"Welcome, User's Name", None))
        self.pushButton_Patient_History.setText(QCoreApplication.translate("MainWindow", u"Patient's History", None))
    # retranslateUi

