from bs4 import BeautifulSoup
import requests
import re
import json
# from pprint import pprint
import time
import pymysql
import os

def get_conn():
    return pymysql.connect(
        host='127.0.0.1',
        user='dooo',
        password='1234',
        port=3307,
        db='corpusdb',
        charset='utf8')

def getLastId(sql):
    conn = get_conn()
    cur = conn.cursor()    
    cur.execute(sql)
    lastid = cur.fetchall()
    cur.close()
    return lastid        

sqltalklastid = 'select talk_id from Talk order by talk_id desc limit 1'

sqlTalk = '''insert into Talk(talk_id, title, event, talk_year, tags) 
                        values( %s,%s,%s,%s,%s)'''
sqlSpeaker = "insert into Speaker(speaker_id, name, field) values(%s, %s, %s)"
sqlEnglish = "insert into English(talk_id, engcue, eng) values(%s,%s,%s)"
sqlKorean = "insert into Korean(talk_id, korcue, kor) values(%s,%s,%s)"
sqlTalkSpeaker = "insert into TalkSpeaker (talk_id, speaker_id) values (%s, %s)"

error = []
nfound = []
# 값 비우기(쿼리문, num = lastid + 1)
# lastid 가져오기

# print(lastid)
# print("num >> ", num)
# exit()
class Ted:

    num = 0

    talk = []
    speaker = []
    korean = []
    english = []
    talkspeaker = []
    isEng = True

    def __init__(self):

        lastid = getLastId(sqltalklastid)
        if len(lastid) == 0:
            self.num = 1
        else:
            self.num = lastid[0][0] + 1

        if len(nfound) != 0:
            self.num = nfound[0] + 1
        # print(self.num)
        # return

    def getDetail(self):

        print('============================={} started ============================='.format(self.num))
        # exit()
        if os.path.exists("html/{}.html}".format(self.num)) == True:
            with open("html/{}.html".format(self.num), 'r', encoding='utf-8') as rfile:
                req = rfile 

        else:
            url = 'https://www.ted.com/talks/' + str(self.num)
            req = requests.get(url)
            html = req.text
            if req.status_code == 404:
                print("----------------------------PAGE DO NOT EXIST----------------------------")
                nfound.append(self.num)
                time.sleep(1)
                exit()
            else:
                nfound.clear()
                with open("html/{}.html".format(self.num), 'w', encoding='utf-8') as file:
                    file.write(html)


        soup = BeautifulSoup(html, 'html.parser')
        # with open("lecturer.htm", "r", encoding='utf8') as file:
        #     soup = BeautifulSoup(file, 'html.parser')
        script = str(soup.find_all('script'))
        # print(script)


        #---------------------------------title json------------------------------------
        pattern = re.compile('"player_talks":(.*),\"ratings')
        plyrtalks = re.findall(pattern, script)
        try:
            jsonTitle = json.loads(plyrtalks[0])
            jsonData = jsonTitle[0]
            title = jsonData['title']
            #---------------------------------detailinfo json------------------------------------
            targeting = jsonData['targeting']
            #talk_id == num
            # talk_id = targeting['id']
            tags = targeting['tag']
            talk_year = targeting['year']
            event = targeting['event'] 
            
            self.talk=[(self.num, title, event, talk_year, tags)]

            #---------------------------------speaker json------------------------------------
            pattern = re.compile('"speakers":(.*),\"url')
            speakers = re.findall(pattern, script)
            spkJson = json.loads(speakers[0])
            speaker_id = spkJson[0]['id']
            name = spkJson[0]['firstname'] + ' ' + spkJson[0]['lastname']
            field = spkJson[0]['description']
            self.speaker=[(speaker_id, name, field)]
            self.talkspeaker=[(self.num, speaker_id)]

            self.saveTalk()
            self.saveSpeaker()
            self.saveTalkSpeaker()

        except Exception as err:
            error.append(self.num)
            print("error >>>>>>>>>>>> ", err, "Status code >> ", req.status_code)
            print(plyrtalks)
    
    def getEngData(self, lang='en'):
        # print(self.num)
        # return
        eng = []
        cue = 1

        if os.path.exists("html/eng{}.html}".format(self.num)) == True:
            with open("html/eng{}.html".format(self.num), 'r', encoding='utf-8') as rengfile:
                jjson = rengfile 
        else:
            url = 'https://www.ted.com/talks/' + str(self.num) + '/transcript.json?language=' + lang
            stat_json = requests.get(url)
            jjson = stat_json.text
            
            with open("html/eng{}.html".format(self.num), 'w', encoding='utf-8') as k_file:
                k_file.write(jjson)

            if stat_json.status_code != 200:
                self.isEng = False
                print("{} translation does not exist".format(lang), stat_json.status_code)
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
                eng.append((self.num, cue, t))
                cue += 1
        self.english = eng
        
        self.saveEnglish()
        print("-----------------save English Done----------------")



    def getKorData(self, lang='ko'):
        kor = []
        kcue = 1
        # print(self.num)

        if self.isEng == False:
            print("---------DO NOT NEED TO GET KOREAN TRANSLATION----------------")
            return
        else:

            if os.path.exists("html/kor{}.html}".format(self.num)) == True:
                with open("html/kor{}.html".format(self.num), 'r', encoding='utf-8') as rengfile:
                    kjjson = rengfile 
            
            else:

                kurl = 'https://www.ted.com/talks/' + str(self.num) + '/transcript.json?language=' + lang

                kstat_json = requests.get(kurl)
                kjjson = kstat_json.text
                with open("html/kor{}.html".format(self.num), 'w', encoding='utf-8') as e_file:
                    e_file.write(kjjson)
                if kstat_json.status_code != 200:
                    print("{} translation does not exist".format(lang))
                    return
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
                kor.append((self.num, kcue, t))
                kcue += 1
        self.korean = kor
        self.saveKorean()

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
        print('@@@@@@@@@@@@@@@@@@@@@@@@ Talk Done @@@@@@@@@@@@@@@@@@@@@@@@')

    def saveSpeaker(self):
        self.save(sqlSpeaker, self.speaker)
        print('@@@@@@@@@@@@@@@@@@@@@@@@ Speaker Done @@@@@@@@@@@@@@@@@@@@@@@@')

    def saveEnglish(self):
        self.save(sqlEnglish, self.english)
        print('@@@@@@@@@@@@@@@@@@@@@@@@ English Done @@@@@@@@@@@@@@@@@@@@@@@@')

    def saveKorean(self):
        self.save(sqlKorean, self.korean)
        print('@@@@@@@@@@@@@@@@@@@@@@@@ Korean Done @@@@@@@@@@@@@@@@@@@@@@@@')

    def saveTalkSpeaker(self):
        self.save(sqlTalkSpeaker, self.talkspeaker)
        print('@@@@@@@@@@@@@@@@@@@@@@@@ TalkSpeaker Done @@@@@@@@@@@@@@@@@@@@@@@@')


for i in range(1,10):
    time.sleep(5)
    ted = Ted()
    ted.getDetail()

    time.sleep(3)
    ted.getEngData()
    time.sleep(3)
    ted.getKorData()


print(error)
print(nfound)