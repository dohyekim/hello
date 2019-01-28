
import re
import melon_function as mf

# MS_Song(Master Table)에 들어갈 data를 가져오는 함수
def song_data():
    # header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url = "http://vlg.berryservice.net:8099/melon/list"
    
    sel_song = "#frm table tbody tr "
   
    get_song = mf.request(url).select(sel_song)
   

    album_ids = []
    song_no = []
    song_name = []
    singer = []
    genre = []
    lst = []
    
    # index page에서 노래 id와 노래 제목, 앨범 id 가져오기   
    for i in get_song:
        song_number = i.attrs["data-song-no"]
        song_no.append(song_number)
        song_name.append((i.select_one('div.rank01 span a').text))
        singer.append(i.select_one('div.rank02 span').text)
        album_id_strings = i.select_one('div.ellipsis.rank03 a').attrs['href']
        pattern = re.compile("\'(.*)\'")
        album_id = re.findall(pattern, album_id_strings)[0]
        album_ids.append(album_id)
        
    # 곡 상세 페이지에서 장르 가져오기
    for num, song_num in enumerate(song_no):
        url2 = "http://vlg.berryservice.net:8099/melon/songdetail?songId=" + song_num
      
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        # params =  {'contsIds': ",".join(song_no)}
        
        song_data = "#downloadfrm div.wrap_info div.entry div.meta"
        get_data = mf.request(url2).select(song_data)
       
        # 위에서 받은 노래 id, 노래 이름, 앨범 id와 2번째 for loop에서 받아온 장르 담기
        for i in get_data:
            genre.append(i.select_one('dl.list dd:nth-of-type(3)').text)
            lst.append([song_no[num],song_name[num],genre[num],album_ids[num]])
            print('Song ----->', (num+1), 'record  --> done!')
    print ("Finished Crawling Songs!!!!!")        
    
    return lst
