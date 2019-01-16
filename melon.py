import requests
from bs4 import BeautifulSoup
import json
import csv, codecs

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


def melon(rank,writemode,least):

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

    dic = sorted(song_info.items(), key=lambda d: d[1]['ranking'])
    print(dic)
    like = sorted(song_info.items(), key=lambda d: d[1]['Like'])
    least_like = like[0][1]['Like']
    least_like_a = min(x['Like'] for x in dic.items())

    
    with codecs.open('./melon_top.csv', writemode, 'utf-8') as ff:
        writer = csv.writer(ff, delimiter=',', quotechar='"')
        writer.writerow(['랭킹','제목','가수명','좋아요','좋아요 차이'])

        least_like_100 = min(lst)

        like_sum = 0
        least_like_sum = 0

        for i in dic:
            writer.writerow([i[1]['ranking'], i[1]['title'], i[1]['singer'], i[1]['Like'], (i[1]['Like'] - least_like_100)])
            like_sum = like_sum + i[1]['Like']
            least_like_sum = least_like_sum + (i[1]['Like'] - least_like_100)

        writer.writerow(['계', '', '', like_sum, least_like_sum])

melon(rank_50, 'w')
melon(rank_100, 'a')
    




