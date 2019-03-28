# 이후 Elastic Search로 Refac

import tedfunctions as f

class ElasticSearch():
    
    findEngCue = []
    findEng = []
    def __init__ (self):
        sqlSearch = '''select engcue, eng from English 
	                where eng like '%Thank you%';'''
        
        conn = f.get_conn()
        cur = conn.cursor()
        cur.execute(sqlSearch)
        rows = cur.fetchall()
        for i in range(len(rows)):
            findEngCue.append(rows[i][0])
            findEng.append(rows[i][1])

        # engcue = rows[0][0]
        # print(engcue)
        # print(type(engcue))
        # eng = rows[0][1]
        # print(eng)
        # print(type(eng))

    def Korequiv(self, start, end):
        sqlKorSearch = '''select korcue, kor from Korean 
            where korcue between {} and {};'''.format(start, end)

        conn = f.get_conn()
        cur = conn.cursor()
        cur.execute(sqlKorSearch)
        krows = cur.fetchall()
        
s = ElasticSearch()
