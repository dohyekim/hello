import pymysql
import json

def get_conn(db):
    return pymysql.connect(
        host='127.0.0.1',
        user='dooo',
        password='1234',
        port=3306,
        db=db,
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8')


conn = get_conn('corpusdb')
cur = conn.cursor()
sql = 'select * from Talk where talk_id between 1 and 5'
cur.execute(sql)
rows = cur.fetchall()
# print(rows)

# with open("sampledata/examples.json", 'w') as file4:
#         json.dump(rows, file)

with open("sampledata/examples3.json","w") as file:
    tid = rows[0]['talk_id']
    dic = { "index" : { "_index" : "corpus", "_type" : "Corpus", "_id" : tid } }
    json.dump(dic, file)
    file.write("\n")
    json.dump(rows[0], file)
    file.write("\n")

with open("sampledata/examples3.json","a") as file2:
    for i in range(1,len(rows)):
        tid = rows[i]['talk_id']
        dic = { "index" : { "_index" : "corpus", "_type" : "Corpus", "_id" : tid } }
        json.dump(dic, file2)
        file2.write("\n")
        json.dump(rows[i], file2)
        file2.write("\n")
# # with open ("sampledata/examples.json","r") as file3:
    
# # 
# # def json (self) :
# #     j = {c.name: getattr(self, c.name) for c in self.__table__.columns}
# #     return j



# # with open("sampledata/examples.json", "r") as file2:
# #     with open("sampledata/examples2.json","a") as file3:
# #         for f in file2:

# #             # jsonData = json.load(f)
# #             # print(jsonData)
# #             # print(type(jsonData))