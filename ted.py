from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint
import time
import pymysql

url = 'https://www.ted.com/talks/minda_dentler_what_i_learned_when_i_conquered_the_world_s_toughest_triathlon/transcript'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
bigdiv = soup.select_one('div.bg:gray-ll.c:black.p-x:2.p-y:.5.bg:white@md')
lecturer = bigdiv.select_one('div.f:.9.m-b:.4.m-t:.5.d:i-b').text
topic = bigdiv.select_one('div.d:i-b.f:.9')
title = bigdiv.select_one('hi.f-w:900.l-h:t.l-s:t.m-y:0.f:3')

tagdiv = soup.select_one('f:.9.p-x:3@md.c:black.t-a:l')
tags = tagdiv.select('ul.l-s-t:n.p-l:0.m-y:0 li.t-t:c')
taglist = []
for tag in tags:
    tag = tag.text
    taglist.append(tag)

print(title)

def getData(num, lang):
    resultpg = {}
    pgnum = 1
    # texts = []
    url = 'https://www.ted.com/talks/' + str(num) + '/transcript.json?language=' + lang
    params = {
        'language' : lang
    }
    jjson = requests.get(url, params = params).text
    jsonData = json.loads(jjson, encoding="utf-8")
    t = ''
    #paragraphs
    pgs = jsonData['paragraphs']
    for pg in pgs:

        cues = pg['cues']
        for i in range(len(cues)):
            text = cues[i]['text']
            # print(text)
            if text[-1] == ' ' :
                t = t + text
                t = t.replace('\n', ' ')
            else :
                t = t + text + ' ' 
                t = t.replace('\n', ' ')
        # print ([pgnum, t])
        # print((pgnum, t))
        
        resultpg['topic'] = topic
        # resultpg['year'] = 
        resultpg['title'] = title
        resultpg['lecturer'] = lecturer
        resultpg['tags'] = taglist

        resultpg[pgnum] = t
        # resultpg['eng'] = resultpg[pgnum]
        # resultpg['kor'] = resultpg[pgnum]
        pgnum += 1
        t = ''
        
    # print(resultpg)
    return resultpg[1]


# ----------------------------------db connection -------------------------------
def get_conn():
   return pymysql.connect(
       host='127.0.0.1',
       user='dooo',
       password='1234',
       port=3307,
       db='dooodb',
       charset='utf8')


# -----------------------------------db insert ------------------------------------
data = getData(9,'en')
insert_sql = "insert into AAA (text1) values (%s)"
def save(sql, data):
    try:
        conn = get_conn()
        conn.autocommit = False
        cur = conn.cursor()
        
        cur.execute(sql, data)
        print("Affected RowCount is", cur.rowcount)
        conn.commit()

        sql = "select text1 from AAA"
        cur.execute(sql)
        aaa = cur.fetchall()
        print(aaa[0][0].replace('\\',''))


    except Exception as err:
        conn.rollback()
        print("Error!!", err)

    finally:
        try:
            cur.close()
        except:
            print("Error on close cursor")
        try:
            conn.close()
            print ("OOKKKK")
        except Exception as err2:
            print("Fail to connect!!", err2)

save(insert_sql, data)
