import melon_function as mf
import requests
import re


url = "http://vlg.berryservice.net:8099/melon/list"
# headers = {
#     'Referer': 'https://www.melon.com/',
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# }
trs = mf.request(url).select('tbody tr[data-song-no]')


def album_data ():
    
    url = "http://vlg.berryservice.net:8099/melon/list"
    trs = mf.request(url).select('tbody tr[data-song-no]')

    album_data = []
    b = 0
    for tr in trs:
        album_json = tr.select('td:nth-of-type(4) a')
        album_title = tr.select_one('div.ellipsis.rank03 a').text
        
        # album id 가져오기
        for j in album_json:
            strings = j.attrs['href']
            pattern = re.compile("\'(.*)\'")
            album_id = re.findall(pattern, strings)
            
            # album 상세 페이지
            album_url = "http://vlg.berryservice.net:8099/melon/detail?albumId={}".format(album_id[0])
            # headers = {
            #     'Referer': 'https://www.melon.com/album/detail.htm?albumId={}'.format(album_id[0]),
            #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
            # }

            # album 평점 json
            json_url = " http://vlg.berryservice.net:8099/melon/albumratejson?albumId={}".format(album_id[0])

            # album의 id, title, genre, 발매일, 발매사, 기획사 가져오기
            divs = mf.request(album_url).select_one('div.entry')
            dls = divs.select('div.meta dl.list')
            for dl in dls:
                releasedt = dl.select_one('dd:nth-of-type(1)').text
                album_genre = dl.select_one('dd:nth-of-type(2)').text
                album_comp = dl.select_one('dd:nth-of-type(3)').text
                entertainment = dl.select_one('dd:nth-of-type(4)').text
                b += 1

            # album의 평점 가져오기
            jsonData = mf.requestJson(json_url)
            rating = jsonData['infoGrade']['TOTAVRGSCORE']

            # 모든 column의 data 모으기
            album_data.append([album_id[0], album_title, album_genre, "{:.02f}".format(float(rating)) , releasedt, album_comp, entertainment])
            print("Album ----->", b , "record  --> done!")
    print ("Album_data has been downloaded!!!!")
    return (album_data)


