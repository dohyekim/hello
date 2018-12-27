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

    

# # dooodb (target)
# conn_dooodb = get_conn('dooodb')

# # "select name, prof, classroom from Subject"
# with conn_dooodb:
#     cur = conn_dooodb.cursor()
#     cnt = "select count(*) from Subject"
#     cur.execute(cnt)
#     cnt_dooodb = cur.fetchall()
#     rand = "select id from Subject order by rand() limit 5"
#     cur.execute(rand)
#     rand_dooodb = cur.fetchall()
#     print(rand_dooodb)
    
# # dadb (source)
# conn_dadb = get_conn('dadb')

# with conn_dadb:
#     cur = conn_dadb.cursor()
#     cnt = "select count(*) from Subject"
#     cur.execute(cnt)
#     cnt_dadb = cur.fetchall()



# print("AffectedRowsDooodb-->", cnt_dooodb, "AffectedRowsDadb-->", cnt_dadb)

# conn_dadb_valid = get_conn('dadb')
# with conn_dadb_valid:
#     cur = conn_dadb_valid.cursor()
    
#     for i in rand_dooodb:
#         valid = "select id, name from Subject where id = "
#         cur.execute(valid)
#         valid_dadb = cur.fetchall()
#         print(valid_dadb)