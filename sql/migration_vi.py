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