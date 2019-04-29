# 이후 Elastic Search로 Refac

import tedfunctions as f
from pprint import pprint
class ElasticSearch():

    talkcnt = 0    
<<<<<<< HEAD
    # findEngCue = []
    findEng = []
    findKor = []
    engtalk = []
    kortalk = []

=======
    engtalk = []
    diffs = []
    kortalk = []
    korsentences = []
    engsentences=[]
    shows={}
>>>>>>> 97e557429b08ffdb80f9227f2de91259c4e30523
    def __init__ (self):

        # 전체 Talk의 수 구하기
        conn = f.get_conn()
        cur = conn.cursor()
        
        sqltalkcnt = ''' select (@rownum := @rownum + 1) r
                        from Talk t, (select @rownum := 0) rn
                        order by r desc
                        limit 1; '''

        sqlisdiff = 'select talk_id from Talk where diff = 0'
        
        cur.execute(sqltalkcnt)
        self.talkcnt = cur.fetchall()[0][0]

<<<<<<< HEAD
    def engtoKor(self, search):
        # 전체 row 수만큼 loop 돌리도록 수정
=======
        cur = conn.cursor()
        cur.execute(sqlisdiff)
        self.diffs = cur.fetchall()

    def engtoKor(self, search):
        # 전체 row 수만큼 loop 돌리도록 수정(int(self.talkcnt)+1)
>>>>>>> 97e557429b08ffdb80f9227f2de91259c4e30523
        for t in range(1, 20):
            if (t,) in self.diffs:
                continue

<<<<<<< HEAD
            sqlSearch = '''select talk_id, engcue, eng from English 
                        where eng like '%{}%'
                        and talk_id = {}'''.format(search, t)
       
=======
            # 검색
            s = ''
            s = search[0]
            sqlEngSearch = '''select engcue from English 
                        where eng regexp '([{}{}]{})'
                        and talk_id = {}'''.format(s.lower(), s.upper(), search[1:], t)
            # sqlEngSearch = '''select engcue from English 
            #                     where eng like '%{}%'
            #                     and talk_id = {}'''.format(search, t)
>>>>>>> 97e557429b08ffdb80f9227f2de91259c4e30523
            conn = f.get_conn()
            cur = conn.cursor()
            cur.execute(sqlEngSearch)
            rows = cur.fetchall()
            cur.close()

            # 검색어가 없는 경우
            if len(rows) == 0:
                continue
            # 검색어가 있는 경우
            else:
<<<<<<< HEAD
                cur.execute(sqlSearch)
                rows = cur.fetchall()
                if len(rows) == 0:
                    continue
                else:
                    print("rows >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ", rows)
                    for i in range(len(rows)):
                        # (talk_id, cue, english)
                        talkcue = (rows[i][0], rows[i][1], rows[i][2])
                        self.engtalk.append(talkcue)
                    print(self.engtalk)
                print("--------------- NEXT TURN -----------------")

    def engtoKorequiv(self):
        for k in range(len(self.engtalk)):
            cue = self.engtalk[k][1]
            if self.engtalk[k][1] == 1:
                sqlKorSearch = '''select korcue, kor from Korean 
=======
                for row in rows:
                    cue = row[0]
                    self.engtalk.append((t, cue))
                    sentence = ''
                    sqleng = 'select eng from English where engcue between {} and {} and talk_id = {}'.format(cue-1, cue+1, t)
                    # print(sqlss)
                    cur = conn.cursor()
                    cur.execute(sqleng)
                    rows2 = cur.fetchall()
                    cur.close()
                    # print(rows2)
                    for r in rows2:
                        sentence += (r[0]+' ')
                    # print(sentence)
                    self.engsentences.append(sentence)
    def engtoKorequiv(self):
        tags = []

        n=0
        # print(len(self.engtalk))
        for k, engt in enumerate(self.engtalk):
            strs = ''
            cue = engt[1]
            tid = engt[0]

            # 만일 첫 문장인 경우
            if cue == 1:
                sqlKorSearch = '''select kor from Korean 
