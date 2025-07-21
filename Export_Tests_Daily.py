import pypyodbc as odbc
import pandas as pd
from datetime import datetime

# Connecting to the database
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'ELAD-COMPUTER\\SQLEXPRESS'
DATABASE_NAME = 'DB_Final_Project'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;
"""

# Query to retrieve tests from today
query = """
SELECT 
    T.Test_ID,
    T.Patient_ID,
    T.Physiotherapist_ID,
    T.Start_Time,
    T.End_Time,
    T.Test_Status,
    T.Notes,
    T.Error_Type,
    T.Error_Description_Patient
FROM TESTS AS T
WHERE CAST(T.Start_Time AS DATE) = CAST(GETDATE() AS DATE)
"""

try:
    conn = odbc.connect(connection_string)
    df = pd.read_sql(query, conn)
    conn.close()

    # Target file – includes date
    filename = datetime.now().strftime("Tests_%Y-%m-%d.csv")
    filepath = f"C:/Users/elada\PycharmProjects/‏‏Final_Project - עותק/Reports/{filename}"

    df.to_csv(filepath, index=False, encoding='utf-8-sig')
    print(f"✅ CSV exported to: {filepath}")

except Exception as e:
    print(f"❌ Error: {e}")
