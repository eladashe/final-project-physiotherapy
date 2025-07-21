from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from urllib.parse import quote_plus
import pandas as pd

# Elad
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'ELAD-COMPUTER\\SQLEXPRESS'
DATABASE_NAME = 'DB_Final_Project'

# Amir
# DRIVER_NAME = 'ODBC Driver 11 for SQL Server'
# # DRIVER_NAME = 'ODBC Driver 13 for SQL Server'
# SERVER_NAME = 'DESKTOP-DROOU2D\\SQLEXPRESS'
# DATABASE_NAME = 'Test_Elad'

params = quote_plus(
    f"DRIVER={DRIVER_NAME};"
    f"SERVER={SERVER_NAME};"
    f"DATABASE={DATABASE_NAME};"
    f"Trusted_Connection=yes;"
)
engine: Engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# Queries the PATIENTS table by ID and returns gender and date of birth.
def get_patient_info(patient_id):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT Gender, Date_Of_Birth FROM PATIENTS WHERE Patient_ID = :pid
            """), {'pid': patient_id}).fetchone()
            return {"gender": result[0], "dob": result[1]} if result else None

    except Exception as e:
        print("❌ Error fetching patient info:", e)
        return None

# Returns a dictionary with parameter names and values
def get_recent_parameters(patient_id, days):
    try:
        with engine.connect() as conn:
            rows = conn.execute(text("""
                SELECT TP.Parameter_Name, PP.Param_Value
                FROM PATIENTPARAMETER AS PP JOIN TOTALPARAMETERS AS TP ON PP.Param_ID = TP.Parameter_ID
                WHERE PP.Patient_ID = :pid
                AND PP.Updated_At >= DATEADD(DAY, -:days, CAST(GETDATE() AS DATE))
            """), {'pid': patient_id, 'days': days}).fetchall()
            return {name: value for name, value in rows} if rows else None
    except Exception as e:
        print("❌ Error fetching parameters:", e)
        return None

# Checks if there is a test history for the patient in the database
def has_patient_test_history(patient_id: str) -> bool:
    if not patient_id or not patient_id.isdigit():
        return False
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT COUNT(*) FROM TESTS WHERE patient_ID = :pid
            """), {'pid': patient_id}).scalar()
            return result > 0
    except Exception as e:
        print("❌ Error checking test history:", e)
        return False

# Fetches the Valid_Range string for a given parameter ID from TOTALPARAMETERS
def get_valid_range(param_id):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT Valid_Range FROM TOTALPARAMETERS WHERE Parameter_ID = :pid
            """), {'pid': param_id}).scalar()
            return result
    except Exception as e:
        print("❌ Error fetching Valid_Range:", e)
        return None

# Parses a 'min-max' range string into float values
def parse_range(range_str):
    try:
        min_val, max_val = map(float, range_str.strip().split('-'))
        return min_val, max_val
    except:
        return None, None

# region Saving results and analysis
# Adds a new test to the TESTS table, including a connection to PHYSIOTHERAPISTS via the physiotherapist's email, and returns the Test_ID
def insert_new_test(physiotherapist_email, patient_id, start_time, end_time, test_status, notes=None,
                    error_code=None, error_description=None):
    try:
        with engine.begin() as conn:
            # שליפת ה-ID של הפיזיותרפיסט
            physio_result = conn.execute(text("""
                    SELECT Physiotherapist_ID FROM PHYSIOTHERAPISTS WHERE Email = :email
                """), {'email': physiotherapist_email}).fetchone()

            if not physio_result:
                print("❌ Physiotherapist not found for email:", physiotherapist_email)
                return None

            physiotherapist_id = physio_result[0]

            # הכנסת מבחן והחזרת ה-ID שנוצר באמצעות OUTPUT
            result = conn.execute(text("""
                    INSERT INTO TESTS (
                        Physiotherapist_ID, patient_ID, Start_Time, End_Time, Test_Status, Notes, Error_Type, Error_Description_Patient
                    )
                    OUTPUT INSERTED.Test_ID
                    VALUES (
                        :physio_id, :pid, :start, :end, :status, :notes, :error_code, :error_desc
                    )
                """), {
                'physio_id': physiotherapist_id,
                'pid': patient_id,
                'start': start_time,
                'end': end_time,
                'status': test_status,
                'notes': notes,
                'error_code': error_code,
                'error_desc': error_description
            })

            inserted_id = result.scalar()
            return inserted_id

    except Exception as e:
        print("❌ Failed to insert test:", e)
        return None

def get_last_note(patient_id):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT TOP 1 Notes, CAST(Start_Time AS DATE) AS Start_Date
                FROM TESTS
                WHERE Patient_ID = :pid AND Notes IS NOT NULL AND LTRIM(RTRIM(Notes)) != ''
                ORDER BY Start_Time DESC
            """), {'pid': patient_id}).fetchone()
            return result if result else (None, None)
    except Exception as e:
        print("❌ Error fetching last note:", e)
        return (None, None)

