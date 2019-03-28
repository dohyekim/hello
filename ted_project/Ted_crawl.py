from bs4 import BeautifulSoup
import requests
import re
import json
import random
# from pprint import pprint
import time
import pymysql
import os

# with open("chart", "w", encoding="utf-8") as chartfile:
#     chartfile.write("D1 ,K1 ,E1  ,\n")

# with open("chart", "a", encoding="utf-8") as addfile:
#     addfile.write("D{},K{},E{}, \n".format(i,i,i))

sqllastid = 'select talk_id from Korean order by talk_id desc limit 1'
sqlTalk = '''insert into Talk(talk_id, title, event, talk_year, tags) 
                        values( %s,%s,%s,%s,%s)'''
sqlSpeaker = "insert into Speaker(speaker_id, name, field) values(%s, %s, %s)"
sqlEnglish = "insert into English(talk_id, engcue, eng) values(%s,%s,%s)"
sqlKorean = "insert into Korean(talk_id, korcue, kor) values(%s,%s,%s)"
sqlTalkSpeaker = "insert into TalkSpeaker (talk_id, speaker_id) values (%s, %s)"


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
    
nfound = []
ifkorean = []
error = []

class TedCrawl():
    
    
    num = 0
    isEng = True
    isNF = True
    # isKorean = []
    talk = []
    speaker = []
    korean = []
    english = []
    talkspeaker = []

    def __init__(self):
        a = []
        with open("chart","r",encoding="utf-8") as readfile:
            for line in readfile:
                a.append(line[1])
            number = len(a)
        self.num = number

        # global nfound
        # if len(nfound) != 0:
        #     self.num = nfound[0] + 1
        # nfound = []

    def engcrawl(self, lang='en'):
        self.num += 1
        print("============================{} started ====================================".format(self.num))
        # if self.isNF == False:
        #     self.isEng = False
        #     return
        if os.path.exists("html/" + lang + str(self.num) + ".json") == True:
            print(" {} English json already exists".format(self.num))
            return
        else:
            time.sleep(random.randrange(5,10))
            url = 'https://www.ted.com/talks/' + str(self.num) + '/transcript.json?language=' + lang
            stat_json = requests.get(url)
            if stat_json.status_code == 404:
                print("----------------------------English PAGE DO NOT EXIST----------------------------")
                # nfound.append(self.num)
                self.isEng = False
                # print(self.nfound)
                # isNF = False
                print("{} translation does not exist".format(lang), stat_json.status_code)
                return

            else:
                print(stat_json.status_code)
                # 저장하기
                jjson = stat_json.json()
                print("{} Requests succeess".format(lang))
                with open("html/" + lang + str(self.num) + ".json", 'w') as engjson:
                    json.dump(jjson, engjson)


    def korcrawl(self, lang='ko'):
        # self.num += 1
        if os.path.exists("html/" + lang + str(self.num) + ".json") == True:
            print(" {} Korean json already exists".format(self.num))
            return
        else:
            time.sleep(random.randrange(5,10))
            url = 'https://www.ted.com/talks/' + str(self.num) + '/transcript.json?language=' + lang
            if self.isEng == False:
                print(" No need to get Korean Translation ")
                return
            else:
                stat_json = requests.get(url)
                if stat_json.status_code == 404:
                    print("----------------------------Korean PAGE DO NOT EXIST----------------------------")
                    # global ifkorean
                    # ifkorean.append(self.num)
                    print("{} translation does not exist".format(lang), stat_json.status_code)
                    return

                else:
                    print(stat_json.status_code)
                    # 저장하기
                    jjson = stat_json.json()
                    print("{} Requests succeess".format(lang))
                    with open("html/" + lang + str(self.num) + ".json", 'w') as engjson:
                        json.dump(jjson, engjson)


    
    def getDetail(self):
        if self.isEng == False:
            with open("chart", "a", encoding="utf-8") as addfile:
                addfile.write("D{}\n".format(self.num))
            return
        
        # elif self.isNF == False:
            # self.isNF == True
            # return
        # html = ''
        if os.path.exists("html/" + str(self.num) + ".htm"):
            print(" Detail page already exists")
            with open("chart", "a", encoding="utf-8") as addfile:
                addfile.write("D{}\n".format(self.num))
            return
            # with open("html/" + str(self.num) +".htm", 'r', encoding='utf-8') as rfile:
            #     for i in rfile:
            #         html += i
            # print("Finished writing HTML")

        else:
            time.sleep(random.randrange(5,10))
            url = 'https://www.ted.com/talks/' + str(self.num)
            req = requests.get(url)
            print(req.status_code)
            html = req.text
            # if req.status_code == 404:
            #     print("----------------------------Detail PAGE DO NOT EXIST----------------------------")

            #     self.nfound.append(self.num)
            #     self.isNF = False
            #     # time.sleep(1)
            #     print(self.nfound)
            #     return
            # else:
            print("{} Detail requests success ".format(self.num))
            # self.nfound.clear()
            with open("html/{}.htm".format(self.num), 'w', encoding='utf-8') as file:
                file.write(html)
            with open("chart", "a", encoding="utf-8") as addfile:
                addfile.write("D{}\n".format(self.num))



