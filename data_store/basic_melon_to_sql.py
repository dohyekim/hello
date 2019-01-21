import pymysql
import csv
import codecs


def get_mysql_conn(db):
    return pymysql.connect(
        host = 'localhost', 
        user = 'dooo', 
        password = '1234', 
        port = 3307, 
        db = db, 
        charset = 'utf8'
        )


data = []
melon_csv = codecs.open("./melon_top.csv","r","euc-kr")
reader = csv.reader(melon_csv, delimiter=',', quotechar = '"')
for row in reader:
    data.append((row[0], row[1], row[2], row[3]))

del data[0]
del data[len(data) - 1]
# del data[0]

conn_dadb = get_mysql_conn('dadb')
with conn_dadb:
    cur = conn_dadb.cursor()
    sql_truncate = "truncate table Meltop"
    sql_insert = "insert into Meltop(rank, title, singer, likecnt) values(%s,%s,%s,%s)"
    cur.execute(sql_truncate)
    cur.executemany(sql_insert, data)
    print(cur.rowcount)


# with conn_dooodb:
#     cur = conn_dooodb.cursor()
#     sql = "select name, prof, classroom from Subject"
#     cur.execute(sql)
#     conn.commit
#     rows = cur.fetchall()


# conn_dadb = mm.get_mysql_conn('dadb')
