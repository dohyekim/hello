# 이후 Elastic Search로 Refac

import tedfunctions as f

class ElasticSearch():

    talkcnt = 0    
    # findEngCue = []
    findEng = []
    findKor = []
    engtalk = []
    engtalkid = []
    kortalk = []
    korsentences = []
    engsentences=[]

    def __init__ (self):

        # 전체 Talk의 수 구하기
        sqltalkcnt = ''' select (@rownum := @rownum + 1) r
                        from Talk t, (select @rownum := 0) rn
                        order by r desc
                        limit 1; '''
        
        talkconn = f.get_conn()
        talkcur = talkconn.cursor()
        talkcur.execute(sqltalkcnt)
        self.talkcnt = talkcur.fetchall()[0][0]

    def engtoKor(self, search):
        # 전체 row 수만큼 loop 돌리도록 수정
        for t in range(1, 10):
            # 개수 비교
            sqlseleng = "select engcue from English where talk_id = {} order by engcue desc limit 1".format(t)
            sqlselkor = "select korcue from Korean where talk_id = {} order by korcue desc limit 1".format(t)

            # 검색
            sqlSearch = '''select engcue from English 
                        where eng like '%{}%'
                        and talk_id = {}'''.format(search, t)
            conn = f.get_conn()
            cur = conn.cursor()
            cur.execute(sqlseleng)
            
            # English table의 row수
            engcnt = cur.fetchall()
            if len(engcnt) != 0:
                engs = engcnt[0][0]
            cur.execute(sqlselkor)

            # Korean table의 row수
            korcnt = cur.fetchall()
            if len(korcnt) != 0:
                kors = korcnt[0][0]

            # 3개 이상 차이가 나면 skip
            if abs(engs - kors) > 3:
                print("Hard to match those two")
                continue

            else:
                cur.execute(sqlSearch)
                rows = cur.fetchall()

                # 검색어가 없는 경우
                if len(rows) == 0:
                    continue
                # 검색어가 있는 경우
                else:
                    for row in rows:
        #                 # (talk_id, cue)
                        # print("row[1]>>>>>", row[1])
                        # talkcue = row[1] # cue
                        cue = row[0]
                        self.engtalk.append((t, cue))
                        # if row[0] in self.engtalkid:
                        #     continue
                        # else:
                        #     self.engtalkid.append(row[0])

                        sentence = ''
                        sqlss = 'select eng from English where engcue between {} and {} and talk_id = {}'.format(cue-1, cue+1, t)
                        # print(sqlss)
                        cur.execute(sqlss)
                        rows2 = cur.fetchall()
                        # print(rows2)
                        for r in rows2:
                            sentence += (r[0]+' ')
                        # print(sentence)
                        self.engsentences.append([sentence])
            # print(self.engsentences)
            # print(len(self.engsentences))
            


    def engtoKorequiv(self):
        tags = []
        res=[]
        # print(len(self.engtalk))
        # print(self.engtalk)
        for k, engt in enumerate(self.engtalk):
            cue = engt[1]
            tid = engt[0]

            # 만일 첫 문장인 경우
            if cue == 1:
                sqlKorSearch = '''select kor from Korean 
                    where korcue between {} and {}
                    and talk_id = {}'''.format(cue, cue+2, tid)

            # 첫 문장이 아닌 경우
            else:     
                sqlKorSearch = '''select kor from Korean 
                    where korcue between {} and {}
                    and talk_id = {}'''.format(cue-1, cue+1, tid)

            # tags 가져오기
            tagSearch = 'select tags from Talk where talk_id = {}'.format(tid)
            conn = f.get_conn()
            cur = conn.cursor()
            cur.execute(sqlKorSearch)
            korows = cur.fetchall() # tuple
            cur.execute(tagSearch)
            tagrows = cur.fetchall()
            
            a=[]

            for korean in korows:
                a.append(korean) # eng

            for m in tagrows:
                tag = m[0]
                
                # 같은 talk_id를 갖고 있는 경우 tag들의 중복 append 방지
                if tag in tags:
                    continue
                else:
                    tags.append(tag)

            # 하나의 string으로 만들기
            estrs = a[0][0] + ' ' + a[1][0] + ' ' + a[2][0]
            res.append("Kor >>>> ..." + estrs + "..." + "\nTags >>>> " + tags[0] + "\n")
            print(tid, cue, "\n", self.engsentences[k], "\n", res[k], "\n")

# -------------------------------------- 여기까지 refac!!! --------------------------------------

    def kortoEng(self, search):
        for t in range(1, 10):
            sqlseleng = "select engcue from English where talk_id = {} order by engcue desc limit 1".format(t)
            sqlselkor = "select korcue from Korean where talk_id = {} order by korcue desc limit 1".format(t)

            sqlSearch = '''select talk_id, korcue from Korean 
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
                    for row in rows:
        #                 # (talk_id, cue)
                        # print("row[1]>>>>>", row[1])
                        # talkcue = row[1] # cue
                        self.kortalk.append((row[0], row[1]))
                        # if row[0] in self.engtalkid:
                        #     continue
                        # else:
                        #     self.engtalkid.append(row[0])

                        sentence = ''
                        sqlss = 'select kor from Korean where korcue between {} and {} and talk_id = {}'.format(row[1]-1, row[1]+1, row[0])
                        # print(sqlss)
                        cur.execute(sqlss)
                        rows2 = cur.fetchall()
                        # print(rows2)
                        for r in rows2:
                            sentence += (r[0]+' ')
                        # print(sentence)
                        self.korsentences.append([sentence])
            # print(self.engsentences)
            # print(len(self.engsentences))

    def kortoEngequiv(self):
        tags = []
        res=[]
        estrs = ''
        for k in range(len(self.kortalk)):
            cue = self.kortalk[k][1]
            if self.kortalk[k][1] == 1:
                sqlEngSearch = '''select engcue, eng from English 
                    where engcue between {} and {}
                    and talk_id = {}'''.format(cue, cue+1, self.kortalk[k][0])
            else:     
                sqlEngSearch = '''select engcue, eng from English 
                    where engcue between {} and {}
                    and talk_id = {}'''.format(cue-1, cue+1, self.kortalk[k][0])
            talkid = self.kortalk[k][0]
            # talkids.append(talkid) # talk_id
            tagSearch = 'select tags from Talk where talk_id = {}'.format(talkid)
            conn = f.get_conn()
            cur = conn.cursor()
            cur.execute(sqlEngSearch)
            erows = cur.fetchall() # tuple
            cur.execute(tagSearch)
            esearch = cur.fetchall()
            aa=[]

            for j in erows:
                aa.append(j) # eng
            # print(a)
            # print(len(a))

            for m in esearch:
                tag = m[0]
                if tag in tags:
                    continue
                else:
                    tags.append(tag)
            searchstrs = ", ".join(tags)
            for a in aa:
                estrs += (a[1] + ' ') 
        # print(estrs)
            # print(self.korsentences[k])
            res.append("Eng >>>> ..." + estrs + "..." + "\nTags >>>> " + searchstrs + "\n")
            print("\n", self.korsentences[k], "\n", res[k], "\n")


s = ElasticSearch()
s.engtoKor('inspire')
s.engtoKorequiv()

# s.kortoEng('감사합니다')
# s.kortoEngequiv()

# s.kortoEng('비합리')
# s.kortoEngequiv()

# 구분해서 출력하는 코드 짜기