nos = []
class Ted():

    talk = []
    speaker = []
    korean = []
    english = []
    talkspeaker = []
    num = 0

    def __init__(self):
        self.num = getLastId(sqllastid)[0][0] + 1
        global nos
        if len(nos) != 0:
            self.num = nos[-1] + 1

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


    def sqlEngData(self, lang='en'):
        if os.path.exists("html/" + lang + str(self.num) + ".json") == False:
            return

        # self.num = getLastId(sqllastid)
        print('======================= English SQL {} started ============================='.format(self.num))
        with open("html/" + lang + str(self.num) + ".json", encoding='utf-8') as kjson:
            jsonData = json.load(kjson)
        eng = []
        cue = 1

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

    def sqlKorData(self, lang='ko'):
        if os.path.exists("html/" + lang + str(self.num) + ".json") == False:
            return

        # self.num = self.getlastId(sqllastid)
        print('========================= Korean SQl {} started ============================='.format(self.num))
        with open("html/" + lang + str(self.num) + ".json", encoding='utf-8') as kjson:
            jsonData = json.load(kjson)
        kor = []
        kcue = 1

        t = ''
        #paragraphs
        pgs = jsonData['paragraphs']
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

    def sqlDetail(self):
        if os.path.exists("html/" + str(self.num) + ".htm") == False:
            nos.append(self.num)
            return

        print('========================= Detail SQl {} started ============================='.format(self.num))

        htmls = ''
        with open("html/" + str(self.num) +".htm", 'r', encoding='utf-8') as rfile:
            for i in rfile:
                htmls += i

        soup = BeautifulSoup(htmls, 'html.parser')
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

            self.saveSpeaker()
            self.saveTalkSpeaker()
            self.saveTalk()

        except Exception as err:
            global error
            error.append(self.num)
            print("error >>>>>>>>>>>> ", err)
            print(plyrtalks)




for i in range(1, 10):
    tedcrawl = TedCrawl()
    tedcrawl.engcrawl()
    tedcrawl.korcrawl()
    tedcrawl.getDetail()



for i in range(1,10):
    ted = Ted()
    ted.sqlEngData()
    ted.sqlKorData()
    ted.sqlDetail()

def updateTalk(talk_id):
    sqlUpdate = '''update Talk t set isKorean = (select case when max(k.kor) is null then 0 else 1 end
                                from English e left outer join Korean k on e.talk_id = k.talk_id
                                where e.talk_id = t.talk_id)
                    where talk_id > ''' + str(talk_id) + ';'

    try: 
        print(" UPDATE STARTED ")
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(sqlUpdate)
        conn.commit()
        print(" UPDATE SUCCESS ")

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

updateTalk(90)