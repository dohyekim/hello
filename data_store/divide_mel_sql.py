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

#len을 하기 위해서는 모든 stream을 다 가져와야하기 때문에 for loop 안의 reader는 0이 됨
total = len(list(reader))

data = []
save_unit = 15

#다시 뚫기

melon_csv2 = codecs.open("./melon_top.csv","r","euc-kr")
reader2 = csv.reader(melon_csv2, delimiter=',', quotechar = '"')

for i, row in enumerate(reader2):
    # del data[0]
    # del data[len(data) - 1]
    if i != 0 and i != (total - 1):
        data.append((row[0], row[1], row[2], row[3]))
    if len(data) == save_unit or i == (total - 1):
        save('dadb', data)
        data.clear()

# del data[0]
# del data[len(data) - 1]

# save('dadb',data)