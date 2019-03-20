from bs4 import BeautifulSoup
import requests
import re
import json
# from pprint import pprint
import time
import pymysql

def get_conn():
    return pymysql.connect(
        host='127.0.0.1',
        user='dooo',
        password='1234',
        port=3306,
        db='corpusdb',
        charset='utf8')

def getLastId(sql):
    conn = get_conn()
    cur = conn.cursor()    
    cur.execute(sql)
    lastid = cur.fetchall()
    return lastid        

sqllastid = 'select talk_id from Talk order by talk_id desc limit 1'
sqlTalk = '''insert into Talk(talk_id, title, genre, talk_year, tags) 
                        values( %s,%s,%s,%s,%s)'''
sqlSpeaker = "insert into Speaker(speaker_id, name) values(%s, %s)"
sqlEnglish = "insert into English(talk_id, engcue, eng) values(%s,%s,%s)"
sqlKorean = "insert into Korean(talk_id, korcue, kor) values(%s,%s,%s)"
sqlTalkSpeaker = "insert into TalkSpeaker (talk_id, speaker_id) values (%s, %s)"

# 값 비우기(쿼리문, num = lastid + 1)
# lastid 가져오기

# print(lastid)
# print("num >> ", num)
# exit()
class Ted:

    lastid = getLastId(sqllastid)
    if len(lastid) == 0:
        num = 1
    else:
        num = lastid[0][0] + 1

    talk = []
    speaker = []
    korean = []
    english = []
    talkspeaker = []
    isEng = True

    def __init__(self):
        print('----------------------{} started --------------------'.format(self.num))
        # exit()
        url = 'https://www.ted.com/talks/' + str(self.num) + '/details'
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
        #talk_id == num
        # talk_id = targeting['id']
        tags = targeting['tag']
        talk_year = targeting['year']
        genre = targeting['event'] 
        
        self.talk=[(self.num, title, genre, talk_year, tags)]

        #---------------------------------speaker json------------------------------------
        pattern = re.compile('"speakers":(.*),\"url')
        speakers = re.findall(pattern, script)
        spkJson = json.loads(speakers[0])
        speaker_id = spkJson[0]['id']
        name = spkJson[0]['firstname'] + ' ' + spkJson[0]['lastname']
        self.speaker=[(speaker_id, name)]
        self.talkspeaker=[(self.num, speaker_id)]
        self.saveTalk()
        print('-----------------save Talk Done----------------')
    
    def getEngData(self, lang='en'):
        
        pgnum = 1

        url = 'https://www.ted.com/talks/' + str(self.num) + '/transcript.json?language=' + lang

        stat_json = requests.get(url)
        jjson = stat_json.text
        if stat_json.status_code != 200:
            print("{} translation does not exist".format(lang))
            self.isEng = False
            return 
        else:
            print("Requests succeess")
        jsonData = json.loads(jjson, encoding="utf-8") 

        t = ''
        #paragraphs
        pgs = jsonData['paragraphs']
        for cues in pgs:
            texts = cues['cues']
            for text in texts:
                t = text['text']

                if '\n' in t:
                    t = t.replace('\n',' ')
                self.english.append((self.num, pgnum, t))
                pgnum += 1
        
        self.saveEnglish()
        print("-----------------save English Done----------------")



    def getKorData(self, lang='ko'):
        if self.isEng == False:
            return
        kpgnum = 1

        kurl = 'https://www.ted.com/talks/' + str(self.num) + '/transcript.json?language=' + lang

        kstat_json = requests.get(kurl)
        kjjson = kstat_json.text
        if kstat_json.status_code != 200:
            print("{} translation does not exist".format(lang))
            pass
        else:
            print("Requests succeess")
        kjsonData = json.loads(kjjson, encoding="utf-8") 

        t = ''
        pgs = kjsonData['paragraphs']
        for cues in pgs:
            texts = cues['cues']
            for text in texts:
                t = text['text']

                if '\n' in t:
                    t = t.replace('\n',' ')
                self.korean.append((self.num, kpgnum, t))
                kpgnum += 1

        self.saveKorean()
        print('-----------------save Korean Done----------------')


    def save(self,sql, data):
        try:
            conn = get_conn()
            conn.autocommit = False
            cur = conn.cursor()
            
            cur.executemany(sql, data)
            if sql == sqlEnglish:
                print("Affected RowCount is {}/{}".format(cur.rowcount,len(self.english)) )
            elif sql == sqlKorean:
                print("Affected RowCount is {}/{}".format(cur.rowcount,len(self.korean)) )
            else:
                print("Affected RowCount is ", cur.rowcount)
            conn.commit()

            # sql = "select text1 from AAA"
            # cur.execute(sql)
            # aaa = cur.fetchall()
            # print(aaa[0][0].replace('\\',''))

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

    def saveTalk(self):
        self.save(sqlTalk, self.talk)

    def saveSpeaker(self):
        self.save(sqlSpeaker, self.speaker)

    def saveEnglish(self):
        self.save(sqlEnglish, self.english)

    def saveKorean(self):
        self.save(sqlKorean, self.korean)

    def saveTalkSpeaker(self):
        self.save(sqlTalkSpeaker, self.talkspeaker)

    


for i in range(1,5):
    ted = Ted()
    time.sleep(2)
    ted.getEngData()
    print('-----------------English Done----------------')
    time.sleep(2)
    ted.getKorData()
    print('-----------------Korean Done----------------')

    ted.saveSpeaker()
    print('-----------------save Speaker Done----------------')

    ted.saveTalkSpeaker()
    print('-----------------save Talkspeaker Done----------------')

