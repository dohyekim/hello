import pymysql
import bigquery
import sys, os
from google.cloud import bigquery as bq
import bigquery

passwd = os.getenv('passwd')
keyfile = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
DATABASE='bqdb'
TABLE='SongAlbum'

song_sql = "select s.song_no, s.title, s.genre, a.album_id, a.album_title, a.album_genre, cast(a.rating as char(10)) as rating, cast(a.releasedt as char(30)) as releasedt, a.album_comp, a.entertainment, cast(a.crawldt as char(30)) as crawldt from MS_Song s inner join Album a on s.album_id = a.album_id"
client = bigquery.get_client(json_key_file=keyfile, readonly = False)


def collectData():
    conn= pymysql.connect(
        host='35.243.112.23',
        user='root',
        password=passwd,
        port=3306,
        db='melondb',
        # cursorclass=pymysql.cursors.DictCursor,
        charset='utf8')

    with conn:

        cur = conn.cursor()
        cur.execute(song_sql)

        # cur.description == 
        # (('song_no', 253, None, 50, 50, 0, False), ('title', 253, None, 128, 128, 0, True), ('genre', 253, None, 50, 50, 0, True), ('album_id', 253, None, 50, 50, 0, False))
        cols = [c[0] for c in cur.description]
        albumidx = cols.index('album_id')
        
        for row in cur.fetchall():
            dic = {}
            album = {}
            for idx, r in enumerate(row):
                if idx < albumidx:
                    dic[ cols[idx] ] = r
                else:
                    album[ cols[idx] ] = r
            dic['albumdetail'] = album 
            yield dic


# # # ---------------------bigquery--------------------------------

def createTable():
    if not client.check_table(DATABASE, TABLE):
        print("Create table {}.{}".format(DATABASE, TABLE, file = sys.stderr))

    client.create_table(DATABASE, TABLE, [
        {'name': 'song_no', 'type': 'string', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'genre', 'type': 'string', 'description': 'song genre'},
        {'name': 'albumdetail', 'type': 'record', 'description': 'album detail',
        'fields': [{'name': 'album_id', 'type': 'string'},
                    {'name': 'album_title', 'type': 'string'},
                    {'name': 'album_genre', 'type': 'string'},
                    {'name': 'rating', 'type': 'float', 'description': 'album rating'},
                    {'name': 'releasedt', 'type':'date'},
                    {'name': 'album_comp', 'type':'string'},
                    {'name': 'entertainment', 'type':'string'},
                    {'name': 'crawldt', 'type':'timestamp'}

                    ]}])


def insertData():
    
    pushResult = client.push_rows(DATABASE, TABLE, collectData(), insert_id_key='song_no')
    print("Pushed Result is", pushResult)

def readData():
    client = bq.Client()
    QUERY = 'select * from `%s.%s` limit 100' %(DATABASE, TABLE)
    print("Query sent")
    query_job = client.query(QUERY)
    print("Selected Data")
    rows = query_job.result()
    for row in rows:
        print(row)

# createTable()
# insertData()
readData()
    