import sqlite3

connection = sqlite3.connect("Applications.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS applications(id INTEGER PRIMARY KEY AUTOINCREMENT, company_name TEXT, date TEXT, cv TEXT)")
connection.commit()

def GetApplications():
    cursor.execute("SELECT id, company_name, date, cv FROM applications")
    return cursor.fetchall()

def SaveApplication(company_name, date, cv):
    cursor.execute("INSERT INTO applications(company_name, date, cv) VALUES(?, ?, ?)", (company_name, date, cv))
    connection.commit()
    return cursor.lastrowid
