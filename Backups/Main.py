from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QCursor
from PySide6.QtCore import QTimer, QDate, QFile, Qt, QEvent
import sys
from Physiotherapist_Utils import Physiotherapist_Utils

#region JSON
# # From here - connection to json file in order to translate
# import json
#
# with open("translations/en.json", encoding="utf-8") as f:
#     translations = json.load(f)
#
# def tr(key):
#     return translations.get(key, f"[{key}]")
# # Till here - json file
#endregion

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.utils = Physiotherapist_Utils(self)
        self.is_admin = False
        self.current_user = None
        self.default_enter_button = None  # Button that will be clicked if Enter is pressed
        self.param_days_back = 0
        self.current_patient_id = None
        self.utils.load_login_page()

    # region OTHERS
        # self.login_ui = Ui_LoginPage() # Loading the login screen.
        # self.login_ui.setupUi(self) # Allows the login screen to access the main class and run functions from within it.
        # self.login_ui.LoginButton.clicked.connect(self.print_login_info) # Binds the login button to the print_login_info function.
        # self.setCentralWidget(self.login_ui.centralwidget)
        # self.set_default_enter_button(self.login_ui.LoginButton)

        # self.autofill_timer = QTimer()
        # self.autofill_timer.setSingleShot(True)
        # self.autofill_timer.timeout.connect(self.autofill_patient_data)
        #
        #
        # self.inactivity_timer = QTimer()
        # self.session_time = 20
        # self.inactivity_timer.setInterval(self.session_time * 60 * 1000)
        # # self.inactivity_timer.setInterval(5 * 1000)
        # self.inactivity_timer.setSingleShot(True)
        # self.inactivity_timer.timeout.connect(self.show_inactivity_warning)
        # self.logout_timer = QTimer()
        # self.logout_timer.setInterval(60 * 1000)
        # self.logout_timer.setSingleShot(True)
        # self.logout_timer.timeout.connect(self.handle_inactivity_logout)
        #
        # QApplication.instance().installEventFilter(self)
        # self.inactivity_timer.start()


    # def set_default_enter_button(self, button):
    #     self.default_enter_button = button
    #endregion

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # QSS loading phase
    file = QFile("QSS/SpyBot.qss")
    #region BETTER OPTIONS
    # file = QFile("QSS/Adaptic.qss")
    # file = QFile("QSS/Combinear.qss")
    # file = QFile("QSS/Irrorater.qss")
    # file = QFile("QSS/Obit.qss")
    # file = QFile("QSS/style.qss")
    # file = QFile("QSS/Toolery.qss")
    #endregion

    #region NOT SO GOOD
    # file = QFile("QSS/Darkeum.qss")
    # file = QFile("QSS/DeepBox.qss")
    # file = QFile("QSS/Diffnes.qss")
    # file = QFile("QSS/Gravira.qss")
    # file = QFile("QSS/Incrypt.qss")
    # file = QFile("QSS/Integrid.qss")
    # file = QFile("QSS/Medize.qss")
    # file = QFile("QSS/SyNet.qss")
    # file = QFile("QSS/Wstartpage.qss")
    # endregion

    if file.open(QFile.ReadOnly | QFile.Text):
        style_sheet = file.readAll().data().decode("utf-8")
        app.setStyleSheet(style_sheet)

    window = MainApp()
    window.show()
    sys.exit(app.exec())
