import sqlite3

connection = sqlite3.connect("Applications.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS applications(id INTEGER PRIMARY KEY AUTOINCREMENT, company_name TEXT, date TEXT, cv TEXT, status TEXT)")
connection.commit()

def GetApplications():
    cursor.execute("SELECT id, company_name, date, cv, status FROM applications")
    return cursor.fetchall()

def SaveApplication(company_name, date, cv):
    cursor.execute("INSERT INTO applications(company_name, date, cv, status) VALUES(?, ?, ?, ?)", (company_name, date, cv, "Pending"))
    connection.commit()
    return cursor.lastrowid

def UpdateStatus(application_id, status):
    cursor.execute("UPDATE applications SET status = ? WHERE id = ?", (status, application_id))
    connection.commit()
