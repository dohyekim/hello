import melon_function as mf
import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://www.melon.com/chart/index.htm"
headers = {
    'Referer': 'https://www.melon.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
trs = mf.request(url, headers).select('tbody tr[data-song-no]')



album_data = []
for tr in trs:
    album_json = tr.select('td:nth-of-type(4) a')
    for j in album_json:
        strings = j.attrs['href']
        pattern = re.compile("\'(.*)\'")
        album_id = re.findall(pattern, strings)

        album_url = "https://www.melon.com/album/detail.htm?albumId={}".format(album_id[0])
        headers = {
            'Referer': 'https://www.melon.com/album/detail.htm?albumId={}'.format(album_id[0]),
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }


        json_url = "https://www.melon.com/album/albumGradeInfo.json?albumId={}".format(album_id[0])
        json_params = {
            'albumid' : album_id[0]
        }

        divs = mf.request(album_url, headers).select_one('div.entry')
        dls = divs.select('div.meta dl.list')
        for dl in dls:
            releasedt = dl.select_one('dd:nth-of-type(1)').text
            album_genre = dl.select_one('dd:nth-of-type(2)').text
            album_comp = dl.select_one('dd:nth-of-type(3)').text
            entertainment = dl.select_one('dd:nth-of-type(4)').text


        rating_json = requests.get(json_url, params = json_params, headers = headers).text
        jsonData = json.loads(rating_json, encoding = "utf-8")
        rating = jsonData['infoGrade']['TOTAVRGSCORE']
        album_data.append([album_id[0], album_genre, rating, releasedt, album_comp, entertainment])
       

print(album_data)