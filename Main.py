from PySide6.QtWidgets import QMainWindow, QApplication #, QMessageBox
# from PySide6.QtGui import QCursor
from PySide6.QtCore import QFile #, QTimer, QDate, Qt, QEvent
import sys
from Physiotherapist_Utils import Physiotherapist_Utils

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.utils = Physiotherapist_Utils(self)
        self.utils.load_login_page()


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
