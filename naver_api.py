import requests
import json
from bs4 import BeautifulSoup
import pymysql

url = "https://openapi.naver.com/v1/search/blog.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "XEIkDv0Pg4Q3mxlju6Mx",
    "X-Naver-Client-Secret": "5HJNNNG_Gg"
}

res = requests.get(url, params = params, headers = headers).text

jsonData = json.loads(res)

# dic = json.dumps(jsonData, ensure_ascii=False, indent=2)
items = jsonData['items']
dic = json.dumps(items, ensure_ascii=False, indent=2)

sql = '''insert into Api(title, link, description, 
                            bloggername, bloggerlink, postdate)
            values( %(title)s, %(link)s, %(description)s, 
                    %(bloggername)s, %(bloggerlink)s, %(postdate)s ) '''

try:
    conn = pymysql.connect(
    host='192.168.99.100',
    user='dooo',
    password='1234',
    port=3307,
    db='dadb',
    charset='utf8')
    conn.autocommit = False
    cur = conn.cursor()
    
    cur.executemany(sql, dic)
    print("Affected RowCount is", cur.rowcount, "/", len(dic))
    conn.commit()

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




# # for item in jsonData['items']:
# #     print(item['title'].replace('</b>','').replace('<b>',''), item['bloggerlink'], item['bloggername'], item['postdate'])