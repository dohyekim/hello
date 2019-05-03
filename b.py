import requests
import json
from bs4 import BeautifulSoup
import pymysql
import re
from pprint import pprint

url = "https://openapi.naver.com/v1/search/blog.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "aaaa",
    "X-Naver-Client-Secret": "aaaa"
}

res = requests.get(url, params = params, headers = headers).text

jsonData = json.loads(res)


items = jsonData['items']
dic = json.dumps(items, ensure_ascii=False, indent=2)
# pprint(dic)

#----------------------table Blogger--------------------
blogger = []
blogpost = []


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

    blogger.append(bloggername)
    
a = set(blogger)
print("set blogger>>> ", a, len(a))