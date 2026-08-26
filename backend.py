import sqlite3
import app

connection = sqlite3.connect("Applications.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS applications(application_number, date, cv, coverletter)")

def GetApplications():
    cursor.execute("SELECT * FROM applications")
    all_applications = cursor.fetchall()
    return all_applications


def SaveCV(FilePath):
    print(FilePath)