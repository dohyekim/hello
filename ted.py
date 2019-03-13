from bs4 import BeautifulSoup
import requests
import re
import json
# from pprint import pprint
import time
# import pymysql

def getDetail(num):

    details = {}

    url = 'https://www.ted.com/talks/' + str(num) + '/details'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    # with open("lecturer.htm", "r", encoding='utf8') as file:
    #     soup = BeautifulSoup(file, 'html.parser')
    script = str(soup.find_all('script'))


    #---------------------------------title json------------------------------------
    pattern = re.compile('"player_talks":(.*),\"ratings')
    plyrtalks = re.findall(pattern, script)
    jsonTitle = json.loads(plyrtalks[0])
    jsonData = jsonTitle[0]
    title = jsonData['title']

    #---------------------------------detailinfo json------------------------------------
    targeting = jsonData['targeting']
    talkid = targeting['id']
    tags = targeting['tag']
    year = targeting['year']
    genre = targeting['event'] 

    #---------------------------------speaker json------------------------------------
    pattern = re.compile('"speakers":(.*),\"url')
    speakers = re.findall(pattern, script)

    spkJson = json.loads(speakers[0])
    spkid = spkJson[0]['id']
    spkname = spkJson[0]['firstname'] + ' ' + spkJson[0]['lastname']

    details['talkId'] = talkid
    details['title'] = title
    details['speakerId'] = spkid
    details['speakerName'] = spkname
    details['genre'] = genre
    details['tags'] = tags
    details['year'] = year
    print(details)
    return details

# url = 'https://www.ted.com/talks/minda_dentler_what_i_learned_when_i_conquered_the_world_s_toughest_triathlon/details'
# html = requests.get(url).text
# with open("details.htm", 'w', encoding='utf-8') as file2:
#     file2.write(html)
# with open("details.htm", 'r', encoding='utf-8') as file:
#     soup = BeautifulSoup(file, 'html.parser')
def getData(num, lang='en'):
    resultpg = {}
    pgnum = 1
    # texts = []
    url = 'https://www.ted.com/talks/' + str(num) + '/transcript.json?language=' + lang
    # params = {
    #     'language' : lang
    # }
    stat_json = requests.get(url)
    jjson = stat_json.text
    if stat_json.status_code != 200:
        print("Korean translation does not exist    ")
        return None
    else:
        print("Requests succeess")
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

        resultpg[pgnum] = t
        pgnum += 1
        t = ''
        
    # print(resultpg)

    return resultpg[1]

for i in range(1,10):
    getData(i)
    time.sleep(2)
    getData(i, 'ko')
    time.sleep(2)
    getDetail(i)
    time.sleep(2)
    
# # ----------------------------------db connection -------------------------------
# def get_conn():
#    return pymysql.connect(
#        host='127.0.0.1',
#        user='dooo',
#        password='1234',
#        port=3307,
#        db='dooodb',
#        charset='utf8')


# # -----------------------------------db insert ------------------------------------
# data = getData(9,'en')
# insert_sql = "insert into AAA (text1) values (%s)"
# def save(sql, data):
#     try:
#         conn = get_conn()
#         conn.autocommit = False
#         cur = conn.cursor()
        
#         cur.execute(sql, data)
#         print("Affected RowCount is", cur.rowcount)
#         conn.commit()

#         sql = "select text1 from AAA"
#         cur.execute(sql)
#         aaa = cur.fetchall()
#         print(aaa[0][0].replace('\\',''))


#     except Exception as err:
#         conn.rollback()
#         print("Error!!", err)

#     finally:
#         try:
#             cur.close()
#         except:
#             print("Error on close cursor")
#         try:
#             conn.close()
#             print ("OOKKKK")
#         except Exception as err2:
#             print("Fail to connect!!", err2)

# save(insert_sql, data)