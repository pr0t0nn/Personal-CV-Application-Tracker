import sqlite3

connection = sqlite3.connect("Applications.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE applications(name, date, cv, coverletter)")

