import pymysql

def get_conn(db):
    return pymysql.connect(
        host = 'localhost', 
        user = 'dooo', 
        password = '1234', 
        port = 3307, 
        db = db, 
        charset = 'utf8'
        )

conn_dooodb = get_conn('dooodb')


with conn_dooodb:
    cur = conn_dooodb.cursor()
    sql = "select name, prof, classroom from Subject"
    cur.execute(sql)
    rows = cur.fetchall()


conn_dadb = get_conn('dadb')


with conn_dadb:
    cur = conn_dadb.cursor()
    cur.execute('truncate dadb.Subject')
    sql = "insert into Subject(name, prof, classroom) values(%s, %s, %s)"
    cur.executemany(sql, rows)
    print("AffectedRowsCount-->", cur.rowcount)
    conn_dadb.commit()