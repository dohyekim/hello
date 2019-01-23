from bs4 import BeautifulSoup
import requests
import time

url = "https://www.melon.com/chart/index.htm"
headers = {
    'Referer': 'https://www.melon.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
html = requests.get(url, headers = headers).text
soup = BeautifulSoup(html, 'html.parser')
parameter = []

sel = soup.select("div#tb_list table tbody tr[data-song-no]")

for i in sel:
    a = i.attrs['data-song-no']
    parameter.append(a)
# print(sel)



genres = []

for p in parameter:
    song_url = "https://www.melon.com/song/detail.htm?songId={}".format(p)
    headers = {
        'Referer': 'https://www.melon.com/song/detail.htm?songId=31565593',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    html1 = requests.get(song_url, headers = headers).text
    soup1 = BeautifulSoup(html1, 'html.parser')
    song_num = p

    div = soup1.select_one('div.entry')
    # print(div)?
    genre = div.select_one('dl.list dd:nth-of-type(3)').text
    genres.append
    time.sleep(3)
    