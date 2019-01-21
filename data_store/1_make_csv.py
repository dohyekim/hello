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


def melon(rank):

    trs = rank
    song_info = {}

    for tr in trs:
        t = tr.select_one('div.ellipsis.rank01 a').text
        songno = tr.get('data-song-no')
        s = tr.select_one('div.ellipsis.rank02 span a').text
        r = tr.select_one('span.rank').text
        if len(s) >= 2:
                s1 = []
                for j in s:
                    s1.append(j)
                s1 = ",".join(s1)
        aaaa = {"ranking" : r, "title" : t, "singer" :s}
        song_info[songno] = aaaa

    song_id = []
    for j in jsonData['contsLike']:
        song_id = str(j['CONTSID'])
        x = song_info.get(song_id)
        if x == None:
            continue    
        x['Like'] = j['SUMMCNT']
    
    # print(song_info)

    dic = sorted(song_info.items(), key=lambda d: int(d[1]['ranking']))
    print(dic)
    # like = sorted(song_info.items(), key=lambda d: d[1]['Like'])
    # least_like = like[0][1]['Like']
    least_like_a = min(x[1]['Like'] for x in song_info.items())

    like_sum = 0
    least_like_sum = 0
    
    with codecs.open('./melon_top.csv', 'w', 'euc-kr') as ff:
        writer = csv.writer(ff, delimiter=',', quotechar='"')
        writer.writerow(['랭킹','제목','가수명','좋아요','좋아요 차이'])

        for i in dic:
            writer.writerow([i[1]['ranking'], i[1]['title'], i[1]['singer'], i[1]['Like'], (i[1]['Like'] - least_like_a)])
            like_sum = like_sum + i[1]['Like']
            least_like_sum = least_like_sum + (i[1]['Like'] - least_like_a)

        writer.writerow(['계', '', '', like_sum, least_like_sum])

melon(sel)