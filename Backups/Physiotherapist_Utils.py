#region Imports
from PySide6.QtWidgets import (QLabel, QLineEdit, QPushButton, QWidget, QMainWindow, QTableWidget, QToolButton, QTableWidgetItem,
                               QMessageBox, QComboBox, QDateEdit, QCheckBox, QApplication)
from PySide6.QtCore import QCoreApplication, QRect, QMetaObject, Qt, QTimer, QDate, QObject, QEvent
from PySide6.QtGui import QFont, QCursor, QIcon, QAction, QColor
from LoginPage import Ui_MainWindow as Ui_LoginPage
from TestParametersPage import Ui_MainWindow as Ui_TestParameters
from PreparationPage import Ui_MainWindow as Ui_PreparationPage
from ResultsAnalysisPage import Ui_MainWindow as Ui_ResultsAnalysisPage
from AdminPage import Ui_MainWindow as Ui_AdminPage
from RegisterNewPhysiotherapist import Ui_MainWindow as Ui_RegisterNewPhysiotherapist
from RemoveExistingPhysiotherapists import Ui_MainWindow as Ui_RemoveExistingPhysiotherapists
from PatientHistoryPage import Ui_MainWindow as Ui_PatientHistoryPage
from FirstUsePage import Ui_MainWindow as Ui_FirstUsePage
from CheckSystemPage import Ui_MainWindow as Ui_CheckSystemPage
from ResetPasswordPage import Ui_MainWindow as Ui_ResetPasswordPage
from GraphManager import GraphManager
# from DashboardManager import DashboardManager
import DatabaseUtils
from Translator import Translator
from language_settings import load_saved_language, save_language
from NPWT_Test import predict_risk_probability
from datetime import datetime
import re, csv, os, bcrypt, pandas as pd #, pyodbc, pypyodbc as odbc
###
import random
from time import time
###
#endregion


