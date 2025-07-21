from PySide6.QtWidgets import QSizePolicy, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QDateEdit, QTextEdit, QFormLayout, QMainWindow, QCheckBox
from PySide6.QtCore import Qt
import json, os

class LanguageManager:
    # region shifting
    def shift_login(self, language, login_ui):
        if language == "en":
            self.set_english(login_ui)
        else:
            self.set_hebrew_login_X(login_ui)

    def shift_first_use(self, language, first_use_ui):
        if language == "en":
            self.set_english(first_use_ui)
        else:
            self.set_hebrew_comboBoxLanguage_X(first_use_ui, "FirstUsePage")
            self.set_hebrew_first_use_X(first_use_ui)

    def shift_admin(self, language, admin_ui):
        if language == "en":
            self.set_english(admin_ui)
        else:
            self.set_hebrew_comboBoxLanguage_X(admin_ui, "AdminPage")

    def shift_check_system(self, language, check_system_ui):
        if language == "en":
            self.set_english(check_system_ui)
        else:
            self.set_hebrew_comboBoxLanguage_X(check_system_ui, "CheckSystemPage")

    def shift_patient_hisory(self, language, patient_hisory_ui):
        if language == "en":
            self.set_english(patient_hisory_ui)
        else:
            self.set_hebrew_comboBoxLanguage_X(patient_hisory_ui, "PatientHistoryPage")

    def shift_preparation(self, language, preparation_ui):
        if language == "en":
            self.set_english(preparation_ui)
        else:
            self.set_hebrew_comboBoxLanguage_X(preparation_ui, "PreparationPage")

    def shift_register(self, language, register_ui):
        if language == "en":
            self.set_english(register_ui)
        else:
            self.set_hebrew_register_new_physiotherapist_X(register_ui)
            self.set_hebrew_comboBoxLanguage_X(register_ui, "RegisterNewPhysiotherapist")

    def shift_remove(self, language, remove_ui):
        if language == "en":
            self.set_english(remove_ui)
        else:
            self.set_hebrew_comboBoxLanguage_X(remove_ui, "RemoveExistingPhysiotherapists")

    def shift_reset(self, language, reset_ui):
        if language == "en":
            self.set_english(reset_ui)
        else:
            self.set_hebrew_reset_password_X(reset_ui)
            self.set_hebrew_comboBoxLanguage_X(reset_ui, "ResetPasswordPage")

    def shift_result(self, language, result_ui):
        if language == "en":
            self.set_english(result_ui)
        else:
            self.set_hebrew_comboBoxLanguage_X(result_ui, "ResultsAnalysisPage")

    def shift_test_parameters(self, language, test_parameters_ui):
        if language == "en":
            self.set_english(test_parameters_ui)
        else:
            self.set_hebrew_comboBoxLanguage_X(test_parameters_ui, "TestParametersPage")
            self.set_hebrew_test_parameters_X(test_parameters_ui)
    # endregion

    def apply_x_positions(self, widget_dict: dict):
        for widget, new_x in widget_dict.items():
            old_geometry = widget.geometry()
            widget.setGeometry(new_x, old_geometry.y(), old_geometry.width(), old_geometry.height())

    # region Hebrew
    def set_hebrew_comboBoxLanguage_X(self, ui, file_name):
        width = self.load_width_from_json("Positions/" + file_name +".json", "window_width", "window")
        comboBoxLanguage_X = self.load_width_from_json("Positions/" + file_name +".json", "comboBoxLanguage", "widgets_X")
        comboBoxLanguage_Width = self.load_width_from_json("Positions/" + file_name +".json", "comboBoxLanguage", "widgets_Width")
        hebrew_X = {
            ui.comboBoxLanguage: width - comboBoxLanguage_X - comboBoxLanguage_Width
        }
        self.apply_x_positions(hebrew_X)

    def set_hebrew_first_use_X(self, ui):
        width = self.load_width_from_json("Positions/FirstUsePage.json", "window_width", "window")
        label_lineEdit_X = self.load_width_from_json("Positions/FirstUsePage.json", "label_Email", "widgets_X")
        label_lineEdit_Width = self.load_width_from_json("Positions/FirstUsePage.json", "lineEdit_Email", "widgets_Width")
        label_error_Width = self.load_width_from_json("Positions/FirstUsePage.json", "error_Email", "widgets_Width")
        label_error_X = label_lineEdit_X + label_lineEdit_Width - label_error_Width
        ResetButton_X = self.load_width_from_json("Positions/FirstUsePage.json", "ResetButton","widgets_X")
        ResetButton_Width = self.load_width_from_json("Positions/FirstUsePage.json", "ResetButton","widgets_Width")
        hebrew_X = {
            ui.ResetButton: width - ResetButton_X - ResetButton_Width,
            ui.lineEdit_Email: label_lineEdit_X,
            ui.lineEdit_Username: label_lineEdit_X,
            ui.comboBox_Gender: label_lineEdit_X,
            ui.dateEdit_Date_Of_Birth: label_lineEdit_X,
            ui.lineEdit_First_Name: label_lineEdit_X,
            ui.lineEdit_Last_Name: label_lineEdit_X,
            ui.lineEdit_Password: label_lineEdit_X,
            ui.lineEdit_Password_Confirmation: label_lineEdit_X,
            ui.error_Email: label_error_X,
            ui.error_Username: label_error_X,
            ui.error_Gender: label_error_X,
            ui.error_First_Name: label_error_X,
            ui.error_Last_Name: label_error_X,
            ui.error_Password: label_error_X,
            ui.error_Password_Confirmation: label_error_X
        }
        self.apply_x_positions(hebrew_X)

    def set_hebrew_login_X(self, ui):
        line_edit_x = self.load_width_from_json("Positions/LoginPage.json", "lineEdit_Username", "widgets_X")
        line_edit_width = self.load_width_from_json("Positions/LoginPage.json", "lineEdit_Username", "widgets_Width")
        label_error_width = self.load_width_from_json("Positions/LoginPage.json", "error_Username_or_Password", "widgets_Width")
        hebrew_X = {
            ui.label_goodbye_user: self.load_width_from_json("Positions/LoginPage.json", "label_LoginPage", "widgets_X"),
            ui.error_Username_or_Password: line_edit_x + line_edit_width - label_error_width
        }
        self.apply_x_positions(hebrew_X)

    def set_hebrew_register_new_physiotherapist_X(self, ui):
        label_lineEdit_X = self.load_width_from_json("Positions/RegisterNewPhysiotherapist.json", "label_Email", "widgets_X")
        label_lineEdit_Width = self.load_width_from_json("Positions/RegisterNewPhysiotherapist.json", "lineEdit_Email","widgets_Width")
        label_checkBox_Width = self.load_width_from_json("Positions/RegisterNewPhysiotherapist.json", "checkBox_Is_Admin","widgets_Width")
        label_error_Width = self.load_width_from_json("Positions/RegisterNewPhysiotherapist.json", "error_Email", "widgets_Width")
        label_error_X = label_lineEdit_X + label_lineEdit_Width - label_error_Width
        checkBox_X = label_lineEdit_X + label_lineEdit_Width - label_checkBox_Width
        hebrew_X = {
            ui.lineEdit_Email: label_lineEdit_X,
            ui.lineEdit_Username: label_lineEdit_X,
            ui.comboBox_Gender: label_lineEdit_X,
            ui.dateEdit_Date_Of_Birth: label_lineEdit_X,
            ui.lineEdit_First_Name: label_lineEdit_X,
            ui.lineEdit_Last_Name: label_lineEdit_X,
            ui.lineEdit_Password: label_lineEdit_X,
            ui.lineEdit_Password_Confirmation: label_lineEdit_X,
            ui.checkBox_Is_Admin: checkBox_X,
            ui.error_Email: label_error_X,
            ui.error_Username: label_error_X,
            ui.error_Gender: label_error_X,
            ui.error_First_Name: label_error_X,
            ui.error_Last_Name: label_error_X,
            ui.error_Password: label_error_X,
            ui.error_Password_Confirmation: label_error_X
        }
        self.apply_x_positions(hebrew_X)

    def set_hebrew_reset_password_X(self, ui):
        label_lineEdit_error_X = self.load_width_from_json("Positions/ResetPasswordPage.json", "label_Email","widgets_X")
        hebrew_X = {
            ui.lineEdit_Email: label_lineEdit_error_X,
            ui.lineEdit_Password: label_lineEdit_error_X,
            ui.lineEdit_Password_Confirmation: label_lineEdit_error_X,
            ui.error_Email: label_lineEdit_error_X,
            ui.error_Password: label_lineEdit_error_X,
            ui.error_Password_Confirmation: label_lineEdit_error_X
        }
        self.apply_x_positions(hebrew_X)

    def set_hebrew_test_parameters_X(self, ui):
        label_X = self.load_width_from_json("Positions/TestParametersPage.json", "label_Patient_ID", "widgets_X")
        label_lineEdit_X = self.load_width_from_json("Positions/TestParametersPage.json", "lineEdit_Patient_ID","widgets_X")
        label_lineEdit_Width = self.load_width_from_json("Positions/TestParametersPage.json", "lineEdit_Patient_ID","widgets_Width")
        label_error_Width = self.load_width_from_json("Positions/TestParametersPage.json", "error_Patient_Id", "widgets_Width")
        label_error_X = label_lineEdit_X + label_lineEdit_Width - label_error_Width
        hebrew_X = {
            ui.label_welcome_user: label_X,
            ui.PatientHistoryButton: label_X - 40,
            ui.DT_Notes: label_X,
            ui.error_Patient_Id: label_error_X,
            ui.error_Gender: label_error_X,
            ui.error_Shoe_Width: label_error_X,
            ui.error_Pelvic_Width: label_error_X,
            ui.error_Patient_Has_Fallen: label_error_X
        }
        self.apply_x_positions(hebrew_X)
    # endregion

    def load_positions_from_json(self, ui_name: str) -> dict:
        file_path = os.path.join("Positions", f"{ui_name}.json")
        if not os.path.exists(file_path):
            print(f"⚠️ JSON file not found for {ui_name}")
            return {}
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def apply_positions_from_json(self, ui, position_dict: dict):
        widgets_x = position_dict.get("widgets_X", {})
        for name, x in widgets_x.items():
            widget = ui.centralwidget.findChild(QWidget, name)
            if widget:
                g = widget.geometry()
                widget.setGeometry(x, g.y(), g.width(), g.height())

    def set_english(self, ui):
        ui_name = ui.__class__.__name__.replace("Ui_", "")
        position_dict = self.load_positions_from_json(ui_name)
        self.apply_positions_from_json(ui, position_dict)

        # Identifiers of labels that should not change
        center_aligned_labels = {"label_Gauge_Title", "label_Gauge_Percentage"}

        for widget in ui.centralwidget.findChildren(QWidget):
            if isinstance(widget, (QLabel, QLineEdit, QTextEdit)):
                if widget.objectName() not in center_aligned_labels:
                    widget.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                widget.setLayoutDirection(Qt.LeftToRight)

            elif isinstance(widget, (QComboBox, QDateEdit, QPushButton)):
                widget.setLayoutDirection(Qt.LeftToRight)

    def save_widget_positions_to_json(self, ui_class, json_path: str):
        window = QMainWindow()
        ui = ui_class()
        ui.setupUi(window)
        window.show()

        widget_types = (QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, QDateEdit, QCheckBox)
        widgets = ui.centralwidget.findChildren(QWidget)

        positions_dict = {
            "widgets_X": {
                w.objectName(): w.geometry().x()
                for w in widgets
                if isinstance(w, widget_types) and w.objectName()
            },
            "widgets_Width": {
                w.objectName(): w.geometry().width()
                for w in widgets
                if isinstance(w, widget_types) and w.objectName()
            },
            "window": {
                "window_width": window.width()
            }
        }

        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(positions_dict, f, ensure_ascii=False, indent=4)

        # print(f"✅ Saved widget positions and widths to: {json_path}")

    def load_width_from_json(self, json_path: str, widget: str, section: str) -> int:
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # If it is the width of the window
            if section == "window":
                return data.get("window", {}).get("window_width", 0)

            # Access the correct area (widgets_Width or widgets_X)
            section_data = data.get(section, {})
            value = section_data.get(widget, None)

            if value is None:
                print(f"⚠️ Widget '{widget}' not found in section '{section}' of {json_path}")
                return 0

            return value

        except FileNotFoundError:
            print(f"❌ File not found: {json_path}")
            return 0
        except Exception as e:
            print(f"❌ Error reading JSON: {e}")
            return 0