# Adds data to RESULTS, RESULTSPARAMETER, PATIENTPARAMETER for the test
def save_test_results(test_id, patient_id, fall_risk_prob, real_steps_count, real_wrong_steps,
                      pelvic_width, shoe_width, has_fall_last_year):
    try:
        with engine.begin() as conn:
            conn.execute(text("""
                    INSERT INTO RESULTS (Test_ID, Analysis_Timestamp)
                    VALUES (:tid, GETDATE())
                """), {'tid': test_id})

            result_params = [
                {'tid': test_id, 'pid': 1, 'val': str(round(fall_risk_prob, 4))},
                {'tid': test_id, 'pid': 2, 'val': str(real_steps_count)},
                {'tid': test_id, 'pid': 3, 'val': str(real_wrong_steps)}
            ]
            for p in result_params:
                conn.execute(text("""
                        INSERT INTO RESULTSPARAMETER (Test_ID, Param_ID, Param_Value)
                        VALUES (:tid, :pid, :val)
                    """), p)

            patient_params = [
                {'pid': patient_id, 'param_id': 4, 'val': str(pelvic_width)},
                {'pid': patient_id, 'param_id': 5, 'val': str(shoe_width)},
                {'pid': patient_id, 'param_id': 6, 'val': str(has_fall_last_year)}
            ]
            for p in patient_params:
                conn.execute(text("""
                        INSERT INTO PATIENTPARAMETER (Patient_ID, Param_ID, Param_Value)
                        VALUES (:pid, :param_id, :val)
                    """), p)

    except Exception as e:
        print("❌ Error while saving test results:", e)

# Check if there are active physical therapists
def get_latest_patient_note(patient_id):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                    SELECT TOP 1 Notes, Start_Time
                    FROM TESTS
                    WHERE Patient_ID = :pid AND Notes IS NOT NULL AND LTRIM(RTRIM(Notes)) != ''
                    ORDER BY Start_Time DESC
                """), {'pid': patient_id}).fetchone()
            return result if result else None
    except Exception as e:
        print("❌ Error fetching latest note:", e)
        return None

# Check if there is at least one physiotherapist in the table
def has_physiotherapists():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                    SELECT CASE WHEN EXISTS (SELECT 1 FROM PHYSIOTHERAPISTS) THEN 1 ELSE 0 END
                """)).scalar()
            return result == 1
    except Exception as e:
        print("❌ Error in has_physiotherapists:", e)
        return False

# Retrieve physiotherapist login data by email or username.
# Returns tuple: (Email, First_Name, Password_Hash, Password_Last_Changed, Is_Admin)
def get_login_data(username):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                    SELECT Email, First_Name, Physio_Password, Password_last_changed, Is_Admin
                    FROM PHYSIOTHERAPISTS 
                    WHERE Email = :user OR Username = :user
                """), {'user': username}).fetchone()
            return result
    except Exception as e:
        print("❌ Error in get_login_data:", e)
        return None

# Check if an active physiotherapist exists by email
def get_existing_physiotherapist_by_email(email):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                    SELECT COUNT(*) FROM PHYSIOTHERAPISTS 
                    WHERE Email = :email AND Is_Active = 1
                """), {'email': email}).scalar()
            return result if result else 0
    except Exception as e:
        print("❌ Error in get_existing_user_by_email:", e)
        return 0

