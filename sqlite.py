import sqlite3


class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)

        self.cur = self.con.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS STUDENT(id Integer Primary Key,name TEXT,userid TEXT, contactno TEXT, department TEXT, gender TEXT, year TEXT)'
        self.cur.execute(sql)
        self.con.commit()


    def insert(self, name, userid, contactno, department, gender, year):
        self.cur.execute("insert into STUDENT values (NULL,?, ?, ?, ?, ?, ?)",(name,userid,contactno,department,gender,year))
    # print(A)
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * from STUDENT")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("delete from STUDENT where id=?", (id,))

        self.con.commit()

    def update(self, id, name, userid, contactno, department, gender, year):
        self.cur.execute("update STUDENT set name =?, userid =?, contactno =?, department =?, gender =?, year =? where id =?",(name,userid,contactno,department,gender,year,id))
        self.con.commit()