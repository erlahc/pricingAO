import sqlite3

class Entity:
    def __init__(self,db_entity):
        self.name = db_entity[1]
        self.activity = db_entity[2]
        self.turnover = db_entity[3]
        self.country = db_entity[4]
        self.pie = db_entity[5]
        self.csp = db_entity[6]
        self.scope = db_entity[7]
        self.crosswork = db_entity[8]
        self.manual = db_entity[9]


conn=sqlite3.connect('base1.db')
cur=conn.cursor()
cur.execute("SELECT * FROM abaque")
abaque = list(cur.fetchall())
cur.execute("SELECT * FROM input")
db_temp = list(cur.fetchall(
    ))
db=[]
for i in db_temp:
    db.append(Entity(i))  