# Get details of a previously registered but inactive physiotherapist.
# Returns: (Username, First_Name, Last_Name, Gender, Date_Of_Birth)
def get_inactive_physiotherapist_details(email):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                    SELECT Username, First_Name, Last_Name, Gender, Date_Of_Birth
                    FROM PHYSIOTHERAPISTS 
                    WHERE Email = :email AND Is_Active = 0
                """), {'email': email}).fetchone()
            return result
    except Exception as e:
        print("❌ Error in get_inactive_user_details:", e)
        return None

# Update password and timestamp for an active physiotherapist
def reset_password(email, hashed_password):
    try:
        with engine.begin() as conn:
            conn.execute(text("""
                    UPDATE PHYSIOTHERAPISTS
                    SET Physio_Password = :pw, Password_last_changed = GETDATE()
                    WHERE Email = :email AND Is_Active = 1
                """), {'pw': hashed_password, 'email': email})
        return True
    except Exception as e:
        print("❌ Error in reset_password:", e)
        return False

# Return a list of physiotherapists that start with the given base
def get_existing_physiotherapists(base):
    try:
        with engine.connect() as conn:
            rows = conn.execute(text("""
                    SELECT Username FROM PHYSIOTHERAPISTS 
                    WHERE Username LIKE :pattern
                """), {'pattern': f"{base}%"}).fetchall()
            return [row[0] for row in rows if row[0] is not None]
    except Exception as e:
        print("❌ Error in get_existing_physiotherapists:", e)
        return []

# Insert a new physiotherapist into the database
def insert_physiotherapist(email, username, first_name, last_name, gender, dob, hashed_password, is_admin):
    try:
        with engine.begin() as conn:
            conn.execute(text("""
                    INSERT INTO PHYSIOTHERAPISTS 
                    (Email, Username, First_Name, Last_Name, Gender, Date_Of_Birth, Is_Admin, Physio_Password, Password_last_changed, Is_Active, Is_Active_From)
                    VALUES (:email, :username, :fname, :lname, :gender, :dob, :is_admin, :pw, GETDATE(), 1, GETDATE())
                """), {
                'email': email,
                'username': username,
                'fname': first_name,
                'lname': last_name,
                'gender': gender,
                'dob': dob,
                'is_admin': int(is_admin),
                'pw': hashed_password
            })
        return True
    except Exception as e:
        print("❌ Error in insert_physiotherapist:", e)
        return False

# Soft-delete the most recent active record of a physiotherapist
def soft_delete_physio(email):
    try:
        with engine.begin() as conn:
            conn.execute(text("""
                    UPDATE PHYSIOTHERAPISTS
                    SET Is_Active = 0, Is_Active_Until = GETDATE()
                    WHERE Physiotherapist_ID = (
                        SELECT TOP 1 Physiotherapist_ID
                        FROM PHYSIOTHERAPISTS
                        WHERE Email = :email AND Is_Active = 1
                        ORDER BY Is_Active_From DESC
                    )
                """), {'email': email})
        return True
    except Exception as e:
        print("❌ Error in soft_delete_physio:", e)
        return False

# Get list of all active physiotherapists, excluding the one with the provided email.
# Returns: list of tuples
def get_all_physios_except(email):
    try:
        with engine.connect() as conn:
            rows = conn.execute(text("""
                    SELECT Email, Username, First_Name, Last_Name, Gender,
                           DATEDIFF(YEAR, Date_Of_Birth, GETDATE()) - 
                           CASE WHEN DATEADD(YEAR, DATEDIFF(YEAR, Date_Of_Birth, GETDATE()), Date_Of_Birth) > GETDATE()
                                THEN 1 ELSE 0 END AS Age,
                           Is_Admin
                    FROM PHYSIOTHERAPISTS
                    WHERE Email != :email AND Is_Active = 1
                """), {'email': email}).fetchall()
            return rows
    except Exception as e:
        print("❌ Error in get_all_physios_except:", e)
        return []

# Insert a patient into the PATIENTS table only if they don't already exist
def create_patient_if_needed(patient_id, gender, dob):
    try:
        with engine.begin() as conn:
            exists = conn.execute(text("""
                    SELECT COUNT(*) FROM PATIENTS WHERE Patient_ID = :pid
                """), {'pid': patient_id}).scalar()
            if exists == 0:
                conn.execute(text("""
                        INSERT INTO PATIENTS (Patient_ID, Gender, Date_Of_Birth)
                        VALUES (:pid, :gender, :dob)
                    """), {'pid': patient_id, 'gender': gender, 'dob': dob})
        return True
    except Exception as e:
        print("❌ Error in create_patient_if_needed:", e)
        return False

# Delete all data from non-lookup tables
def reset_main_tables():
    try:
        with engine.begin() as conn:
            for table in ["RESULTSPARAMETER", "RESULTS", "TESTS", "PATIENTPARAMETER", "PATIENTS", "PHYSIOTHERAPISTS"]:
                conn.execute(text(f"DELETE FROM {table}"))
        return True
    except Exception as e:
        print("❌ Error in reset_main_tables:", e)
        return False

# Get test history data (aggregated) for a patient between two dates
def get_history_by_date_range(patient_id, start_date, end_date):
    try:
        with engine.connect() as conn:
            query = text("""
                    SELECT
                        CAST(T.Start_Time AS DATE) AS [Test Date],
                        ISNULL(FORMAT(CAST(MAX(CASE WHEN RP.Param_ID = 1 THEN RP.Param_Value END) AS FLOAT) * 100, 'N1') + '%', 'N/A') AS [Fall Risk (%)],
                        ISNULL(MAX(CASE WHEN RP.Param_ID = 2 THEN RP.Param_Value END), '0') AS [Step Count],
                        ISNULL(MAX(CASE WHEN RP.Param_ID = 3 THEN RP.Param_Value END), '0') AS [Error Steps],
                        ISNULL(CONVERT(VARCHAR(8), T.Start_Time, 108), '') AS [Start Time],
                        ISNULL(CONVERT(VARCHAR(8), T.End_Time, 108), '') AS [End Time],
                        ISNULL(DATEDIFF(SECOND, T.Start_Time, T.End_Time), 0) AS [Test Time (sec)]
                    FROM PATIENTS AS P
                    JOIN TESTS AS T ON P.Patient_ID = T.Patient_ID
                    JOIN RESULTS AS R ON T.Test_ID = R.Test_ID
                    JOIN RESULTSPARAMETER AS RP ON R.Test_ID = RP.Test_ID
                    WHERE 
                        T.Patient_ID = :pid
                        AND CAST(T.Start_Time AS DATE) BETWEEN :start AND :end
                    GROUP BY T.Test_ID, T.Start_Time, T.End_Time
                    ORDER BY [Test Date] DESC, [Start Time] DESC

                """)
            results = conn.execute(query, {'pid': patient_id, 'start': start_date, 'end': end_date}).fetchall()
            return results
    except Exception as e:
        print("❌ Error in get_history_by_date_range:", e)
        return []

# Get latest test data for a patient (used for the KPI gauge)
def get_latest_test_data(patient_id: int) -> pd.DataFrame:
        # SELECT RP.Test_ID, TP.Parameter_Name, RP.Param_Value, R.Analysis_Timestamp
    query = text("""
        SELECT TOP 1 RP.Test_ID, TP.Parameter_Name, RP.Param_Value, R.Analysis_Timestamp
        FROM RESULTS R
        JOIN TESTS T ON R.Test_ID = T.Test_ID
        JOIN RESULTSPARAMETER RP ON R.Test_ID = RP.Test_ID
        JOIN TOTALPARAMETERS TP ON RP.Param_ID = TP.Parameter_ID
        WHERE T.Patient_ID = :pid
        AND R.Analysis_Timestamp = (
            SELECT MAX(R2.Analysis_Timestamp)
            FROM RESULTS R2
            JOIN TESTS T2 ON R2.Test_ID = T2.Test_ID
            WHERE T2.Patient_ID = :pid
        )
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn, params={"pid": patient_id})
    if df.empty:
        return df
    df['Param_Value'] = pd.to_numeric(df['Param_Value'], errors='coerce')
    df_pivot = df.pivot_table(index=['Test_ID', 'Analysis_Timestamp'],
                              columns='Parameter_Name',
                              values='Param_Value',
                              aggfunc='first').reset_index()
    df_pivot.columns = [col.replace('_', ' ') if isinstance(col, str) else col for col in df_pivot.columns]
    return df_pivot