>>>>>>> 97e557429b08ffdb80f9227f2de91259c4e30523
                    where korcue between {} and {}
                    and talk_id = {}'''.format(cue, cue+2, tid)

            # 첫 문장이 아닌 경우
            else:     
                sqlKorSearch = '''select kor from Korean 
                    where korcue between {} and {}
<<<<<<< HEAD
                    and talk_id = {}'''.format(cue-2, cue+2, self.engtalk[k][0])
            
            tagSearch = 'select tags from Talk where talk_id = {}'.format(self.engtalk[k][0])
            conn = f.get_conn()
            cur = conn.cursor()
            cur.execute(sqlKorSearch)
            krows = cur.fetchall() # tuple
            cur.execute(tagSearch)
            ksearch = cur.fetchall()
            for j in krows:
                self.findKor.append(j[1])
            kstrs = " ".join(self.findKor)

        print(kstrs, ksearch)

    def kortoEng(self, search):
        for t in range(1, 5):
            sqlseleng = "select engcue from English where talk_id = {} order by engcue desc limit 1".format(t)
            sqlselkor = "select korcue from Korean where talk_id = {} order by korcue desc limit 1".format(t)

            sqlSearch = '''select talk_id, korcue, kor from Korean 
                        where kor like '%{}%'
                        and talk_id = {}'''.format(search, t)
        
            conn = f.get_conn()
            cur = conn.cursor()
            cur.execute(sqlseleng)
            engcnt = cur.fetchall()
            if len(engcnt) != 0:
                engs = engcnt[0][0]
            cur.execute(sqlselkor)
            korcnt = cur.fetchall()
            if len(korcnt) != 0:
                kors = korcnt[0][0]
            # print(abs(engcnt - korcnt))
            if abs(engs - kors) > 3:
                print(" Hard to match those two ")
                continue

            else:
                cur.execute(sqlSearch)
                rows = cur.fetchall()
                if len(rows) == 0:
                    continue
                else:
                    print("rows >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ", rows)
                    for i in range(len(rows)):
                        # (talk_id, cue, english)
                        talkcue = (rows[i][0], rows[i][1], rows[i][2])
                        self.kortalk.append(talkcue)
            print("--------------- NEXT TURN -----------------")
        print(self.kortalk)

    def kortoEngequiv(self):
        res = []
        tags = []
        for k in range(len(self.kortalk)):
            cue = self.kortalk[k][1]
            if self.kortalk[k][1] == 1:
                sqlEngSearch = '''select engcue, eng from English 
                    where engcue between {} and {}
                    and talk_id = {}'''.format(cue, cue+2, self.kortalk[k][0])
            else:     
                sqlEngSearch = '''select engcue, eng from English 
                    where engcue between {} and {}
                    and talk_id = {}'''.format(cue-2, cue+2, self.kortalk[k][0])

            ktagSearch = 'select tags from Talk where talk_id = {}'.format(self.kortalk[k][0])
            conn = f.get_conn()
            cur = conn.cursor()
            cur.execute(sqlEngSearch)
            erows = cur.fetchall() # tuple
            cur.execute(ktagSearch)
            esearch = cur.fetchall()
            for j in erows:
                self.findEng.append(j[1])
            for m in esearch:
                tags.append(str(m))
            searchstrs = ", ".join(tags)
            estrs = " ".join(self.findEng)
            # print(type(searchstrs))
            # print(type(estrs))
            res.append("... " + estrs + "... \n" + searchstrs + "\n")
            

        print(res)
=======
                    and talk_id = {}'''.format(cue-1, cue+1, tid)

            # tags 가져오기
            tagSearch = 'select tags from Talk where talk_id = {}'.format(tid)
            conn = f.get_conn()
            cur = conn.cursor()
            cur.execute(sqlKorSearch)
            korows = cur.fetchall() # tuple
            cur.close()
            cur = conn.cursor()
            cur.execute(tagSearch)
            tagrows = cur.fetchall()
            cur.close()
            
            a=[]

            for korean in korows:
                a.append(korean[0]) # eng
