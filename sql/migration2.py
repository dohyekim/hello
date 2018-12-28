import mysql_migration as mm

connection = mm.get_oracle_conn()

with connection:

  cursor = connection.cursor()

  sql = '''select region_id, region_name from Regions'''

  cursor.execute(sql)
  rows = cursor.fetchall()

for row in rows:
  print(row)


conn_dadb = mm.get_mysql_conn('dadb')
with conn_dadb:
    cur = conn_dadb.cursor()
    cur.execute("drop table if exists Regions")
    sql_create = '''Create table Regions(
        id smallint not null auto_increment primary key,
        region_name varchar(36)
    )'''

    
    cur.execute(sql_create)
    sql_insert = "insert into Regions(id, region_name) values(%s, %s)"
    cur.executemany(sql_insert,rows)
    print("AffectedRows-->", cur.rowcount)
    conn_dadb.commit()
