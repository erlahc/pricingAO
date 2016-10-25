import sqlite3

conn=sqlite3.connect('base1.db')
cur=conn.cursor()
cur.execute("SELECT * FROM abaque")
data = list(cur.fetchall())

print(len(data))
