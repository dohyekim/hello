import mysql_migration as mm


conn_dooodb = mm.get_mysql_conn('dooodb')
with conn_dooodb:
    dooo_cnt = mm.get_count(conn_dooodb, 'Subject')


conn_dadb = mm.get_mysql_conn('dadb')
with conn_dadb:
    dadb_cnt = mm.get_count(conn_dadb, 'Subject')

if dooo_cnt == dadb_cnt:
    print("OK", "Dooo-->" ,dooo_cnt, "dadb--->", dadb_cnt)
    

else:
    print("Not Okay", "Dooo-->" ,dooo_cnt, "dadb--->", dadb_cnt)

conn_dooodb = mm.get_mysql_conn('dooodb')
with conn_dooodb:
    cur = conn_dooodb.cursor()
    rand = "select id, name, prof, classroom from Subject order by rand() limit 5"
    cur.execute(rand)
    rand_dooodb = cur.fetchall()

    print(rand_dooodb)

a = []
for i in range(0,5):
    a.append(rand_dooodb[i][0])
print(a)



conn_dadb = mm.get_mysql_conn('dadb')
with conn_dadb:
    cur = conn_dadb.cursor()
    vr = "select id, name, prof, classroom from Subject where id = %s"
    vr_dadb = []
    for i in a:
        (cur.execute(vr, i))
        vr_dadb.append(cur.fetchone())
        
    print(tuple(vr_dadb))

if rand_dooodb == tuple(vr_dadb):
    print("OK")


