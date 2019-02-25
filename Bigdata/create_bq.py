import bigquery
import sys
<<<<<<< HEAD
client = bigquery.get_client(json_key_file='../../bigquery.json', readonly = False)
=======
client = bigquery.get_client(json_key_file='./bigquery.json', readonly = False)
>>>>>>> 4d7c3674b82b77d1b2e3158fa29013a5e01504c8
# print("identification success")

DATABASE='bqdb'
TABLE='sample'

if not client.check_table(DATABASE, TABLE):
<<<<<<< HEAD
    print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)
=======
    print("Create table {}.{}".format(DATABASE, TABLE, file = sys.stderr))
>>>>>>> 4d7c3674b82b77d1b2e3158fa29013a5e01504c8

    client.create_table(DATABASE, TABLE, [
        {'name': 'songno', 'type': 'string', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'albumid', 'type': 'string', 'description': 'album id'}
    ])

ttt = [
<<<<<<< HEAD
    {'songno': '111', 'title': '홍21', 'albumid': '121212121'},
    {'songno': '222', 'title': '홍2', 'albumid': '1212121212'},
    {'songno': '333', 'title': '홍3', 'albumid': '1212121213'}
=======
    {'songno': '111', 'title': 'Hong21', 'albumid': '121212121'},
    {'songno': '222', 'title': 'Hong2', 'albumid': '1212121212'},
    {'songno': '333', 'title': 'Hong3', 'albumid': '1212121213'}
>>>>>>> 4d7c3674b82b77d1b2e3158fa29013a5e01504c8
        ]
pushResult = client.push_rows(DATABASE, TABLE, ttt, insert_id_key='songno')
print("Pushed Result is", pushResult)


