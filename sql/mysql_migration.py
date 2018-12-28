import pymysql

def get_mysql_conn(db):
    return pymysql.connect(
        host = 'localhost', 
        user = 'dooo', 
        password = '1234', 
        port = 3307, 
        db = db, 
        charset = 'utf8'
        )

def trun_table(conn, tbl):
    cur = conn.cursor()   
    cur.execute('truncate ' + tbl)


def get_count(conn, tbl, where = ''):
    cur = conn.cursor()
    sql = "Select count(*) from " + tbl
    if where != '':
        sql = sql + "where" + where
    cur.execute(sql)

    return cur.fetchone()[0]

import cx_Oracle

def get_oracle_conn():
    return cx_Oracle.connect("hr", "hrpw", "localhost:1521/xe")
    