class Physiotherapist_Utils(QObject):
    def __init__(self, ui):
        super().__init__()
        # self.csv_folder = 'C:\\Users\\elada\\PycharmProjects\\‏‏Final_Project\\Reports'
        self.csv_folder = r"C:\Users\elada\PycharmProjects\‏‏Final_Project\Reports"
        self.explorer = r"C:\Program Files\RStudio\rstudio.exe"
        self.diagnostic = r"C:\Program Files\RStudio\rstudio.exe"
        # region Initialize GUI fields
        self.login_ui = None
        self.first_use_ui = None
        self.register_ui = None
        self.admin_ui = None
        self.remove_ui = None
        self.test_parameters_ui = None
        self.check_system_ui = None
        self.test_status_ui = None
        self.result_ui = None
        # endregion
        self.ui = ui
        self.parent_window = self.ui
        self.current_user = {
            "email": None,
            "first_name": None,
            "is_admin": False,
            "password_last_changed": None,
            "preferred_language": None
        }
        self.current_patient_id = None
        self.start_time = None
        self.current_notes = None
        self.note_to_save = None
        self.graph_manager = None
        # self.dashboard_manager = None
        # self.current_language = 'en'
        self.current_language = load_saved_language()
        self.translator = Translator(language_code=self.current_language)
        # self.current_language = None
        # self.translator = Translator(language_code='en')
        # self.translator = Translator(language_code='he')
        self.error_color = "#C00000"
        self.param_days_back = 2
        self.initialization()

    def initialization(self):
        self.autofill_timer = QTimer()
        self.autofill_timer.setSingleShot(True)
        self.autofill_timer.timeout.connect(self.autofill_patient_data)

        self.inactivity_timer = QTimer()
        self.session_time = 20
        self.inactivity_timer.setInterval(self.session_time * 60 * 1000)
        self.inactivity_timer.setSingleShot(True)
        self.inactivity_timer.timeout.connect(self.show_inactivity_warning)
        self.logout_timer = QTimer()
        self.logout_timer.setInterval(60 * 1000)
        self.logout_timer.setSingleShot(True)
        self.logout_timer.timeout.connect(self.handle_inactivity_logout)

        QApplication.instance().installEventFilter(self)
        self.inactivity_timer.start()

    # region Setup Pages
    # ===== Login
    def setup_login_ui(self):
        self.login_ui = Ui_LoginPage()
        self.login_ui.setupUi(self.parent_window)
        self.translate_login_ui()

        self.apply_layout_direction_recursive(self.login_ui.centralwidget)
        self.login_ui.LoginButton.clicked.connect(lambda: self.load_test_parameters_page(True))
        self.login_ui.FirstUseButton.clicked.connect(self.load_first_use_page)
        self.login_ui.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_ui.error_Username_or_Password.setStyleSheet(f"color: {self.error_color}")
        self.login_ui.error_Username_or_Password.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.login_ui.error_Username_or_Password.hide()
        self.login_ui.label_Forgot_Password.hide()
        self.setup_password_visibility(self.login_ui)

        for line_edit in self.login_ui.centralwidget.findChildren(QLineEdit):
            line_edit.returnPressed.connect(lambda: self.load_test_parameters_page(True))
        for button in self.login_ui.centralwidget.findChildren(QPushButton):
            button.setDefault(True)
    # ===== Reset Password
    def setup_reset_password_ui(self):
        self.reset_ui = Ui_ResetPasswordPage()
        self.reset_ui.setupUi(self.parent_window)
        self.translate_reset_password_ui()

        self.reset_ui.comboBoxLanguage.currentIndexChanged.connect(
            lambda: self.handle_language_change(self.reset_ui.comboBoxLanguage, "reset")
        )
        self.set_language_combobox(self.reset_ui.comboBoxLanguage)

        self.reset_ui.ResetPasswordButton.clicked.connect(self.handle_reset_password)
        self.reset_ui.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)

        for error_label in [self.reset_ui.error_Email, self.reset_ui.error_Password, self.reset_ui.error_Password_Confirmation]:
            error_label.setStyleSheet(f"color: {self.error_color}")
            error_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            error_label.hide()
        self.setup_password_visibility(self.reset_ui)

        for line_edit in self.reset_ui.centralwidget.findChildren(QLineEdit):
            line_edit.returnPressed.connect(self.handle_reset_password)
    # ===== First Use
    def setup_first_use_ui(self):
        self.first_use_ui = Ui_FirstUsePage()
        self.first_use_ui.setupUi(self.parent_window)
        self.translate_first_use_ui()

        self.first_use_ui.comboBoxLanguage.currentIndexChanged.connect(
            lambda: self.handle_language_change(self.first_use_ui.comboBoxLanguage, "first_use")
        )
        self.set_language_combobox(self.first_use_ui.comboBoxLanguage)

        self.first_use_ui.AddButton.clicked.connect(lambda: self.handle_registration(self.first_use_ui))
        self.first_use_ui.ResetButton.clicked.connect(self.reset_database)
        self.first_use_ui.lineEdit_Email.editingFinished.connect(lambda: self.handle_email_finished(self.first_use_ui))

        for error_label in [self.first_use_ui.error_Email, self.first_use_ui.error_Username, self.first_use_ui.error_Gender,
                            self.first_use_ui.error_First_Name, self.first_use_ui.error_Last_Name, self.first_use_ui.error_Password,
                            self.first_use_ui.error_Password_Confirmation]:
            error_label.setStyleSheet(f"color: {self.error_color}")
            error_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            error_label.hide()
        # self.first_use_ui.error_Email.setStyleSheet(f"color: {self.error_color}")
        # self.first_use_ui.error_Email.hide()
        # self.first_use_ui.error_Username.setStyleSheet(f"color: {self.error_color}")
        # self.first_use_ui.error_Username.hide()
        # self.first_use_ui.error_Gender.setStyleSheet(f"color: {self.error_color}")
        # self.first_use_ui.error_Gender.hide()
        # self.first_use_ui.error_First_Name.setStyleSheet(f"color: {self.error_color}")
        # self.first_use_ui.error_First_Name.hide()
        # self.first_use_ui.error_Last_Name.setStyleSheet(f"color: {self.error_color}")
        # self.first_use_ui.error_Last_Name.hide()
        # self.first_use_ui.error_Password.setStyleSheet(f"color: {self.error_color}")
        # self.first_use_ui.error_Password.hide()
        # self.first_use_ui.error_Password_Confirmation.setStyleSheet(f"color: {self.error_color}")
        # self.first_use_ui.error_Password_Confirmation.hide()
        self.first_use_ui.dateEdit_Date_Of_Birth.setDate(QDate.currentDate())
        self.setup_password_visibility(self.first_use_ui)

        for line_edit in self.first_use_ui.centralwidget.findChildren(QLineEdit):
            line_edit.returnPressed.connect(lambda: self.handle_registration(self.first_use_ui))
        for button in self.first_use_ui.centralwidget.findChildren(QPushButton):
            button.setDefault(True)
    # ===== Admin
    def setup_admin_ui(self):
        self.admin_ui = Ui_AdminPage()
        self.admin_ui.setupUi(self.parent_window)
        self.translate_admin_ui()

        self.admin_ui.comboBoxLanguage.currentIndexChanged.connect(
            lambda: self.handle_language_change(self.admin_ui.comboBoxLanguage, "admin")
        )
        self.set_language_combobox(self.admin_ui.comboBoxLanguage)

        self.admin_ui.AddButton.clicked.connect(self.load_register_page)
        self.admin_ui.RemoveButton.clicked.connect(self.load_remove_page)
        self.admin_ui.ReturnButton.clicked.connect(lambda: self.load_test_parameters_page(False))
        self.admin_ui.LogOffButton.clicked.connect(self.log_off)
        for button in self.admin_ui.centralwidget.findChildren(QPushButton):
            button.setDefault(True)
    # ===== Register New Physiotherapist
    def setup_register_ui(self):
        self.register_ui = Ui_RegisterNewPhysiotherapist()
        self.register_ui.setupUi(self.parent_window)
        self.translate_register_ui()

        self.register_ui.comboBoxLanguage.currentIndexChanged.connect(
            lambda: self.handle_language_change(self.register_ui.comboBoxLanguage, "register")
        )
        self.set_language_combobox(self.register_ui.comboBoxLanguage)

        self.register_ui.AddButton.clicked.connect(lambda: self.handle_registration(self.register_ui))
        self.register_ui.ReturnButton.clicked.connect(lambda: self.load_test_parameters_page(False))
        self.register_ui.LogOffButton.clicked.connect(self.log_off)
        self.register_ui.lineEdit_Email.editingFinished.connect(lambda: self.handle_email_finished(self.register_ui))

        for error_label in [self.register_ui.error_Email, self.register_ui.error_Username, self.register_ui.error_Gender,
                            self.register_ui.error_First_Name, self.register_ui.error_Last_Name, self.register_ui.error_Password,
                            self.register_ui.error_Password_Confirmation]:
            error_label.setStyleSheet(f"color: {self.error_color}")
            error_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            error_label.hide()
        # self.register_ui.error_Email.setStyleSheet(f"color: {self.error_color}")
        # self.register_ui.error_Email.hide()
        # self.register_ui.error_Username.setStyleSheet(f"color: {self.error_color}")
        # self.register_ui.error_Username.hide()
        # self.register_ui.error_Gender.setStyleSheet(f"color: {self.error_color}")
        # self.register_ui.error_Gender.hide()
        # self.register_ui.error_First_Name.setStyleSheet(f"color: {self.error_color}")
        # self.register_ui.error_First_Name.hide()
        # self.register_ui.error_Last_Name.setStyleSheet(f"color: {self.error_color}")
        # self.register_ui.error_Last_Name.hide()
        # self.register_ui.error_Password.setStyleSheet(f"color: {self.error_color}")
        # self.register_ui.error_Password.hide()
        # self.register_ui.error_Password_Confirmation.setStyleSheet(f"color: {self.error_color}")
        # self.register_ui.error_Password_Confirmation.hide()
        self.register_ui.dateEdit_Date_Of_Birth.setDate(QDate.currentDate())
        self.setup_password_visibility(self.register_ui)
        for line_edit in self.register_ui.centralwidget.findChildren(QLineEdit):
            line_edit.returnPressed.connect(lambda: self.handle_registration(self.register_ui))
        for button in self.register_ui.centralwidget.findChildren(QPushButton):
            button.setDefault(True)
    # ===== Remove Existing Physiotherapists
    def setup_remove_ui(self):
        self.remove_ui = Ui_RemoveExistingPhysiotherapists()
        self.remove_ui.setupUi(self.parent_window)
        self.translate_remove_ui()

        self.remove_ui.comboBoxLanguage.currentIndexChanged.connect(
            lambda: self.handle_language_change(self.remove_ui.comboBoxLanguage, "remove")
        )
        self.set_language_combobox(self.remove_ui.comboBoxLanguage)

        self.remove_ui.RemoveButton.clicked.connect(self.remove_selected_physio)
        self.remove_ui.ReturnButton.clicked.connect(self.load_admin_page)
        self.remove_ui.LogOffButton.clicked.connect(self.log_off)
        self.populate_physios()
        for button in self.remove_ui.centralwidget.findChildren(QPushButton):
            button.setDefault(True)
    # ===== Test Parameters
    def setup_test_parameters_ui(self):
        self.test_parameters_ui = Ui_TestParameters()
        self.test_parameters_ui.setupUi(self.parent_window)
        self.translate_test_parameters_ui()

        self.apply_layout_direction_recursive(self.test_parameters_ui.centralwidget)
        self.test_parameters_ui.comboBoxLanguage.currentIndexChanged.connect(
            lambda: self.handle_language_change(self.test_parameters_ui.comboBoxLanguage, "test_parameters")
        )
        self.set_language_combobox(self.test_parameters_ui.comboBoxLanguage)

        self.test_parameters_ui.label_welcome_user.setText(self.translator.tr("Welcome_User_Dynamic", name=self.current_user['first_name']))
        self.test_parameters_ui.lineEdit_Patient_ID.textChanged.connect(self.restart_autofill_timer)
        self.test_parameters_ui.PatientHistoryButton.hide()
        self.test_parameters_ui.AdminPageButton.setVisible(self.current_user['is_admin'])
        self.test_parameters_ui.ContinueButton.clicked.connect(self.on_start_test_clicked)
        self.test_parameters_ui.PatientHistoryButton.clicked.connect(self.load_patient_history_page)
        self.test_parameters_ui.AdminPageButton.clicked.connect(self.load_admin_page)
        self.test_parameters_ui.CheckSystemButton.clicked.connect(self.load_check_system_page)
        self.test_parameters_ui.LogOffButton.clicked.connect(self.log_off)

        for error_label in [self.test_parameters_ui.error_Patient_Id, self.test_parameters_ui.error_Shoe_Width,
                            self.test_parameters_ui.error_Pelvic_Width, self.test_parameters_ui.error_Patient_Has_Fallen]:
            error_label.setStyleSheet(f"color: {self.error_color}")
            error_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            error_label.hide()
        # self.test_parameters_ui.error_Patient_Id.setStyleSheet(f"color: {self.error_color}")
        # self.test_parameters_ui.error_Patient_Id.hide()

        # self.test_parameters_ui.error_Shoe_Width.setStyleSheet(f"color: {self.error_color}")
        # self.test_parameters_ui.error_Shoe_Width.hide()
        # self.test_parameters_ui.error_Pelvic_Width.setStyleSheet(f"color: {self.error_color}")
        # self.test_parameters_ui.error_Pelvic_Width.hide()
        # self.test_parameters_ui.error_Patient_Has_Fallen.setStyleSheet(f"color: {self.error_color}")
        # self.test_parameters_ui.error_Patient_Has_Fallen.hide()
        self.test_parameters_ui.DT_Notes.hide()
        self.test_parameters_ui.dateEdit_Date_Of_Birth.setDate(QDate.currentDate())

        for line_edit in self.test_parameters_ui.centralwidget.findChildren(QLineEdit):
            line_edit.returnPressed.connect(self.on_start_test_clicked)
        for button in self.test_parameters_ui.centralwidget.findChildren(QPushButton):
            button.setDefault(True)
    # ===== Check System
    def setup_check_system_ui(self):
        self.check_system_ui = Ui_CheckSystemPage()
        self.check_system_ui.setupUi(self.parent_window)
        self.translate_check_system_ui()

        self.check_system_ui.comboBoxLanguage.currentIndexChanged.connect(
            lambda: self.handle_language_change(self.check_system_ui.comboBoxLanguage, "check_system")
        )
        self.set_language_combobox(self.check_system_ui.comboBoxLanguage)

        self.check_system_ui.ExplorerButton.clicked.connect(lambda: os.startfile(self.explorer))
        self.check_system_ui.DiagnosticButton.clicked.connect(lambda: os.startfile(self.diagnostic))
        self.check_system_ui.ReturnButton.clicked.connect(lambda: self.load_test_parameters_page(False))
        self.check_system_ui.LogOffButton.clicked.connect(self.log_off)
        for button in self.check_system_ui.centralwidget.findChildren(QPushButton):
            button.setDefault(True)
    # ===== Preparation
    def setup_preparation_ui(self):
        self.preparation_ui = Ui_PreparationPage()
        self.preparation_ui.setupUi(self.parent_window)
        self.translate_preparation_ui()

        self.preparation_ui.comboBoxLanguage.currentIndexChanged.connect(
            lambda: self.handle_language_change(self.preparation_ui.comboBoxLanguage, "preparation")
        )
        self.set_language_combobox(self.preparation_ui.comboBoxLanguage)

        self.preparation_ui.StartTestButton.clicked.connect(lambda: self.load_result_page(self.pelvic_width, self.shoe_width, self.has_fall_last_year))
        self.preparation_ui.StartTestButton.setDefault(True)
        self.preparation_ui.StartTestButton.setFocus()
    # # ===== Test Status
    # def setup_test_status_ui(self):
    #     self.test_status_ui = Ui_TestStatusPage()
    #     self.test_status_ui.setupUi(self.parent_window)
    #     # self.test_status_ui.pushButton_Ready.clicked.connect()
    #     for button in self.test_status_ui.centralwidget.findChildren(QPushButton):
    #         button.setDefault(True)
    # ===== Results Analysis
    def setup_result_ui(self):
        self.result_ui = Ui_ResultsAnalysisPage()
        self.result_ui.setupUi(self.parent_window)
        self.translate_results_analysis_ui()

        self.result_ui.comboBoxLanguage.currentIndexChanged.connect(
            lambda: self.handle_language_change(self.result_ui.comboBoxLanguage, "results")
        )
        self.set_language_combobox(self.result_ui.comboBoxLanguage)

        self.result_ui.NewTestButton.clicked.connect(lambda: self.load_test_parameters_page(False))
        self.result_ui.HistoryResultsButton.clicked.connect(self.load_patient_history_page)
        self.result_ui.LogOffButton.clicked.connect(self.log_off)
        for button in self.result_ui.centralwidget.findChildren(QPushButton):
            button.setDefault(True)
    # ===== Patient's History
    def setup_patient_history_ui(self):
        self.patient_hisory_ui = Ui_PatientHistoryPage()
        self.patient_hisory_ui.setupUi(self.parent_window)
        self.translate_patient_history_ui()

        self.patient_hisory_ui.comboBoxLanguage.currentIndexChanged.connect(
            lambda: self.handle_language_change(self.patient_hisory_ui.comboBoxLanguage, "patient_history")
        )
        self.set_language_combobox(self.patient_hisory_ui.comboBoxLanguage)

        today = QDate.currentDate()
        one_year_ago = today.addYears(-1)
        self.patient_hisory_ui.dateEdit_From.setDate(one_year_ago)
        self.patient_hisory_ui.dateEdit_To.setDate(today)

        # self.patient_hisory_ui.dateEdit_From.dateChanged.connect(self.filter_results_by_date)
        # self.patient_hisory_ui.dateEdit_To.dateChanged.connect(self.filter_results_by_date)


        # self.patient_hisory_ui.dateEdit_From.setDate(QDate.currentDate().addDays(-30))
        # self.patient_hisory_ui.dateEdit_To.setDate(QDate.currentDate())

        # self.dashboard_manager = DashboardManager(
        #     container_widget=self.patient_hisory_ui.plotWidget,
        #     graph_manager_factory=lambda parent: GraphManager(parent)
        # )

        self.patient_hisory_ui.dateEdit_From.dateChanged.connect(self.filter_results_by_date)
        self.patient_hisory_ui.dateEdit_To.dateChanged.connect(self.filter_results_by_date)
        self.patient_hisory_ui.NewTestButton.clicked.connect(lambda: self.load_test_parameters_page(False))
        self.patient_hisory_ui.LogOffButton.clicked.connect(self.log_off)
        self.patient_hisory_ui.ExportToCSVButton.clicked.connect(lambda: self.export_history_to_csv(self.current_patient_id))

        for button in self.patient_hisory_ui.centralwidget.findChildren(QPushButton):
            button.setDefault(True)
        self.filter_results_by_date()

    def center_maximized_window(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        screen_center = screen_geometry.center()

        window_size = self.parent_window.size()
        new_x = screen_center.x() - window_size.width() // 2
        new_y = screen_center.y() - window_size.height() // 2

        self.parent_window.move(new_x, new_y)
    # endregion

    # region Load Pages
    # ===== Login
    def load_login_page(self, first_name=None):
        QTimer.singleShot(1, self.center_maximized_window)
        self.setup_login_ui()

        if first_name is None:
            self.login_ui.label_goodbye_user.hide()
        else:
            self.login_ui.label_goodbye_user.setText(self.translator.tr("Goodbye_User_Dynamic", name=first_name))

        # If there are physical therapists in the system, then the First Use button isn't needed
        if self.has_physiotherapists():
            self.login_ui.FirstUseButton.hide()
    # ===== First Use
    def load_first_use_page(self):
        self.setup_first_use_ui()
        QTimer.singleShot(1, self.center_maximized_window)
    # ===== Test Parameters
    def load_test_parameters_page(self, is_login):
        QTimer.singleShot(1, self.center_maximized_window)
        if is_login:
            if self.validate_login(self.login_ui.lineEdit_Username.text(), self.login_ui.lineEdit_Password.text()):
                self.setup_test_parameters_ui()
                if not self.current_user["is_admin"]:
                    self.test_parameters_ui.AdminPageButton.hide()
                    self.test_parameters_ui.CheckSystemButton.setGeometry(QRect(20, 490, 81, 24))
            else:
                self.login_ui.error_Username_or_Password.setText(self.translator.tr("error_Username_or_Password"))
                self.login_ui.error_Username_or_Password.show()
                self.login_ui.label_Forgot_Password.show()
                self.login_ui.label_Forgot_Password.setText(self.translator.tr("forgot_password"))
                self.login_ui.label_Forgot_Password.setCursor(QCursor(Qt.PointingHandCursor))
                self.login_ui.label_Forgot_Password.mousePressEvent = lambda event: self.load_reset_password()

        else:
            self.setup_test_parameters_ui()
            if not self.current_user["is_admin"]:
                self.test_parameters_ui.AdminPageButton.hide()
                self.test_parameters_ui.CheckSystemButton.setGeometry(QRect(20, 490, 81, 24))
    # ===== Admin
    def load_admin_page(self):
        self.setup_admin_ui()
        QTimer.singleShot(1, self.center_maximized_window)
    # ===== Register New Physiotherapist
    def load_register_page(self):
        self.setup_register_ui()
        QTimer.singleShot(1, self.center_maximized_window)
    # ===== Remove Existing Physiotherapists
    def load_remove_page(self):
        self.setup_remove_ui()
        QTimer.singleShot(1, self.center_maximized_window)
    # ===== Check System
    def load_check_system_page(self):
        self.setup_check_system_ui()
        QTimer.singleShot(1, self.center_maximized_window)
    # ===== Preparation
    def load_preparation_page(self, pelvic_width, shoe_width, has_fall_last_year):
        self.pelvic_width = pelvic_width
        self.shoe_width = shoe_width
        self.has_fall_last_year = has_fall_last_year
        self.setup_preparation_ui()
        self.parent_window.setCentralWidget(self.preparation_ui.centralwidget)
        QTimer.singleShot(1, self.center_maximized_window)
    # ===== Results Analysis
    def load_result_page(self, pelvic_width, shoe_width, has_fall_last_year):
        self.setup_result_ui()
        self.parent_window.setCentralWidget(self.result_ui.centralwidget)
        QTimer.singleShot(1, self.center_maximized_window)

        real_steps_count = random.randint(7, 30)
        real_wrong_steps = random.randint(0, 20)
        while real_wrong_steps > real_steps_count:
            real_wrong_steps = random.randint(0, 20)
        time_seconds = random.random() * 20 + 5
        # time_seconds = self.end_time - self.test_start_time
        fall_risk_prob = predict_risk_probability(
            steps_count=real_steps_count,
            wrong_steps=real_wrong_steps,
            trial_time=time_seconds
        )

        # Conversion to percentages
        fall_risk_percent = round(fall_risk_prob * 100, 4)

        # שלב 1: שליפת ההערה האחרונה והתאריך שלה
        last_note_text, _ = DatabaseUtils.get_last_note(self.current_patient_id)

        # שלב 2: הערה שהוזנה כעת
        new_note = self.current_notes

        # שלב 3: אם ההערה החדשה זהה להערה הקודמת — נכניס None, אחרת נכניס אותה
        self.note_to_save = None if new_note == last_note_text else new_note

        # Inserting a new test
        test_id = DatabaseUtils.insert_new_test(
            physiotherapist_email = self.current_user["email"],
            patient_id = self.current_patient_id,
            start_time = self.start_time,
            end_time = datetime.now(),
            test_status = "Finished",
            notes = self.note_to_save
        )
        if test_id is None:
            QMessageBox.critical(None, self.translator.tr("test_fail_title"), self.translator.tr("test_fail_text"))

            return

        self.result_ui.tableWidget_Results.setItem(-1, 1, QTableWidgetItem(f"{fall_risk_percent}%"))
        self.result_ui.tableWidget_Results.setItem(0, 1, QTableWidgetItem(f"{time_seconds:.1f} sec"))
        self.result_ui.tableWidget_Results.setItem(1, 1, QTableWidgetItem(str(real_steps_count)))
        self.result_ui.tableWidget_Results.setItem(2, 1, QTableWidgetItem(str(real_wrong_steps)))

        # # פריט סיכון לנפילה
        # fall_item = QTableWidgetItem(f"{fall_risk_percent}%")
        # fall_item.setFont(QFont("Arial", 12, QFont.Bold))
        # self.result_ui.tableWidget_Results.setItem(-1, 1, fall_item)
        #
        # # זמן בדיקה
        # time_item = QTableWidgetItem(f"{time_seconds:.1f} sec")
        # time_item.setFont(QFont("Arial", 12))
        # self.result_ui.tableWidget_Results.setItem(0, 1, time_item)
        #
        # # פריט מספר צעדים
        # steps_item = QTableWidgetItem(str(real_steps_count))
        # steps_item.setFont(QFont("Arial", 12))
        # self.result_ui.tableWidget_Results.setItem(1, 1, steps_item)
        #
        # # פריט צעדים שגויים
        # wrong_item = QTableWidgetItem(str(real_wrong_steps))
        # wrong_item.setFont(QFont("Arial", 12))
        # self.result_ui.tableWidget_Results.setItem(2, 1, wrong_item)

        # שמירת נתוני הבדיקה במסד הנתונים
        DatabaseUtils.save_test_results(
            test_id = test_id,
            patient_id = self.current_patient_id,
            fall_risk_prob = fall_risk_prob,
            real_steps_count = real_steps_count,
            real_wrong_steps = real_wrong_steps,
            pelvic_width = pelvic_width,
            shoe_width = shoe_width,
            has_fall_last_year = has_fall_last_year
        )
        self.save_test_result_to_csv(
            patient_id = self.current_patient_id,
            test_time_sec = time_seconds,
            risk_level = fall_risk_prob,
            total_steps = real_steps_count,
            error_steps = real_wrong_steps
        )
    # ===== Patient's History
    def load_patient_history_page(self):
        self.setup_patient_history_ui()
        QTimer.singleShot(1, self.center_maximized_window)
        self.patient_hisory_ui.widget_Gauge.setStyleSheet("background-color: white")
        self.patient_hisory_ui.widget_FallRisk.setStyleSheet("background-color: white")
        self.patient_hisory_ui.widget_StepCount.setStyleSheet("background-color: white")
        self.patient_hisory_ui.widget_ErrorSteps.setStyleSheet("background-color: white")
    # ==== Reset Password
    def load_reset_password(self):
        self.setup_reset_password_ui()
        QTimer.singleShot(1, self.center_maximized_window)
    # ===== Log Off
    def log_off(self):
        first_name = self.current_user["first_name"]
        self.current_user = {"email": None, "first_name": None, "is_admin": False, "password_last_changed": None}
        self.inactivity_timer.stop()
        self.logout_timer.stop()
        self.load_login_page(first_name)
    # endregion

    # region Physiotherapist Registration and Management

    #region Login
    # Checks if there are records in the Physiotherapists table in the database. If so - return true
    def has_physiotherapists(self):
        return DatabaseUtils.has_physiotherapists()

    # Searches for a match between the entered password and values in the database.
    def validate_login(self, username, password):
        result = DatabaseUtils.get_login_data(username)
        if result:
            email, first_name, db_password, password_last_changed, is_admin, preferred_language = result
            if self.check_password(password, db_password):
                self.current_user = {
                    "email": email,
                    "first_name": first_name,
                    "is_admin": bool(is_admin),
                    "password_last_changed": password_last_changed,
                    "preferred_language": preferred_language
                }
                print(self.current_user["preferred_language"])
                return True
        return False

    def handle_reset_password(self):
        email = self.reset_ui.lineEdit_Email.text().strip().lower()
        password = self.reset_ui.lineEdit_Password.text()
        password_conf = self.reset_ui.lineEdit_Password_Confirmation.text()

        # Reset error messages
        self.reset_ui.error_Email.hide()
        self.reset_ui.error_Password.hide()
        self.reset_ui.error_Password_Confirmation.hide()

        valid = True

        if '@' not in email:
            self.reset_ui.error_Email.setText(self.translator.tr("error_Email@"))
            self.reset_ui.error_Email.show()
            valid = False
        if not password:
            self.reset_ui.error_Password.setText(self.translator.tr("error_Password"))
            self.reset_ui.error_Password.show()
            valid = False
        if password != password_conf:
            self.reset_ui.error_Password_Confirmation.setText(self.translator.tr("error_Password_Confirmation"))
            self.reset_ui.error_Password_Confirmation.show()
            valid = False

        if not valid:
            return

        # Checking if an email exists in the database
        if not DatabaseUtils.email_exists(email):
            self.reset_ui.error_Email.setText(self.translator.tr("error_Email_Not_Found"))
            self.reset_ui.error_Email.show()
            return

        # Password encryption
        hashed = self.hash_password(password)
        success = DatabaseUtils.reset_password(email, hashed)
        if success:
            QMessageBox.information(None, self.translator.tr("password_reset_success_title"), self.translator.tr("password_reset_success_text"))
            self.load_login_page()
        else:
            QMessageBox.critical(None, self.translator.tr("password_reset_fail_title"), self.translator.tr("password_reset_fail_text"))
    #endregion

    #region Registration
    def handle_email_finished(self, ui):
        email = ui.lineEdit_Email.text().strip().lower()
        if '@' not in email:
            ui.error_Email.setText(self.translator.tr("error_Email@"))
            ui.error_Email.show()
            self.set_fields_editable(ui, False)
            return

        # Step 1: Check if there is an active user with the same email
        active_count = DatabaseUtils.get_existing_physiotherapist_by_email(email)
        if active_count > 0:
            ui.error_Email.setText(self.translator.tr("error_Email_Already_Exist"))
            ui.error_Email.show()
            self.set_fields_editable(ui, False)
            return

        # Step 2: Check if there is an inactive user (Is_Active = 0)
        row = DatabaseUtils.get_inactive_physiotherapist_details(email)
        if row:
            username, fname, lname, gender, dob = row
            ui.error_Email.hide()
            self.set_fields_editable(ui, True)

            # Autofill fields with editing option
            ui.lineEdit_Username.setText(username)
            ui.lineEdit_First_Name.setText(fname)
            ui.lineEdit_Last_Name.setText(lname)
            ui.comboBox_Gender.setCurrentText(gender)
            ui.dateEdit_Date_Of_Birth.setDate(dob)
        else:
            # Step 3: New Email - Suggests a New Username
            ui.error_Email.hide()
            self.set_fields_editable(ui, True)
            base_username = email.split('@')[0]
            usernames = DatabaseUtils.get_existing_physiotherapists(base_username)
            if base_username not in usernames:
                suggested = base_username
            else:
                i = 1
                while f"{base_username}{i}" in usernames:
                    i += 1
                suggested = f"{base_username}{i}"
            ui.lineEdit_Username.setText(suggested)

    def set_fields_editable(self, ui, editable):
        ui.lineEdit_Username.setReadOnly(not editable)
        ui.comboBox_Gender.setEnabled(editable)
        ui.dateEdit_Date_Of_Birth.setEnabled(editable)
        ui.lineEdit_First_Name.setReadOnly(not editable)
        ui.lineEdit_Last_Name.setReadOnly(not editable)
        ui.lineEdit_Password.setReadOnly(not editable)
        ui.lineEdit_Password_Confirmation.setReadOnly(not editable)
        # if ui == self.result_ui:
        #     ui.checkBox_Is_Admin.setEnabled(editable)

    # def generate_unique_username(self, base):
    #     try:
    #         conn = DatabaseUtils.get_connection()
    #         cursor = conn.cursor()
    #         cursor.execute("SELECT Username FROM PHYSIOTHERAPISTS WHERE Username LIKE ?", (f"{base}%",))
    #         results = cursor.fetchall()
    #         conn.close()
    #
    #         existing_usernames = {row[0] for row in results if row[0] is not None}
    #         if base not in existing_usernames:
    #             return base
    #
    #         i = 1
    #         while f"{base}{i}" in existing_usernames:
    #             i += 1
    #         return f"{base}{i}"
    #
    #     except Exception as e:
    #         print("❌ DB Error:", e)
    #         return base

    def register_physiotherapist(self, email, username, first_name, last_name, gender, dob, password, is_admin):
        # Password encryption
        hashed_password = self.hash_password(password)
        return DatabaseUtils.insert_physiotherapist(email, username, first_name, last_name, gender, dob, hashed_password, is_admin)

    def handle_registration(self, ui):
        ui.error_Email.hide()
        ui.error_Gender.hide()
        ui.error_First_Name.hide()
        ui.error_Last_Name.hide()
        ui.error_Password.hide()

        email = ui.lineEdit_Email.text().strip()
        first_name = ui.lineEdit_First_Name.text().strip()
        last_name = ui.lineEdit_Last_Name.text().strip()
        password = ui.lineEdit_Password.text()
        password_conf = ui.lineEdit_Password_Confirmation.text()
        gender = ui.comboBox_Gender.currentText()
        dob = ui.dateEdit_Date_Of_Birth.date().toPython()
        if ui == self.register_ui:
            is_admin = ui.checkBox_Is_Admin.isChecked()
        else:
            is_admin = "1"

        valid = True
        if '@' not in email:
            ui.error_Email.setText(self.translator.tr("error_Email@"))
            ui.error_Email.show()
            valid = False
        if ui.comboBox_Gender.currentIndex() == -1:
            ui.error_Gender.setText(self.translator.tr("error_Gender"))
            ui.error_Gender.show()
            valid = False
        if not re.match(r"^[A-Za-z֐-׿]+$", first_name):
            ui.error_First_Name.setText(self.translator.tr("error_First_Name"))
            ui.error_First_Name.show()
            valid = False
        if not re.match(r"^[A-Za-z֐-׿]+$", last_name):
            ui.error_Last_Name.setText(self.translator.tr("error_Last_Name"))
            ui.error_Last_Name.show()
            valid = False
        if not password:
            ui.error_Password.setText(self.translator.tr("error_Password"))
            ui.error_Password.show()
            valid = False
        if password != password_conf:
            ui.error_Password_Confirmation.setText(self.translator.tr("error_Password_Confirmation"))
            ui.error_Password_Confirmation.show()
            valid = False

        if DatabaseUtils.email_exists(email):
            ui.error_Email.setText(self.translator.tr("error_Email_Already_Exist"))
            ui.error_Email.show()
            return

        username = ui.lineEdit_Username.text().strip()
        if DatabaseUtils.username_exists(username):
            ui.error_Username.setText(self.translator.tr("error_Username_Already_Exist"))
            ui.error_Username.show()
            return
        else:
            ui.error_Username.hide()

        if not valid:
            return

        if self.register_physiotherapist(email, username, first_name, last_name, gender, dob, password, is_admin):
            QMessageBox.information(None, self.translator.tr("register_success_title"), self.translator.tr("register_success_text"))
            if ui == self.first_use_ui:
                self.current_user = {
                    "email": email,
                    "first_name": first_name,
                    "is_admin": bool(is_admin),
                    "password_last_changed": datetime.now()
                }
            self.load_test_parameters_page(False)
        else:
            QMessageBox.critical(None, self.translator.tr("register_fail_title"), self.translator.tr("register_fail_text"))
    #endregion

    #region Removal
    def remove_selected_physio(self):
        selected_row = self.remove_ui.tableWidget_Physiotherapists.currentRow()
        if selected_row >= 0:
            email = self.remove_ui.tableWidget_Physiotherapists.item(selected_row, 0).text()
            confirm = QMessageBox.question(
                None,
                self.translator.tr("delete_confirm_title"),
                self.translator.tr("delete_confirm_text", email=email),
                QMessageBox.Yes | QMessageBox.No
            )
            if confirm == QMessageBox.Yes:
                success = DatabaseUtils.soft_delete_physio(email)
                if success:
                    self.populate_physios()
                    QMessageBox.information(None, self.translator.tr("delete_success_title"), self.translator.tr("delete_success_text"))
                    self.load_test_parameters_page(False)
                else:
                    QMessageBox.critical(None, self.translator.tr("delete_fail_title"), self.translator.tr("delete_fail_text"))
        else:
            QMessageBox.warning(None, self.translator.tr("delete_no_selection_title"), self.translator.tr("delete_no_selection_text"))

    def populate_physios(self):
        self.remove_ui.tableWidget_Physiotherapists.setRowCount(0)
        rows = DatabaseUtils.get_all_physios_except(self.current_user["email"])

        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem(str(value) if not isinstance(value, bool) else ("Yes" if value else "No"))
                self.remove_ui.tableWidget_Physiotherapists.setItem(row_idx, col_idx, item)

        # for row_idx, (email, username, fname, lname, gender, age, is_admin) in enumerate(rows):
        #     self.remove_ui.tableWidget_Physiotherapists.insertRow(row_idx)
        #     self.remove_ui.tableWidget_Physiotherapists.setItem(row_idx, 0, QTableWidgetItem(email))
        #     self.remove_ui.tableWidget_Physiotherapists.setItem(row_idx, 1, QTableWidgetItem(username))
        #     self.remove_ui.tableWidget_Physiotherapists.setItem(row_idx, 2, QTableWidgetItem(fname))
        #     self.remove_ui.tableWidget_Physiotherapists.setItem(row_idx, 3, QTableWidgetItem(lname))
        #     self.remove_ui.tableWidget_Physiotherapists.setItem(row_idx, 4, QTableWidgetItem(gender))
        #     self.remove_ui.tableWidget_Physiotherapists.setItem(row_idx, 5, QTableWidgetItem(str(age)))
        #     self.remove_ui.tableWidget_Physiotherapists.setItem(row_idx, 6, QTableWidgetItem("Yes" if is_admin else "No"))
    #endregion

    # endregion

    # region Start Test
    def create_patient_if_not_exists(self, patient_id, gender, dob):
        DatabaseUtils.create_patient_if_needed(patient_id, gender, dob)

    # Checks if the ID is valid (only numbers 9 in length) and if so - moves to the status page.
    def on_start_test_clicked(self):
        patient_id = self.test_parameters_ui.lineEdit_Patient_ID.text().strip()
        id_approved = True
        pelvic_approved = True
        shoe_approved = True
        has_fallen_approved = True

        if not patient_id.isdigit():
            self.test_parameters_ui.error_Patient_Id.setText(self.translator.tr("error_Patient_Id_isdigit"))
            self.test_parameters_ui.error_Patient_Id.show()
            id_approved = False

        if len(patient_id) != 9:
            self.test_parameters_ui.error_Patient_Id.setText(self.translator.tr("error_Patient_Id_length"))
            self.test_parameters_ui.error_Patient_Id.show()
            id_approved = False

        if id_approved:
            self.test_parameters_ui.error_Patient_Id.hide()

        self.current_patient_id = patient_id
        self.start_time = datetime.now()

        # Read values from input fields
        pelvic_width_text = self.test_parameters_ui.lineEdit_Pelvic_Width.text().strip()
        shoe_width_text = self.test_parameters_ui.lineEdit_Shoe_Width.text().strip()
        has_fall_last_year_text = self.test_parameters_ui.comboBox_Has_Fallen.currentText().strip()

        # === Pelvic Width ===
        pelvic_range = DatabaseUtils.get_valid_range(4)
        min_pelvic, max_pelvic = DatabaseUtils.parse_range(pelvic_range)

        if not pelvic_width_text:
            self.test_parameters_ui.error_Pelvic_Width.setText(self.translator.tr("error_Pelvic_Width_Empty"))
            self.test_parameters_ui.error_Pelvic_Width.show()
            pelvic_approved = False

        if not pelvic_width_text.replace('.', '', 1).isdigit():
            self.test_parameters_ui.error_Pelvic_Width.setText(self.translator.tr("error_Pelvic_Width_numeric"))
            self.test_parameters_ui.error_Pelvic_Width.show()
            pelvic_approved = False

        if pelvic_approved:
            pelvic_width = float(pelvic_width_text)
            if not (min_pelvic <= pelvic_width <= max_pelvic):
                self.test_parameters_ui.error_Pelvic_Width.setText(self.translator.tr("error_Pelvic_Width", min=min_pelvic, max=max_pelvic))
                self.test_parameters_ui.error_Pelvic_Width.show()
                pelvic_approved = False

            if pelvic_approved:
                self.test_parameters_ui.error_Pelvic_Width.hide()

        # === Shoe Width ===
        shoe_range = DatabaseUtils.get_valid_range(5)
        min_shoe, max_shoe = DatabaseUtils.parse_range(shoe_range)

        if not shoe_width_text:
            self.test_parameters_ui.error_Shoe_Width.setText(self.translator.tr("error_Shoe_Width_Empty"))
            self.test_parameters_ui.error_Shoe_Width.show()
            shoe_approved = False

        if not shoe_width_text.replace('.', '', 1).isdigit():
            self.test_parameters_ui.error_Shoe_Width.setText(self.translator.tr("error_Shoe_Width_numeric"))
            self.test_parameters_ui.error_Shoe_Width.show()
            shoe_approved = False

        if shoe_approved:
            shoe_width = float(shoe_width_text)
            if not (min_shoe <= shoe_width <= max_shoe):
                self.test_parameters_ui.error_Shoe_Width.setText(self.translator.tr("error_Shoe_Width", min=min_shoe, max=max_shoe))
                self.test_parameters_ui.error_Shoe_Width.show()
                shoe_approved = False
            if shoe_approved:
                self.test_parameters_ui.error_Shoe_Width.hide()

        # === Has Fallen ===
        valid_fall_values = ["yes", "no", "כן", "לא"]
        if has_fall_last_year_text.lower() not in valid_fall_values:
            self.test_parameters_ui.error_Patient_Has_Fallen.setText(self.translator.tr("error_Patient_Has_Fallen"))
            self.test_parameters_ui.error_Patient_Has_Fallen.show()
            has_fallen_approved = False
        if has_fallen_approved:
            self.test_parameters_ui.error_Patient_Has_Fallen.hide()
        has_fall_last_year = 1 if has_fall_last_year_text.lower() in ["yes", "כן"] else 0

        if id_approved and pelvic_approved and shoe_approved and has_fallen_approved:
            # Create the patient if it does not exist
            gender = self.test_parameters_ui.comboBox_Gender.currentText()
            dob = self.test_parameters_ui.dateEdit_Date_Of_Birth.date().toPython()
            self.create_patient_if_not_exists(patient_id, gender, dob)
            self.current_notes = self.test_parameters_ui.textEdit_Notes.toPlainText().strip()
            self.load_preparation_page(pelvic_width, shoe_width, has_fall_last_year)

    # Automatically loads patient data (gender, age, parameters) after typing ID.
    def autofill_patient_data(self):
        patient_id = self.test_parameters_ui.lineEdit_Patient_ID.text().strip()
        self.test_parameters_ui.PatientHistoryButton.setVisible(DatabaseUtils.has_patient_test_history(patient_id))

        if not patient_id.isdigit():
            self.test_parameters_ui.dateEdit_Date_Of_Birth.setEnabled(True)
            return

        # Retrieving personal data (gender, date of birth)
        info = DatabaseUtils.get_patient_info(patient_id)
        if info:
            self.current_patient_id = patient_id
            self.test_parameters_ui.error_Patient_Id.hide()
            self.test_parameters_ui.error_Shoe_Width.hide()
            self.test_parameters_ui.error_Pelvic_Width.hide()
            self.test_parameters_ui.error_Patient_Has_Fallen.hide()
            self.test_parameters_ui.comboBox_Gender.setCurrentText(info["gender"])
            self.test_parameters_ui.dateEdit_Date_Of_Birth.setDate(info["dob"])
            self.test_parameters_ui.dateEdit_Date_Of_Birth.setEnabled(False)
        else:
            self.test_parameters_ui.comboBox_Gender.setCurrentIndex(-1)
            self.test_parameters_ui.dateEdit_Date_Of_Birth.setDate(QDate.currentDate())
            self.test_parameters_ui.dateEdit_Date_Of_Birth.setEnabled(True)

        # Retrieving recent parameters from the database
        params = DatabaseUtils.get_recent_parameters(patient_id, self.param_days_back)
        if params:
            # Shoe Width
            if not self.test_parameters_ui.lineEdit_Shoe_Width.text().strip():
                shoe = params.get("Shoe_Width", "")
                self.test_parameters_ui.lineEdit_Shoe_Width.setText(shoe)

            # Pelvic Width
            if not self.test_parameters_ui.lineEdit_Pelvic_Width.text().strip():
                pelvic = params.get("Pelvic_Width", "")
                self.test_parameters_ui.lineEdit_Pelvic_Width.setText(pelvic)

            # Fall in last year
            if self.test_parameters_ui.comboBox_Has_Fallen.currentIndex() == -1:
                has_fallen = params.get("Fall_Last_Year", "").strip().lower()
                if has_fallen in ["yes", "1", "true", "כן"]:
                    self.test_parameters_ui.comboBox_Has_Fallen.setCurrentText("Yes")
                elif has_fallen in ["no", "0", "false", "לא"]:
                    self.test_parameters_ui.comboBox_Has_Fallen.setCurrentText("No")
        else:
            self.test_parameters_ui.lineEdit_Shoe_Width.clear()
            self.test_parameters_ui.lineEdit_Pelvic_Width.clear()
            self.test_parameters_ui.comboBox_Has_Fallen.setCurrentIndex(-1)

        # Load latest non-empty Note for the patient
        note_row = DatabaseUtils.get_latest_note(patient_id)
        if note_row:
            note_text, start_time = note_row
            self.test_parameters_ui.textEdit_Notes.setText(note_text)
            self.test_parameters_ui.DT_Notes.setText(start_time.strftime("%d.%m.%Y"))
            self.test_parameters_ui.DT_Notes.setVisible(True)
        else:
            self.test_parameters_ui.textEdit_Notes.clear()
            self.test_parameters_ui.DT_Notes.setVisible(False)
    # endregion

    # region Saving results and analysis
    def save_test_result_to_csv(self, patient_id, test_time_sec, risk_level, total_steps, error_steps):
        os.makedirs(self.csv_folder, exist_ok=True)

        now = datetime.now()
        timestamp = now.strftime("%d-%m-%Y")#_%H:%M")
        # File name by patient ID
        filename = f"{self.csv_folder}/Patient_{patient_id}_{timestamp}_Result.csv"

        # Does the file already exist
        file_exists = os.path.isfile(filename)

        # Writing the data
        with open(filename, mode='a', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)

            # Title only if the file is new
            if not file_exists:
                writer.writerow(["Patient ID", "Date", "Time", "Fall Risk", "Total Steps", "Error Steps", "Test Duration (s)", "Notes"])

            print("Notes to be saved:", self.note_to_save)

            writer.writerow([
                patient_id,
                now.strftime("%d-%m-%Y"),
                now.strftime("%H:%M:%S"),
                risk_level,
                total_steps,
                error_steps,
                f"{test_time_sec:.2f}",
                self.note_to_save or ""
            ])

    def export_history_to_csv(self, patient_id: int):
        os.makedirs(self.csv_folder, exist_ok=True)

        # שם קובץ לפי טווח תאריכים
        date_from_str = self.patient_hisory_ui.dateEdit_From.date().toString("dd-MM-yyyy")
        date_to_str = self.patient_hisory_ui.dateEdit_To.date().toString("dd-MM-yyyy")
        filename = f"{self.csv_folder}/Patient_{patient_id}_{date_from_str}_To_{date_to_str}_History.csv"

        row_count = self.patient_hisory_ui.tableWidget_History.rowCount()
        col_count = self.patient_hisory_ui.tableWidget_History.columnCount()

        if row_count == 0:
            QMessageBox.warning(None, self.translator.tr("no_data_title"), self.translator.tr("no_data_text"))
            return

        with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)

            # כותרות עמודות מתוך הטבלה
            headers = [self.patient_hisory_ui.tableWidget_History.horizontalHeaderItem(col).text() for col in range(col_count)]
            writer.writerow(headers)

            # כתיבת כל השורות בטווח תאריכים
            for row in range(row_count):
                test_date_item = self.patient_hisory_ui.tableWidget_History.item(row, 0)
                if not test_date_item:
                    continue

                test_date = QDate.fromString(test_date_item.text(), "yyyy-MM-dd")
                if not test_date.isValid():
                    test_date = QDate.fromString(test_date_item.text(), "dd/MM/yyyy")
                if not test_date.isValid():
                    continue  # תאריך לא תקין

                if test_date < self.patient_hisory_ui.dateEdit_From.date() or test_date > self.patient_hisory_ui.dateEdit_To.date():
                    continue  # מחוץ לטווח

                row_data = []
                for col in range(col_count):
                    item = self.patient_hisory_ui.tableWidget_History.item(row, col)
                    row_data.append(item.text() if item else "")
                writer.writerow(row_data)

        QMessageBox.information(None, self.translator.tr("export_success_title"), self.translator.tr("export_success_text", filename=filename))

    # endregion

    # region Inactivity Management (Session Timeout)
    def handle_inactivity_logout(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle(self.translator.tr("timeout_title"))
        msg.setText(self.translator.tr("timeout_text"))
        ok_button = msg.addButton(QMessageBox.Ok)
        ok_button.setCursor(QCursor(Qt.PointingHandCursor))
        msg.exec()
        self.log_off()

    def show_inactivity_warning(self):

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle(self.translator.tr("inactive_title"))
        msg.setText(self.translator.tr("inactive_message", minutes=self.session_time))

        yes_button = msg.addButton(QMessageBox.Yes)
        no_button = msg.addButton(QMessageBox.No)

        yes_button.setCursor(QCursor(Qt.PointingHandCursor))
        no_button.setCursor(QCursor(Qt.PointingHandCursor))

        msg.setDefaultButton(yes_button)
        msg.exec()

        if msg.clickedButton() == yes_button:
            self.inactivity_timer.start()
        else:
            self.handle_inactivity_logout()

    # Listens to mouse and keyboard events to initialize an inactivity timer, and stop the logout timer.
    def eventFilter(self, obj, event):
        if event.type() in (QEvent.MouseMove, QEvent.MouseButtonPress, QEvent.KeyPress):
            self.inactivity_timer.start()
            self.logout_timer.stop()
        return super().eventFilter(obj, event)
    # endregion

    # region GUI and Events Helper Methods
    # Starts a half-second timer, which at the end calls the autofill_patient_data function
    def restart_autofill_timer(self):
        self.autofill_timer.start(500)

    # region Password Visibility
    def setup_password_visibility(self, ui):
        ui.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)
        if hasattr(ui, "lineEdit_Password_Confirmation"):
            ui.lineEdit_Password_Confirmation.setEchoMode(QLineEdit.EchoMode.Password)

        ui.icon_eye_open = QIcon("images/eye_open.png")
        ui.icon_eye_closed = QIcon("images/eye_closed.png")

        ui.eye_action = QAction(ui.icon_eye_closed, "", ui.lineEdit_Password)
        # ui.eye_action = QAction(ui.icon_eye_closed, "Toggle password", ui.lineEdit_Password)
        ui.eye_action.setCheckable(True)
        ui.eye_action.toggled.connect(lambda checked: self.toggle_password_visibility(ui, checked))
        ui.lineEdit_Password.addAction(ui.eye_action, QLineEdit.ActionPosition.TrailingPosition)

        # Assign a hand cursor to the object that represents the eye action
        for child in ui.lineEdit_Password.children():
            if isinstance(child, QWidget) and child.toolTip() == "":
                child.setCursor(Qt.CursorShape.PointingHandCursor)

        if hasattr(ui, 'lineEdit_Password_Confirmation'):
            ui.eye_action_conf = QAction(ui.icon_eye_closed, "",
            # ui.eye_action_conf = QAction(ui.icon_eye_closed, "Toggle confirm password",
                                         ui.lineEdit_Password_Confirmation)
            ui.eye_action_conf.setCheckable(True)
            ui.eye_action_conf.toggled.connect(lambda checked: self.toggle_password_visibility_confirm(ui, checked))
            ui.lineEdit_Password_Confirmation.addAction(ui.eye_action_conf,
                                                        QLineEdit.ActionPosition.TrailingPosition)

            # Same for the confirmation field
            for child in ui.lineEdit_Password_Confirmation.children():
                if isinstance(child, QWidget) and child.toolTip() == "Toggle confirm password":
                    child.setCursor(Qt.CursorShape.PointingHandCursor)

    def toggle_password_visibility(self, ui, checked):
        if checked:
            ui.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Normal)
            ui.eye_action.setIcon(ui.icon_eye_open)
        else:
            ui.lineEdit_Password.setEchoMode(QLineEdit.EchoMode.Password)
            ui.eye_action.setIcon(ui.icon_eye_closed)

    def toggle_password_visibility_confirm(self, ui, checked):
        if checked:
            ui.lineEdit_Password_Confirmation.setEchoMode(QLineEdit.EchoMode.Normal)
            ui.eye_action_conf.setIcon(ui.icon_eye_open)
        else:
            ui.lineEdit_Password_Confirmation.setEchoMode(QLineEdit.EchoMode.Password)
            ui.eye_action_conf.setIcon(ui.icon_eye_closed)
    # endregion
    # endregion

    # region Maintenance and Control Functions
    # Reset the database from First Use Page
    def reset_database(self):
        title = self.translator.tr("reset_confirm_title")
        text = self.translator.tr("reset_confirm_text")
        confirm = QMessageBox.question(None, title, text, QMessageBox.Yes | QMessageBox.No)
        if confirm != QMessageBox.Yes:
            return

        success = DatabaseUtils.reset_main_tables()
        if success:
            QMessageBox.information(None, self.translator.tr("reset_success_title"), self.translator.tr("reset_success_text"))
        else:
            QMessageBox.critical(None, self.translator.tr("reset_fail_title"), self.translator.tr("reset_fail_text"))

    # endregion

    #region Password
    # Password encryption
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(), salt)
        return hashed.decode()

    # Password check
    def check_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
    #endregion

    # region Patient's History
    # # Filling the patient's history table
    # def populate_history_table(self, ui, patient_id):
    #     data = self.get_test_history(patient_id)
    #     ui.tableWidget_History.setRowCount(len(data))
    #     for row_idx, row in enumerate(data):
    #         for col_idx, item in enumerate(row):
    #             ui.tableWidget_History.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

    # Retrieving all data including physiotherapist name, fall risk, test duration, number of steps, etc. — then sending it to graphs
    def filter_results_by_date(self):
        start_date = self.patient_hisory_ui.dateEdit_From.date().toPython()
        end_date = self.patient_hisory_ui.dateEdit_To.date().toPython()

        results = DatabaseUtils.get_history_by_date_range(self.current_patient_id, start_date, end_date)
        self.patient_hisory_ui.tableWidget_History.setRowCount(0)

        # מילוי טבלת ההיסטוריה
        for row_num, row_data in enumerate(results):
            self.patient_hisory_ui.tableWidget_History.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                self.patient_hisory_ui.tableWidget_History.setItem(row_num, col_num, QTableWidgetItem(str(value)))

        if results:
            # יצירת גרף ראשי למבנה Gauge עם חיבורים ל־QLabel ו־QWidget
            df = pd.DataFrame(results,
                              columns=["Test Date", "Fall Risk", "Step Count", "Error Steps", "Start Time", "End Time",
                                       "Test Time"])

            # 🔄 עדכון גרף KPI לפי ה־DataFrame המסונן
            self.patient_hisory_ui.widget_Gauge_Canvas.setFixedSize(350, 305)
            gm_gauge = GraphManager(self.patient_hisory_ui.widget_Gauge_Canvas)
            gm_gauge.plot_success_gauge_kpi_from_df(
                df,
                title_label=self.patient_hisory_ui.label_Gauge_Title,
                percentage_label=self.patient_hisory_ui.label_Gauge_Percentage,
                translator = self.translator
            )
            print(f"SELECTED: {self.translator.__str__()}")
            print(self.translator)
            # 🔄 גרפים לפי טווח
            GraphManager(self.patient_hisory_ui.widget_FallRisk).plot_variable_over_time_from_df(df, "Fall Risk", translator = self.translator)
            GraphManager(self.patient_hisory_ui.widget_StepCount).plot_variable_over_time_from_df(df, "Step Count", translator = self.translator)
            GraphManager(self.patient_hisory_ui.widget_ErrorSteps).plot_variable_over_time_from_df(df, "Error Steps", translator = self.translator)
            # self.patient_hisory_ui.widget_Gauge_Canvas.setFixedSize(350, 305)
            # gm_gauge = GraphManager(self.patient_hisory_ui.widget_Gauge_Canvas)
            # gm_gauge.plot_success_gauge_kpi(
            #     patient_id=self.current_patient_id,
            #     title_label=self.patient_hisory_ui.label_Gauge_Title,
            #     percentage_label=self.patient_hisory_ui.label_Gauge_Percentage
            # )
            #
            # # שאר הגרפים
            # GraphManager(self.patient_hisory_ui.widget_FallRisk).plot_variable_over_time(self.current_patient_id, "Fall Risk")
            # GraphManager(self.patient_hisory_ui.widget_StepCount).plot_variable_over_time(self.current_patient_id, "Step Count")
            # GraphManager(self.patient_hisory_ui.widget_ErrorSteps).plot_variable_over_time(self.current_patient_id, "Error Steps")

    def update_results_table(self, results):
        self.tableWidget_Results.setRowCount(len(results))
        for row_index, row_data in enumerate(results):
            for col_index, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.tableWidget_Results.setItem(row_index, col_index, item)
    # endregion

    # region Language
    def apply_layout_direction_recursive(self, widget: QWidget):
        direction = Qt.RightToLeft if self.current_language == "he" else Qt.LeftToRight
        widget.setLayoutDirection(direction)

        for child in widget.findChildren(QWidget):
            child.setLayoutDirection(direction)

    def change_language(self, lang_code: str, page_name: str):
        save_language(lang_code)
        self.current_language = lang_code
        self.translator = Translator(language_code=lang_code)

        # Retranslate the active screen
        if page_name == "login":
            self.translate_login_ui()
        elif page_name == "test_parameters":
            self.translate_test_parameters_ui()
        elif page_name == "admin":
            self.translate_admin_ui()
        elif page_name == "reset_password":
            self.translate_reset_password_ui()
        elif page_name == "first_use":
            self.translate_first_use_ui()
        elif page_name == "register":
            self.translate_register_ui()
        elif page_name == "remove":
            self.translate_remove_ui()
        elif page_name == "patient_history":
            self.translate_patient_history_ui()
            self.filter_results_by_date()
        elif page_name == "preparation":
            self.translate_preparation_ui()
        elif page_name == "results":
            self.translate_results_analysis_ui()
        elif page_name == "check_system":
            self.translate_check_system_ui()
        else:
            print(f"⚠️ Page name '{page_name}' not recognized for translation.")

    def set_language_combobox(self, combobox):
        preferred_lang = self.current_user.get("preferred_language", "עברית")
        if preferred_lang == "English":
            combobox.setCurrentIndex(0)
        elif preferred_lang == "עברית":
            combobox.setCurrentIndex(1)

    def handle_language_change(self, combobox, page_name: str):
        index = combobox.currentIndex()
        if index == 0:
            new_lang = "en"
        elif index == 1:
            new_lang = "he"
        else:
            return  # אינדקס לא ידוע

        # שמירה במסד הנתונים
        if new_lang == "en":
            db_lang = "English"
        else:
            db_lang = "עברית"

        email = self.current_user.get("email")
        if email:
            DatabaseUtils.update_preferred_language(email, db_lang)

        save_language(new_lang)
        # עדכון מתרגם ושפה נוכחית
        self.current_language = new_lang
        self.translator = Translator(language_code=new_lang)

        # תרגום מחדש של הדף הנוכחי
        match page_name:
            case "test_parameters":
                self.translate_test_parameters_ui()
            case "results":
                self.translate_results_analysis_ui()
            case "register":
                self.translate_register_ui()
            case "admin":
                self.translate_admin_ui()
            case "first_use":
                self.translate_first_use_ui()
            case "check_system":
                self.translate_check_system_ui()
            case "remove":
                self.translate_remove_ui()
            case "patient_history":
                print(f"🔁 Changing language to: {new_lang}")
                self.translate_patient_history_ui()
                self.filter_results_by_date()
            case "preparation":
                self.translate_preparation_ui()
            case "reset":
                self.translate_reset_password_ui()
            case _:  # ברירת מחדל
                print(f"⚠️ Page '{page_name}' not recognized.")

    # region Translate Pages
    def translate_admin_ui(self):
        t = self.translator
        self.admin_ui.label_Admin_Page.setText(t.tr("admin_title"))
        self.admin_ui.AddButton.setText(t.tr("add_button"))
        self.admin_ui.RemoveButton.setText(t.tr("remove_button"))
        self.admin_ui.LogOffButton.setText(t.tr("logoff_button"))
        self.admin_ui.ReturnButton.setText(t.tr("return_button"))

    def translate_check_system_ui(self):
        t = self.translator
        self.check_ui.label_Check_System_Page.setText(t.tr("check_system_title"))
        self.check_ui.ExplorerButton.setText(t.tr("explorer_button"))
        self.check_ui.DiagnosticButton.setText(t.tr("diagnostic_button"))
        self.check_ui.LogOffButton.setText(t.tr("logoff_button"))
        self.check_ui.ReturnButton.setText(t.tr("return"))

    def translate_first_use_ui(self):
        t = self.translator
        self.first_use_ui.label_Register_New_Physiotherapist.setText(t.tr("first_use_title"))

        self.first_use_ui.ResetButton.setText(t.tr("reset_button"))
        self.first_use_ui.AddButton.setText(t.tr("add_admin_button"))

        self.first_use_ui.label_First_Name.setText(t.tr("first_name_label"))
        self.first_use_ui.label_Last_Name.setText(t.tr("last_name_label"))
        self.first_use_ui.label_Email.setText(t.tr("email_label"))
        self.first_use_ui.label_Username.setText(t.tr("username_label"))
        self.first_use_ui.label_Gender.setText(t.tr("gender_label"))
        self.first_use_ui.label_Date_Of_Birth.setText(t.tr("dob_label"))
        self.first_use_ui.label_Password.setText(t.tr("password_label"))
        self.first_use_ui.label_Password_Confirmation.setText(t.tr("password_confirm_label"))

        self.first_use_ui.comboBox_Gender.setItemText(0, t.tr("gender_male"))
        self.first_use_ui.comboBox_Gender.setItemText(1, t.tr("gender_female"))
        self.first_use_ui.comboBox_Gender.setItemText(2, t.tr("gender_other"))
        self.first_use_ui.comboBox_Gender.setCurrentIndex(-1)

        self.first_use_ui.error_Email.setText(t.tr("error_email"))
        self.first_use_ui.error_Username.setText(t.tr("error_username"))
        self.first_use_ui.error_First_Name.setText(t.tr("error_first_name"))
        self.first_use_ui.error_Last_Name.setText(t.tr("error_last_name"))
        self.first_use_ui.error_Password.setText(t.tr("error_password"))
        self.first_use_ui.error_Password_Confirmation.setText(t.tr("error_password_confirmation"))
        self.first_use_ui.error_Gender.setText(t.tr("error_gender"))

    def translate_login_ui(self):
        t = self.translator
        self.login_ui.label_LoginPage.setText(t.tr("login_title"))

        self.login_ui.label_Username.setText(t.tr("username_label"))
        self.login_ui.label_Password.setText(t.tr("password_label"))

        self.login_ui.LoginButton.setText(t.tr("login_button"))
        self.login_ui.FirstUseButton.setText(t.tr("first_use_button"))

        self.login_ui.label_Forgot_Password.setText(t.tr("forgot_password"))
        self.login_ui.label_goodbye_user.setText(t.tr("goodbye_user"))

        self.login_ui.error_Username_or_Password.setText(t.tr("error_invalid_login"))

    def translate_patient_history_ui(self):
        t = self.translator
        self.patient_hisory_ui.label_Patient_History_Page.setText(t.tr("patient_history_title"))

        headers = [
            "column_test_date", "column_fall_risk", "column_total_steps",
            "column_error_steps", "column_start_time", "column_end_time", "column_test_time"
        ]
        for i, key in enumerate(headers):
            self.patient_hisory_ui.tableWidget_History.horizontalHeaderItem(i).setText(t.tr(key))

        self.patient_hisory_ui.ExportToCSVButton.setText(t.tr("export_to_csv_button"))
        self.patient_hisory_ui.NewTestButton.setText(t.tr("new_test_button"))
        self.patient_hisory_ui.LogOffButton.setText(t.tr("logoff_button"))

        self.patient_hisory_ui.label_From_Date.setText(t.tr("from_date_label"))
        self.patient_hisory_ui.label_To_Date.setText(t.tr("to_date_label"))

        self.patient_hisory_ui.label_Gauge_Title.setText(t.tr("gauge_title"))

    def translate_preparation_ui(self):
        t = self.translator
        self.preparation_ui.label_Title.setText(t.tr("preparation_title_label"))
        self.preparation_ui.label_Instructions.setText(t.tr("preparation_instructions"))
        self.preparation_ui.StartTestButton.setText(t.tr("start_test_button"))

    def translate_register_ui(self):
        t = self.translator  # Translator instance
        self.register_ui.label_Register_New_Physiotherapist.setText(t.tr("register_title"))

        self.register_ui.label_Email.setText(t.tr("email_label"))
        self.register_ui.label_Username.setText(t.tr("username_label"))
        self.register_ui.label_Gender.setText(t.tr("gender_label"))
        self.register_ui.label_Date_Of_Birth.setText(t.tr("dob_label"))
        self.register_ui.label_First_Name.setText(t.tr("first_name_label"))
        self.register_ui.label_Last_Name.setText(t.tr("last_name_label"))
        self.register_ui.label_Password.setText(t.tr("password_label"))
        self.register_ui.label_Password_Confirmation.setText(t.tr("password_confirm_label"))
        self.register_ui.label_Is_Admin.setText(t.tr("is_admin_label"))

        self.register_ui.comboBox_Gender.setItemText(0, t.tr("gender_male"))
        self.register_ui.comboBox_Gender.setItemText(1, t.tr("gender_female"))
        self.register_ui.comboBox_Gender.setItemText(2, t.tr("gender_other"))
        self.register_ui.comboBox_Gender.setCurrentIndex(-1)

        self.register_ui.AddButton.setText(t.tr("add_button"))
        self.register_ui.LogOffButton.setText(t.tr("logoff_button"))
        self.register_ui.ReturnButton.setText(t.tr("return"))

        self.register_ui.error_Email.setText(t.tr("error_email"))
        self.register_ui.error_Username.setText(t.tr("error_username"))
        self.register_ui.error_Gender.setText(t.tr("error_gender"))
        self.register_ui.error_First_Name.setText(t.tr("error_first_name"))
        self.register_ui.error_Last_Name.setText(t.tr("error_last_name"))
        self.register_ui.error_Password.setText(t.tr("error_password"))
        self.register_ui.error_Password_Confirmation.setText(t.tr("error_password_confirmation"))

    def translate_remove_ui(self):
        t = self.translator
        self.remove_ui.label_Register_New_Physiotherapist.setText(t.tr("remove_title"))

        self.remove_ui.RemoveButton.setText(t.tr("remove_button"))
        self.remove_ui.ReturnButton.setText(t.tr("return"))
        self.remove_ui.LogOffButton.setText(t.tr("logoff_button"))

        headers = [
            "column_email", "column_username", "column_first_name",
            "column_last_name", "column_gender", "column_age", "column_is_admin"
        ]
        for i, key in enumerate(headers):
            self.remove_ui.tableWidget_Physiotherapists.horizontalHeaderItem(i).setText(t.tr(key))

    def translate_reset_password_ui(self):
        t = self.translator
        self.reset_ui.label_Title.setText(t.tr("reset_password_title"))

        self.reset_ui.label_Email.setText(t.tr("email_label"))
        self.reset_ui.label_Password.setText(t.tr("password_label"))
        self.reset_ui.label_Password_Confirmation.setText(t.tr("password_confirm_label"))

        self.reset_ui.ResetPasswordButton.setText(t.tr("reset_password_button"))

        self.reset_ui.error_Email.setText(t.tr("error_email"))
        self.reset_ui.error_Password.setText(t.tr("error_password"))
        self.reset_ui.error_Password_Confirmation.setText(t.tr("error_password_confirmation"))

    def translate_results_analysis_ui(self):
        t = self.translator
        self.results_ui.label_Result_Page.setText(t.tr("results_title"))

        self.results_ui.NewTestButton.setText(t.tr("new_test_button"))
        self.results_ui.HistoryResultsButton.setText(t.tr("history_results_button"))
        self.results_ui.LogOffButton.setText(t.tr("logoff_button"))

        self.results_ui.tableWidget_Results.horizontalHeaderItem(0).setText(t.tr("results_column_value"))
        rows = [
            "results_row_fall_risk",
            "results_row_test_time",
            "results_row_step_count",
            "results_row_error_steps"
        ]
        for i, key in enumerate(rows):
            self.results_ui.tableWidget_Results.verticalHeaderItem(i).setText(t.tr(key))

    def translate_test_parameters_ui(self):
        t = self.translator
        self.test_parameters_ui.label_Test_Parameters_Page.setText(t.tr("test_parameters_title"))

        self.test_parameters_ui.label_Patient_ID.setText(t.tr("patient_id_label"))
        self.test_parameters_ui.label_Gender.setText(t.tr("gender_label"))
        self.test_parameters_ui.label_Date_Of_Birth.setText(t.tr("dob_label"))
        self.test_parameters_ui.label_Shoe_Width.setText(t.tr("shoe_width_label"))
        self.test_parameters_ui.label_Pelvic_Width.setText(t.tr("pelvic_width_label"))
        self.test_parameters_ui.label_Has_Fallen.setText(t.tr("has_fallen_label"))
        self.test_parameters_ui.label_Notes.setText(t.tr("notes_label"))
        self.test_parameters_ui.DT_Notes.setText(t.tr("dt_notes_label"))

        self.test_parameters_ui.comboBox_Gender.setItemText(0, t.tr("gender_male"))
        self.test_parameters_ui.comboBox_Gender.setItemText(1, t.tr("gender_female"))
        self.test_parameters_ui.comboBox_Gender.setItemText(2, t.tr("gender_other"))
        self.test_parameters_ui.comboBox_Gender.setCurrentIndex(-1)

        self.test_parameters_ui.comboBox_Has_Fallen.setItemText(0, t.tr("fallen_yes"))
        self.test_parameters_ui.comboBox_Has_Fallen.setItemText(1, t.tr("fallen_no"))
        self.test_parameters_ui.comboBox_Has_Fallen.setCurrentIndex(-1)

        self.test_parameters_ui.ContinueButton.setText(t.tr("continue_button"))
        self.test_parameters_ui.AdminPageButton.setText(t.tr("admin_page_button"))
        self.test_parameters_ui.CheckSystemButton.setText(t.tr("check_system_button"))
        self.test_parameters_ui.LogOffButton.setText(t.tr("logoff_button"))
        self.test_parameters_ui.PatientHistoryButton.setText(t.tr("patient_history_button"))

        self.test_parameters_ui.error_Patient_Id.setText(t.tr("error_patient_id"))
        self.test_parameters_ui.error_Shoe_Width.setText(t.tr("error_shoe_width"))
        self.test_parameters_ui.error_Pelvic_Width.setText(t.tr("error_pelvic_width"))
        self.test_parameters_ui.error_Patient_Has_Fallen.setText(t.tr("error_has_fallen"))

    # endregion
    # endregion

