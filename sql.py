import sqlite3

conn = sqlite3.connect("test.db")

with conn:
    cur = conn.cursor()
    sql = "select * from Student where id = ? or name = ?"
    cur.execute(sql, (1, '아아아'))
    rows = cur.fetchall()

    for row in rows:
        print(row)