import sqlite3

conn = sqlite3.connect("test.db")

data = (
    (21, '홍길동'),
    (22, '김길동')
)

with conn:
    cur = conn.cursor()
    sql = "insert into tt(id, name) values(?, ?)"
    cur.executemany(sql,data)

    conn.commit()