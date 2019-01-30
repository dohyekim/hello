import requests
import json
from bs4 import BeautifulSoup
import pymysql
import re

# drop table Blogger;
# create table dadb.Blogger(
# id int not null auto_increment primary key,
# bloggerid varchar(256),
# bloggername varchar(256),
# bloggerlink varchar(256)
# );

# select * from dadb.Blogger;
# truncate dadb.Blogger;

# drop table BlogPost;
# create table dadb.BlogPost(
# id int not null auto_increment primary key,
# title varchar(256),
# link varchar(256),
# bloggerid varchar(256),
# postdate varchar(10)
# );

# select * from BlogPost;
# truncate BlogPost;
# -- Alter table Song_Rank add constraint foreign key fk_song_rank (song_no) references MS_Song(song_no);
# alter table dadb.BlogPost add constraint foreign key fk_post_blogger(bloggerid) references dadb.Blogger(bloggerid);


url = "https://openapi.naver.com/v1/search/blog.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "asdf",
    "X-Naver-Client-Secret": "asdf"
}

res = requests.get(url, params = params, headers = headers).text

jsonData = json.loads(res)


items = jsonData['items']
dic = json.dumps(items, ensure_ascii=False, indent=2)
# print(dic)

#----------------------table Blogger--------------------
blogger = []
blogpost = []

conn = pymysql.connect(
host='192.168.99.100',
user='dooo',
password='1234',
port=3307,
db='dadb',
charset='utf8')


sql = '''insert into Blogger(bloggerid, bloggername, bloggerlink)
            values(%s, %s, %s) '''

for item in items:
    # bloggerid
    bloglink = item['bloggerlink']
    pattern = re.compile("naver.com\/(.*)")
    bloggerid = re.findall(pattern, bloglink)
    if len(bloggerid) == 0:
        a = "(http(s)*|:|/)"
        bloggerid = [re.sub(a,'',bloglink)]

    #bloggername
    bloggername = item['bloggername']
    #bloggerlink
    bloggerlink = item['link']

    lst = [set(bloggerid[0]),set(bloggername),set(bloggerlink)]
    blogger = [set(lst)]
    
    bcur = conn.cursor()
    bcur.execute(sql, blogger)
    conn.commit()
#--------------------cursor-----------------------------
    #----------------------table BlogPost--------------------
    #title
    title = item['title'].replace('</b>','').replace('<b>','')
    #link
    link = item['link']
    #postdate
    postdate = item['postdate']
    blogpost_dic = {'title' : title, 'link' : link, 'bloggerid' : bloggerid[0],'postdate' : postdate}
    blogpost.append(blogpost_dic)

# #---------------------connection-------------------------

conn2 = pymysql.connect(
host='192.168.99.100',
user='dooo',
password='1234',
port=3307,
db='dadb',
charset='utf8')


sql2 = '''insert into BlogPost(title, link, bloggerid, postdate)
                    values(%(title)s, %(link)s, %(bloggerid)s, %(postdate)s)'''


pcur = conn2.cursor()
pcur.executemany(sql2, blogpost)
conn2.commit()
print("Table BlogPost has been filled ---> affectedrow: ", pcur.rowcount)

