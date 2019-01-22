import requests
from bs4 import BeautifulSoup
import json
import csv
import codecs

url = "https://www.melon.com/chart/index.htm"
headers = {
    'Referer': 'https://www.melon.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
html = requests.get(url, headers = headers).text
soup = BeautifulSoup(html, 'html.parser')

urlj = "https://www.melon.com/commonlike/getSongLike.json"
parameter = []

sel = soup.select("div#tb_list table tbody tr[data-song-no]")


links = []
for tr in sel:
    link_tag = tr.select('td:nth-of-type(7) div.ellipsis.rank03 a')
    for l in link_tag:
        link = l.attrs['href']
        links.append(link)

print(links)

for i in sel:
    a = i.attrs['data-song-no']
    parameter.append(a)

param_ = ",".join(parameter)

params = {
    "contsIds" : str(param_)
}

headersj = {
    "Referer": "https://www.melon.com/chart/index.htm",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


htmlj = requests.get(urlj, params = params, headers = headersj).text
jsonData = json.loads(htmlj, encoding='utf-8')


# Permlink == https://www.melon.com/album/detail.htm?albumId=10238683
# "javascript:melon.link.goAlbumDetail('10238683')