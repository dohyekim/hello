# 이후 Elastic Search로 Refac

import tedfunctions as f

class ElasticSearch():

    talkcnt = 0    
    engtalk = []
    diffs = []
    kortalk = []
    korsentences = []
    engsentences=[]

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

        cur = conn.cursor()
        cur.execute(sqlisdiff)
        self.diffs = cur.fetchall()

    def engtoKor(self, search):
        # 전체 row 수만큼 loop 돌리도록 수정(int(self.talkcnt)+1)
        for t in range(1, 20):
            if (t,) in self.diffs:
                continue

            # 검색
            s = ''
            s = search[0]
            sqlEngSearch = '''select engcue from English 
                        where eng regexp '([{}{}]{})'
                        and talk_id = {}'''.format(s.lower(), s.upper(), search[1:], t)
            # sqlEngSearch = '''select engcue from English 
            #                     where eng like '%{}%'
            #                     and talk_id = {}'''.format(search, t)
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
                    self.engsentences.append([sentence])
    def engtoKorequiv(self):
        tags = []
        res=[]
        strs = ''
        # print(len(self.engtalk))
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
            cur.close()
            cur = conn.cursor()
            cur.execute(tagSearch)
            tagrows = cur.fetchall()
            cur.close()
            
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

            # 세 개의 문장을 하나의 string으로 만들기
            for i in a:
                strs += (i[0] + ' ')
            res.append("Kor >>>> ..." + strs + "..." + "\nTags >>>> " + tags[0] + "\n")
            print(tid, cue, "\n", self.engsentences[k], "\n", res[k], "\n")


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
                    self.korsentences.append([sentence])

    def kortoEngequiv(self):
        tags = []
        res=[]
        strs = ''

        # print(len(self.engtalk))
        for k, kort in enumerate(self.kortalk):
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

            for english in enrows:
                a.append(english) # eng

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
                strs += (i[0] + ' ')
            res.append("Eng >>>> ..." + strs + "..." + "\nTags >>>> " + tags[0] + "\n")
            print(tid, cue, "\n", self.korsentences[k], "\n", res[k], "\n")


# s = ElasticSearch()
# s.engtoKor('the most important')
# s.engtoKor('start off')
# s.engtoKor('start on')
# s.engtoKor('Thank you')
# s.engtoKorequiv()

# s.kortoEng('감사합니다')
# s.kortoEngequiv()

# s.kortoEng('비합리')
# s.kortoEngequiv()
