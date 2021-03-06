import pymysql
import mysql_migration as mm

conn_dooodb = mm.get_mysql_conn('dooodb')


with conn_dooodb:
    cur = conn_dooodb.cursor()
    sql = "select name, prof, classroom from Subject"
    cur.execute(sql)
    rows = cur.fetchall()


conn_dadb = mm.get_mysql_conn('dadb')


with conn_dadb:
    cur = conn_dadb.cursor()
    mm.trun_table(conn_dadb, 'Subject')
    sql = "insert into Subject(name, prof, classroom) values(%s, %s, %s)"
    cur.executemany(sql, rows)
    print("AffectedRowsCount-->", cur.rowcount)
    conn_dadb.commit()