# Get full test history for a patient (used for line graphs)
def get_patient_tests(patient_id: int) -> pd.DataFrame:
    query = text("""
        SELECT RP.Test_ID, TP.Parameter_Name, RP.Param_Value, R.Analysis_Timestamp
        FROM RESULTS R
        JOIN TESTS T ON R.Test_ID = T.Test_ID
        JOIN RESULTSPARAMETER RP ON R.Test_ID = RP.Test_ID
        JOIN TOTALPARAMETERS TP ON RP.Param_ID = TP.Parameter_ID
        WHERE T.Patient_ID = :pid
    """)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn, params={"pid": patient_id})
    if df.empty:
        return df
    df['Param_Value'] = pd.to_numeric(df['Param_Value'], errors='coerce')
    df_pivot = df.pivot_table(index=['Test_ID', 'Analysis_Timestamp'],
                              columns='Parameter_Name',
                              values='Param_Value',
                              aggfunc='first').reset_index()
    df_pivot['Test Date'] = pd.to_datetime(df_pivot['Analysis_Timestamp']).dt.date
    df_pivot.columns = [col.replace('_', ' ') if isinstance(col, str) else col for col in df_pivot.columns]
    return df_pivot

# Check if an email address already exists
def email_exists(email: str) -> bool:
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT COUNT(*) FROM PHYSIOTHERAPISTS 
                WHERE Email = :email AND Is_Active = 1
            """), {'email': email}).scalar()
            return result > 0
    except Exception as e:
        print("❌ Error in email_exists:", e)
        return False

# Check if username already exists
def username_exists(username: str) -> bool:
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT COUNT(*) FROM PHYSIOTHERAPISTS 
                WHERE Username = :username AND Is_Active = 1
            """), {'username': username}).scalar()
            return result > 0
    except Exception as e:
        print("❌ Error in username_exists:", e)
        return False

# Retrieve the last note for a patient
def get_latest_note(patient_id):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT TOP 1 Notes, Start_Time
                FROM TESTS
                WHERE Patient_ID = :pid AND Notes IS NOT NULL AND LTRIM(RTRIM(Notes)) != ''
                ORDER BY Start_Time DESC
            """), {'pid': patient_id}).fetchone()
            return result if result else None
    except Exception as e:
        print("❌ Error in get_latest_note:", e)
        return None

# Update the physiotherapist's preferred language
def update_preferred_language(email, new_language):
    try:
        with engine.begin() as conn:
            conn.execute(text("""
                UPDATE PHYSIOTHERAPISTS
                SET Preferred_Language = :lang
                WHERE Email = :email AND Is_Active = 1
            """), {'lang': new_language, 'email': email})
        return True
    except Exception as e:
        print("❌ Error updating preferred language:", e)
        return False

def get_preferred_language(email):
    try:
        with engine.begin() as conn:
            result = conn.execute(text("""
                SELECT Preferred_Language
                FROM PHYSIOTHERAPISTS
                WHERE Email = :email AND Is_Active = 1
            """), {'email': email}).fetchone()
        return result[0] if result else None
    except Exception as e:
        print("❌ Error fetching preferred language:", e)
        return None
