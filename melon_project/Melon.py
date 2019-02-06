# 앨범상세(좋아요) JSON: http://vlg.berryservice.net:8099/melon/albumlikejson?albumId=10123639
# 노래상세 http://vlg.berryservice.net:8099/melon/songdetail?songId=31532643
# top100의 좋아요 수 json: http://vlg.berryservice.net:8099/melon/likejson
# 앨범상세(평점) json:  http://vlg.berryservice.net:8099/melon/albumratejson?albumId=10123639 
# 일간 탑100 목록 주소: http://vlg.berryservice.net:8099/melon/list 

import requests
from bs4 import BeautifulSoup
import json
import re

def request(url, headers={}):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup        

def requestJson(url, headers={}, params={}):
    rjson = requests.get(url).text
    jsonData = json.loads(rjson, encoding = "utf-8")
    return jsonData

url = "http://vlg.berryservice.net:8099/melon/list"
class Melon:
    songnos = []
    meltops = {}
    album_id = []
    albums = {}
    artists = []
    songs = {}
    songArtists = {}
    # 생성시 데이터 가져오기
    def __init__(self):
        pattern = re.compile("\'(.*)\'")
        headers = {
            'Referer': 'https://www.melon.com/index.htm',
            'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }

        soup = request(url, headers = headers)
        # resp = requests.get(url, headers = headers)
        # resp.encoding = 'utf-8'
        # html = resp.text
        # soup = BeautifulSoup(html, 'html.parser')

        trs = soup.select('tbody tr[data-song-no]')
        for tr in trs:
            rank = tr.select_one('td:nth-of-type(2) div span.rank').text
            # album id, title 가져와서 json에 담기
            albumids = tr.select_one('td:nth-of-type(7) div.wrap div.wrap_song_info a')
            albumtitle = albumids.text
        
            string = albumids.attrs['href']
            albumid = re.findall(pattern, string)
            self.album_id.append(albumid[0])
            self.albums[int(albumid[0])] = {'title' : albumtitle}

            songno = tr.get('data-song-no')
            self.songnos.append(songno)
            title = tr.select_one('td:nth-of-type(6) div.ellipsis.rank01 span a').text
            singers = tr.select('td:nth-of-type(6) div.ellipsis.rank02 a')
            for singer in singers:
                s = singer.attrs['href']
                singerno = re.findall(pattern, s)
                singerdic = {'name' : singer.text, 'artistid' : int(singerno[0]), 'type' : 3}
                self.artists.append(singerdic)
                self.albums[int(albumid[0])]['singer'] = int(singerno[0])                
            self.meltops[int(songno)] = {
                'rank' : rank,
                'title': title,
                'artist' : self.artists,
                'album' : int(albumid[0])
            }
        
    def songdetail(self):
        return
    def album(self):
        # print(self.album_id)
        # print(self.albums[self.album_id[0]])
        # exit
        for a in self.album_id:
            albumrateurl = "http://vlg.berryservice.net:8099/melon/albumratejson?albumId={}".format(a)
            albumdetailurl = "http://vlg.berryservice.net:8099/melon/detail?albumId={}".format(a)
            jsonheaders = {
                'Referer' : 'https://www.melon.com/album/detail.htm?albumId=10245121',
                'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
            }
            jsonData = requestJson(albumrateurl, headers = jsonheaders)
            
            # album 평점
            albumrating = jsonData['infoGrade']['TOTAVRGSCORE']
            # print(albumrating)

            # 발매일, 발매사, 기획사
            soup = request(albumdetailurl)
            sel = soup.select_one('div.entry div.meta dl.list')
            releasedt = sel.select_one('dd:nth-of-type(1)').text
            company = sel.select_one('dd:nth-of-type(3)').text
            entertainment = sel.select_one('dd:nth-of-type(4)').text

            # if self.albums[a] == None:
            #     print(self.albums[a]['title']) 
            self.albums[int(a)]['releasedate'] = releasedt
            self.albums[int(a)]['company'] = company
            self.albums[int(a)]['entertainment'] = entertainment
            self.albums[int(a)]['rating'] = albumrating
        print(self.albums)

        return
    def artist(self):
        return
    def song(self):
        return 
    def songArtist(self):
        return

if __name__ == '__main__':
    melon = Melon()
    melon.album()