>>>>>>> 97e557429b08ffdb80f9227f2de91259c4e30523

            for m in tagrows:
                tag = m[0]
                
                # 같은 talk_id를 갖고 있는 경우 tag들의 중복 append 방지
                if tag in tags:
                    continue
                else:
                    tags.append(tag)

            # 세 개의 문장을 하나의 string으로 만들기
            for i in a:
                strs += i + ' '
            show = {'tid' : tid, 'cue':cue, 'engsentences':self.engsentences[k], 'result':strs}
            self.shows[n] = show
            n += 1
        pprint(self.shows)
        return self.shows


    def kortoEng(self, search):
        # int(self.talkcnt)+1
        for t in range(1, 10):
            if (t,) in self.diffs:
                continue

            # 검색
            sqlKorSearch = '''select korcue from Korean 
                        where kor like '%{}%'
                        and talk_id = {}'''.format(search, t)
            conn = f.get_conn()
            cur = conn.cursor()
            cur.execute(sqlKorSearch)
            rows = cur.fetchall()
            cur.close()

            # 검색어가 없는 경우
            if len(rows) == 0:
                continue
            # 검색어가 있는 경우
            else:
                for row in rows:
                    cue = row[0]
                    self.kortalk.append((t, cue))
                    sentence = ''
                    sqlkor = 'select kor from Korean where korcue between {} and {} and talk_id = {}'.format(cue-1, cue+1, t)
                    # print(sqlss)
                    cur = conn.cursor()
                    cur.execute(sqlkor)
                    rows2 = cur.fetchall()
                    cur.close()
                    # print(rows2)
                    for r in rows2:
                        sentence += (r[0]+' ')
                    # print(sentence)
                    self.korsentences.append(sentence)

    def kortoEngequiv(self):
        # print("self.korsentences>>", self.korsentences)
        tags = []
        # res=[]
        # eng=[]
        n=1

        print(self.kortalk)
        for k, kort in enumerate(self.kortalk):
            strs = ''
            cue = kort[1]
            tid = kort[0]

            # 만일 첫 문장인 경우
            if cue == 1:
                sqlEngSearch = '''select eng from English 
                    where engcue between {} and {}
                    and talk_id = {}'''.format(cue, cue+2, tid)

            # 첫 문장이 아닌 경우
            else:     
                sqlEngSearch = '''select eng from English 
                    where engcue between {} and {}
                    and talk_id = {}'''.format(cue-1, cue+1, tid)

            # tags 가져오기
            tagSearch = 'select tags from Talk where talk_id = {}'.format(tid)
            conn = f.get_conn()
            cur = conn.cursor()
            cur.execute(sqlEngSearch)
            enrows = cur.fetchall() # tuple
            cur.close()
            cur = conn.cursor()
            cur.execute(tagSearch)
            tagrows = cur.fetchall()
            cur.close()
            
            a=[]
            # print("english >>>", enrows)
            for english in enrows:
                a.append(english[0]) # eng
            # print("aa>>", a)
            for m in tagrows:
                tag = m[0]
                
                # 같은 talk_id를 갖고 있는 경우 tag들의 중복 append 방지
                if tag in tags:
                    continue
                else:
                    tags.append(tag)
            # print("aaa>>", a)
            # 세 개의 문장을 하나의 string으로 만들기
            for i in a:
                strs += i + ' '
            show = {'number' : n, 'tid' : tid, 'cue':cue, 'korsentences':self.korsentences[k], 'result':strs}
            self.shows[n] = show
            self.shows['number'] = n
            n += 1
        pprint(self.shows)
        return self.shows
                
s = ElasticSearch()
<<<<<<< HEAD
# s.get('inspire')
# s.korequiv()
s.kortoEng('감사합니다')
s.kortoEngequiv()
=======
# s.engtoKor('the most important')
# s.engtoKor('start off')
# s.engtoKor('start on')
s.engtoKor('Thank you')
s.engtoKorequiv()

# s.kortoEng('감사합니다')
# s.kortoEngequiv()

# s.kortoEng('비합리')
# s.kortoEngequiv()
>>>>>>> 97e557429b08ffdb80f9227f2de91259c4e30523
