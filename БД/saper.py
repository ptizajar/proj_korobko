import sqlite3 as sq
from data_users import info_users
with sq.connect('saper.db') as con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("CREATE TABLE IF NOT EXISTS users("
                "user_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "name TEXT NOT NULL,"
                "sex INTEGER NOT NULL DEFAULT 1,"
                "old INTEGER,"
                "score INTEGER)")
with sq.connect('saper.db') as con:
    cur=con.cursor()
    cur.executemany("INSERT INTO users VALUES(?,?,?,?,?)",info_users)
with sq.connect('saper.db') as con:
    cur=con.cursor()
    cur.execute("SELECT * FROM users WHERE score > 1000 ORDER BY score DESC")
    result=cur.fetchall()
    print(result)
with sq.connect('saper.db') as con:
    cur=con.cursor()
    cur.execute("SELECT * FROM users WHERE old>17 AND sex=1")
    result1=cur.fetchall()
    print(result1)
with sq.connect('saper.db') as con:
    cur=con.cursor()
    cur.execute("UPDATE users SET score=score+500 WHERE SEX=2")
    cur.execute("SELECT * FROM users WHERE sex=2")
    result3=cur.fetchall()
    print(result3)
with sq.connect('saper.db') as con:
    cur=con.cursor()
    cur.execute("DELETE FROM users WHERE user_id=5")
    cur.execute("SELECT * FROM users")
    result4=cur.fetchall()
    print(result4)