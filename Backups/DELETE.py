class DELETE:
    #region NO NEED: gets the email from the user's username input
    def get_email(username):
        try:
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()

            # Check if the input is an email or username
            if '@' in username:
                cursor.execute("SELECT Email FROM PHYSIOTHERAPISTS WHERE Email = ?", (username,))
            else:
                cursor.execute("SELECT Email FROM PHYSIOTHERAPISTS WHERE Username = ?", (username,))

            result = cursor.fetchone()
            conn.close()

            if result:
                return result[0]  # We will return the email
            else:
                return None  # No match found

        except Exception as e:
            print("❌ DB error:", e)
            return None
    #endregion

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Enter, Qt.Key_Return):
            if self.default_enter_button:
                self.default_enter_button.click()






    # Displays the test results.
    def load_results_analysis_page(self):
        self.results_ui = Ui_ResultsAnalysisPage()
        self.results_ui.setupUi(self)
        self.setCentralWidget(self.results_ui.centralwidget)

        time_seconds = self.end_time - self.test_start_time
        fall_risk = self.calculate_fall_risk(time_seconds)

        # Saving a CSV file:
        if self.current_patient_id:
            save_test_result_to_csv(
                patient_id=self.current_patient_id,
                test_time_sec=time_seconds,
                risk_level=fall_risk,
                # test_notes=self.test_ui.textEdit_Notes.toPlainText()
            )

        icon = {"Low": "✅", "Moderate": "⚠️", "High": "❌"}.get(fall_risk, "❓")
        color = {"Low": "green", "Moderate": "orange", "High": "red"}.get(fall_risk, "black")

        self.results_ui.label_risk.setText(f"{icon} Fall Risk: {fall_risk}")
        self.results_ui.label_risk.setStyleSheet(f"color: {color}; font-size: 20pt; font-weight: bold;")
        self.results_ui.label_time.setText(f"🕒 Test Time: {time_seconds:.1f} sec")
        self.results_ui.label_time.setStyleSheet("font-size: 16pt;")

    # את הסיסמה ה"מאושרת" נקבל לאחר שימוש בתנאי שכתוב כאן
    # confirm_password = סיסמה מאושרת
    # if not self.is_strong_password(new_password):
    #     QMessageBox.warning(None, "Weak Password",
    #                         "Password must have at least 8 characters, upper/lowercase letters, a number, and a special character.")
    #     return False
    # משתמש מחובר משנה סיסמה
    def change_password(self, old_password: str, new_password: str, confirm_password: str) -> bool:
        # בדיקה בסיסית שהסיסמאות החדשות תואמות
        if new_password != confirm_password:
            QMessageBox.warning(None, "Mismatch", "New passwords do not match.")
            return False

        try:
            conn = odbc.connect(connection_string)
            cursor = conn.cursor()

            # שליפת הסיסמה המוצפנת הנוכחית
            cursor.execute("""
                SELECT Physio_Password
                FROM PHYSIOTHERAPISTS
                WHERE Email = ?
            """, (self.current_user["email"],))
            result = cursor.fetchone()

            if not result:
                QMessageBox.critical(None, "Error", "User not found.")
                conn.close()
                return False

            current_hashed_password = result[0]

            # בדיקת סיסמה ישנה
            if not self.check_password(old_password, current_hashed_password):
                QMessageBox.warning(None, "Wrong Password", "Old password is incorrect.")
                conn.close()
                return False

            # הצפנת הסיסמה החדשה
            new_hashed_password = self.hash_password(new_password)

            # עדכון בסיס הנתונים
            cursor.execute("""
                UPDATE PHYSIOTHERAPISTS
                SET Physio_Password = ?, Password_last_changed = ?
                WHERE Email = ?
            """, (new_hashed_password, datetime.now(), self.current_user["email"]))
            conn.commit()
            conn.close()

            QMessageBox.information(None, "Success", "Password changed successfully.")
            return True

        except Exception as e:
            print("❌ Error changing password:", e)
            return False

    # אם עברו יותר מ-90 ימים ← לדרוש שינוי סיסמה
    def is_password_expired(self) -> bool:
        if not self.current_user.get("password_last_changed"):
            return True  # אם לא מוגדר – נדרוש שינוי

        days_since_change = (datetime.now() - self.current_user["password_last_changed"]).days
        return days_since_change > 90

    # בודק האם סיסמה עומדת בכללים
    import re
    def is_strong_password(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"\d", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True
    # 📋 החוקים:
    # לפחות 8 תווים
    # לפחות אות גדולה
    # לפחות אות קטנה
    # לפחות מספר
    # לפחות תו מיוחד

    ######################################################
    # Loads the TestParametersPage page and if an ID was entered - immediately reads the data.
    def load_test_parameters1(self, patient_id=None):
        self.test_ui = Ui_TestParameters()
        self.test_ui.setupUi(self, controller=self)
        self.test_ui.pushButton_Admin_Page.setVisible(self.is_admin)
        self.setCentralWidget(self.test_ui.centralwidget)
        self.set_default_enter_button(self.test_ui.pushButton_Start_Test)
        self.test_ui.dateEdit_Date_Of_Birth.setDate(QDate.currentDate())

        self.test_ui.lineEdit_Patient_ID.textChanged.connect(self.restart_autofill_timer)
        self.test_ui.pushButton_Start_Test.clicked.connect(self.on_start_test_clicked)
        self.test_ui.pushButton_Admin_Page.clicked.connect(self.load_admin_page)
        self.test_ui.pushButton_Log_Off.clicked.connect(self.log_off)

        if self.current_user:
            first_name = get_first_name_from_username(self.current_user)
            if first_name:
                self.test_ui.label_welcome_user.setText(f"Welcome, {first_name}")

        if patient_id:
            self.test_ui.lineEdit_Patient_ID.setText(str(patient_id))
            self.autofill_patient_data()

    def load_first_use_page1(self):
        self.first_use_ui = Ui_FirstUsePage()
        self.first_use_ui.setupUi(self)
        self.setCentralWidget(self.first_use_ui.centralwidget)
        self.first_use_ui.pushButton_Add_New_Physiotherapist.clicked.connect(self.load_admin_page)
        self.first_use_ui.pushButton_Reset.clicked.connect(self.log_off)

    def load_admin_page1(self):
        self.admin_ui = Ui_AdminPage()
        self.admin_ui.setupUi(self, controller=self)
        self.setCentralWidget(self.admin_ui.centralwidget)
        self.admin_ui.pushButton.clicked.connect(self.load_register_page)
        self.admin_ui.pushButton_2.clicked.connect(self.load_remove_page)
        self.admin_ui.pushButton_Log_Off.clicked.connect(self.log_off)
        self.admin_ui.pushButton_Return_To_Test_Parameters_Page.clicked.connect(self.load_test_parameters)

    def load_register_page1(self):
        self.register_ui = Ui_Register_New_Physiotherapist()
        self.register_ui.setupUi(self, controller=self)
        self.setCentralWidget(self.register_ui.centralwidget)
        self.register_ui.pushButton_Return_To_Admin_Page.clicked.connect(self.load_admin_page)
        self.register_ui.pushButton_Log_Off.clicked.connect(self.log_off)

    def load_remove_page1(self):
        self.remove_ui = Ui_Remove_Existing_Physiotherapists()
        self.remove_ui.setupUi(self, controller=self)
        self.setCentralWidget(self.remove_ui.centralwidget)
        self.remove_ui.pushButton_Return_To_Admin_Page.clicked.connect(self.load_admin_page)
        self.remove_ui.pushButton_Log_Off.clicked.connect(self.log_off)

    def return_to_admin1(self):
        if self.controller and hasattr(self.controller, "load_admin_page"):
            self.controller.load_admin_page()

    # Reads the username and password from the UI and if correct: loads the parameter entry page.
    def load_test_parameters_page1(self):
        username = self.lineEdit_Username.text()
        password = self.lineEdit_Password.text()
        is_valid, is_admin = validate_login(username, password)
        if is_valid:
            self.test_ui = Ui_TestParameters()
            self.test_ui.setupUi(self.parent_window, controller=get_email(username), is_admin=bool(is_admin))
        else:
            self.error_Password.setText("Incorrect username or password")
            self.error_Password.show()

    def load_first_use_page1(self):
        self.first_use_ui = Ui_FirstUsePage()
        self.first_use_ui.setupUi(self.parent_window)
    ######################################################
