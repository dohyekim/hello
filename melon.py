import requests
from bs4 import BeautifulSoup
import json

url = "https://www.melon.com/chart/index.htm"
headers = {
    'Referer': 'https://www.melon.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
html = requests.get(url, headers = headers).text
soup = BeautifulSoup(html, 'html.parser')


urlj = "https://www.melon.com/commonlike/getSongLike.json"
parameter = []

rank_50 = soup.select("table > tbody #lst50")
rank_100 = soup.select("table > tbody #lst100")

for i in rank_50:
    a = i.attrs['data-song-no']
    parameter.append(a)

for j in rank_100:
    b = j.attrs['data-song-no']
    parameter.append(b)

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



def melon(rank):

    trs = rank
    song_info = {}
    for tr in trs:
        t = tr.select_one('div.ellipsis.rank01 a')
        songno = tr.get('data-song-no')
        s = tr.select_one('div.ellipsis.rank02 span a')
        r = tr.select_one('span.rank').text
        if len(s) >= 2:
                s1 = []
                for j in s:
                    s1.append(j.text)
                s1 = ",".join(s1)
        aaaa = {"rank----->" : r, "title" : t, "singer" :s}
        song_info[songno] = aaaa

    song_id = []
    for j in jsonData['contsLike']:
        song_id = str(j['CONTSID'])
        x = song_info.get(song_id)
        if x == None:
            continue    
        x['♡'] = j['SUMMCNT']
        print(x)

melon(rank_50)
melon(rank_100)
