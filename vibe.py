from bs4 import BeautifulSoup
import requests
import re

albumid = '3003472'

# url = 'https://music.naver.com/album/index.nhn?albumId=3003472'

# headers = {
#     "Referer": 'https://music.naver.com/recommend/albumTimeLine.nhn?fromTime=2010&toTime=2020&searchType=album&orderType=score&viewType=thumbnail&genre=K01&display=12',
#     "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
# }

# res = requests.get(url, headers=headers)
# html = res.text
# soup = BeautifulSoup(html, "html.parser")
# album = soup.select('div.spot.album_end')

# with open('bts.html', 'w', encoding = 'utf-8') as file:
#     file.write(html)

html = ''
with open('bts.html', 'r', encoding='utf-8') as file:
    for f in file:
        html += f
# print(html)

pattern = re.compile(".*=(.*)")
# # ===================== Album ========================
soup = BeautifulSoup(html, 'html.parser')
album = soup.select_one('div#content ')
title = album.select_one('div.spot.album_end div.info_txt h2').text
releasedt = album.select_one('div.spot.album_end div.info_txt dl.desc dt.date+dd').text
algenre = album.select_one('div.spot.album_end div.info_txt dl.desc dt.type+dd').text
company = album.select_one('div.spot.album_end div.info_txt dl.desc dt.company+dd').text
tracks = soup.select('div table tbody td.name a:nth-of-type(3)')
# del tracks[0]
tids = []
artist = []
songHtmls = ''
for t in tracks:
    # print(t)
    tid = t.get('href')[1:]
    # print(thref)
    # songUrl = ' https://music.naver.com/lyric/index.nhn?trackId={}'.format(tid)
    # songHeaders = {'Referer' : 'https://music.naver.com/album/index.nhn?albumId={}'.format(albumid), 
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    # songRes = requests.get(songUrl, headers = songHeaders)
    # songHtml = songRes.text
    # with open('btssong.html','w', encoding='utf-8') as file2:
    #     file2.write(songHtml)
    with open('btssong.html', 'r', encoding='utf-8') as file3:
        for f in file3:
            songHtmls += f
        # songHtml += file3
    songSoup = BeautifulSoup(songHtmls, 'html.parser')
    info = songSoup.select_one('div#pop_content')
    artists = info.select_one('div.section_info div.dsc span.artist a')
        artisthref = a.select_one('a').get('href')
        artistid = re.findall(pattern, artisthref)[0]

        artist.append({'type':0, 'id':artistid, 'name':artists.text.strip()})
print(artist)
singer = []
artists = album.select('dl.desc dt.artist+dd')
for a in artists:
    singerhref = a.select_one('a').get('href')
    singerid = re.findall(pattern, singerhref)[0]
    singer.append({'type':0,'id':singerid,'name':a.text.strip()})
    

# print("title >>> ", title)
# print("releasedt >>> ", releasedt)
# print("album genre >>> ", algenre)
# print("company >>> ", company)
# print("singer >>> ", singer)

# ===================== Song ========================
# songselector = soup.select('div.section div.song_info_lst ol.song_info_ol li')
# # ico_play


# songtitle = []     # songtitle
# for s in songselector:
#     songtitles = s.select('span.tit')
#     for t in songtitles:
#         songtitle.append(t.text.strip())
#     songgenre = album.select_one('dl.desc dd:nth-of-type(2)').text    # genre

# artistidhref = album.select_one('dl.desc dd.artist a').get('href')
# artist = []
# artistid = re.findall(pattern, artistidhref)[0]   # artistid

# lyricist = []     # lyricist
# lyricistnames = songselector.select('span.info')
# composer = []      # composer
# for l in lyricistnames:
#     ttt = l.select_one('em').text
#     if ttt == '작사':
#         lll = l.select('a')
#         for ll in lll:
#             lyricistids = ll.get('href')
#             lid = re.findall(pattern, lyricistids)
#             lyricist.append({'type':1, 'aid':lid[0], 'name':ll.text})
#     else:
#         ccc = l.select('a')
#         for cc in ccc:
#             composerids = cc.get('href')
#             cid = re.findall(pattern, composerids)
#             composer.append({'type':2, 'aid':cid[0], 'name':cc.text})