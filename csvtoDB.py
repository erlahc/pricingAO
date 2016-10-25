import sqlite3
import csv
import os



def csvtolist(chemin):
    file = open(chemin)
    reader = csv.reader(file)
    data = list(reader)
    data.sort()
    return data


conn = sqlite3.connect("base1.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS input(
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT,
activity TEXT,
turnover FLOAT,
country TEXT,
PIE TEXT,
CSP TEXT,
scope TEXT,
crosswork TEXT,
manual INTEGER)
""")
data = csvtolist("2 - DataSet csv/DB.csv")
for i in range(len(data)):
    cursor.execute("""INSERT INTO input(name, activity, turnover, country, PIE, CSP, scope, crosswork, manual)
    VALUES(?,?,?,?,?,?,?,?,?)""", data[i])

cursor.execute("""CREATE TABLE IF NOT EXISTS abaque(
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
activity TEXT,
mini FLOAT,
structure TEXT,
base FLOAT)
""")
data = csvtolist("2 - DataSet csv/ABAQUE.csv")
for i in range(len(data)):
    cursor.execute("""INSERT INTO abaque(activity,mini,structure,base)
    VALUES(?,?,?,?)""", data[i])

conn.commit()
conn.close()


