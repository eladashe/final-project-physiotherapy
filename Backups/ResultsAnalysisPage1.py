from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QFrame
from PySide6.QtCore import Qt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, controller=None):
        self.controller = controller
        MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 250)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # יצירת מסגרת יפה
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color: #f4f4f4; border-radius: 15px; padding: 20px;")
        self.frame_layout = QVBoxLayout(self.frame)

        # תווית רמת סיכון
        self.label_risk = QLabel("Fall Risk: ")
        self.label_risk.setAlignment(Qt.AlignCenter)
        self.label_risk.setStyleSheet("font-size: 20pt; font-weight: bold;")
        self.frame_layout.addWidget(self.label_risk)

        # תווית זמן בדיקה
        self.label_time = QLabel("Test Time: ")
        self.label_time.setAlignment(Qt.AlignCenter)
        self.label_time.setStyleSheet("font-size: 16pt;")
        self.frame_layout.addWidget(self.label_time)

        # לייאאוט ראשי
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Results Analysis")
