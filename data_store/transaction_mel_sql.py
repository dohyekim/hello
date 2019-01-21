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

sql_truncate = "truncate table Meltop"
sql_delete = "delete from Meltop"
sql_insert = "insert into Meltop(rank, title, singer, likecnt) values(%s,%s,%s,%s)"

isStart = True

def save(db, data):
    try:
        conn = get_mysql_conn(db)
        conn.autocommit = False
        cur = conn.cursor()

        global isStart
        if isStart:
            cur.execute(sql_delete)  
        isStart = False


        cur.executemany(sql_insert, data)
        conn.commit()
        print("Affected Rows ---> ", cur.rowcount, "/", len(data))
    except Exception as err:
        try :
            conn.rollback()
        except:
            print("Error!! rollback done", err)
            

    finally:
        try:
            cur.close()
        except:
            print("Failed to close cursor")
        try:
            conn.close()
        except Exception as err2:
            print("Fail to connect!!", err2)

melon_csv = codecs.open("./melon_top.csv","r","euc-kr")
reader = csv.reader(melon_csv, delimiter=',', quotechar = '"')

data = []
for row in reader:
    data.append((row[0], row[1], row[2], row[3]))

del data[0]
del data[len(data) - 1]

save('dadb',data)