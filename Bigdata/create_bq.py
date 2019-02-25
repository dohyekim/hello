import bigquery
import sys
client = bigquery.get_client(json_key_file='./bigquery.json', readonly = False)
# print("identification success")

DATABASE='bqdb'
TABLE='sample'

if not client.check_table(DATABASE, TABLE):
    print("Create table {}.{}".format(DATABASE, TABLE, file = sys.stderr))

    client.create_table(DATABASE, TABLE, [
        {'name': 'songno', 'type': 'string', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'albumid', 'type': 'string', 'description': 'album id'}
    ])

ttt = [
    {'songno': '111', 'title': 'Hong21', 'albumid': '121212121'},
    {'songno': '222', 'title': 'Hong2', 'albumid': '1212121212'},
    {'songno': '333', 'title': 'Hong3', 'albumid': '1212121213'}
        ]
pushResult = client.push_rows(DATABASE, TABLE, ttt, insert_id_key='songno')
print("Pushed Result is", pushResult)


