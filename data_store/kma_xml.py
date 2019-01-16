import requests
from bs4 import BeautifulSoup

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp"

res = requests.get(url)

with open("./kma.xml", "w", encoding="utf-8") as f:
    f.write(res.text)

soup = BeautifulSoup(res.text, "html.parser")
title = soup.select('item title')
print(title)

data = soup.select('body data')

for datum in data:
    seq = datum.attrs['seq']
    ws = datum.select_one('ws').text
    wd = datum.select_one('wdkor').text
    print(seq, ws, wd)