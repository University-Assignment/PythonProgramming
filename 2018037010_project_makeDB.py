import sqlite3

dbPath = 'Project.db'
con = sqlite3.connect(dbPath)

cur = con.cursor()
cur.execute('CREATE TABLE account (id integer primary key autoincrement, userid TEXT, password TEXT)')
con.commit()