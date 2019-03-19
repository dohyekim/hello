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
        port=3307,
        db='corpusdb',
        charset='utf8')


sqlTalk = '''insert into Talk(talk_id, title, genre, talk_year, tags) 
                        values( %s,%s,%s,%s,%s)'''
sqlSpeaker = "insert into Speaker(speaker_id, name) values(%s, %s)"
sqlEnglish = "insert into English(talk_id, engcue, eng) values(%s,%s,%s)"
sqlKorean = "insert into Korean(talk_id, korcue, kor) values(%s,%s,%s)"
sqlTalkSpeaker = "insert into TalkSpeaker (talk_id, speaker_id) values (%s, %s)"

class Ted:

    talk = []
    speaker = []
    korean = []
    english = []
    talkspeaker = []
    isEng = True

    def __init__(self, num): 
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
        #talk_id == num
        # talk_id = targeting['id']
        tags = targeting['tag']
        talk_year = targeting['year']
        genre = targeting['event'] 
        
        self.talk.append((num, title, genre, talk_year, tags))

        #---------------------------------speaker json------------------------------------
        pattern = re.compile('"speakers":(.*),\"url')
        speakers = re.findall(pattern, script)
        spkJson = json.loads(speakers[0])
        speaker_id = spkJson[0]['id']
        name = spkJson[0]['firstname'] + ' ' + spkJson[0]['lastname']
        self.speaker.append((speaker_id, name))
        self.talkspeaker.append((num, speaker_id))
    
    def getEngData(self, num, lang='en'):
  
        resultpg = {}
        pgnum = 1

        url = 'https://www.ted.com/talks/' + str(num) + '/transcript.json?language=' + lang

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
                self.english.append((num, pgnum, t))
                pgnum += 1


    def getKorData(self, num, lang='ko'):
        if self.isEng == False:
            return
        kpgnum = 1

        kurl = 'https://www.ted.com/talks/' + str(num) + '/transcript.json?language=' + lang

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
                self.korean.append((num, kpgnum, t))
                kpgnum += 1
    def save(self,sql, data):
        try:
            conn = get_conn()
            conn.autocommit = False
            cur = conn.cursor()
            
            cur.executemany(sql, data)
            print("Affected RowCount is", cur.rowcount)
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




ted = Ted(1)
ted.getEngData(1)
print('-----------------English Done----------------')
ted.getKorData(1)
print('-----------------Korean Done----------------')

ted.saveTalk()
print('-----------------save Talk Done----------------')
ted.saveSpeaker()
print('-----------------save Speaker Done----------------')
ted.saveEnglish()
print('-----------------save English Done----------------')
ted.saveKorean()
print('-----------------save Korean Done----------------')
ted.saveTalkSpeaker()
print('-----------------save Talkspeaker Done----------------')


