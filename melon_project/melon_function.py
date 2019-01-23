import requests
from bs4 import BeautifulSoup
import time
# crawling 함수

def request(url, param_header, argv={}):
    # url = param_url
    html = requests.get(url,  headers = param_header, params = argv).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def song_data():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url = "https://www.melon.com/chart/index.htm"
    
    sel_song = "#frm table tbody tr "
   
    get_song = request(url, header).select(sel_song)
   
    album_name = []
    song_no = []
    song_name = []
    singer = []
    
    genre = []
    lst = []
    
    
    
    for i in get_song:
        song_number = i.attrs["data-song-no"]
        song_no.append(song_number)
        song_name.append((i.select_one('div.rank01 span a').text))
        singer.append(i.select_one('div.rank02 span').text)
        album_name.append(i.select_one('div.ellipsis.rank03 a').text)
        

    for num, song_num in enumerate(song_no):
        url2 = "https://www.melon.com/song/detail.htm?songId=" + song_num
      
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        params =  {'contsIds': ",".join(song_no)}
        
        song_data = "#downloadfrm div.wrap_info div.entry div.meta"
        get_data = request(url2, headers, params).select(song_data)
       
        
        for i in get_data:
            genre.append(i.select_one('dl.list dd:nth-of-type(3)').text)
            lst.append([song_no[num],song_name[num],singer[num],genre[num],album_name[num]])
    
    print ("Finished Crawling Songs!!!!!")        
    return (lst)

## MySql 함수

import pymysql
from bs4 import BeautifulSoup
import requests
import time


def get_conn(db):
   return pymysql.connect(
       host='35.243.112.23',
       user='root',
       password='eileen',
       port=3306,
       db=db,
       charset='utf8')

# sql_truncate = "truncate table Meltop"



def save(lst, sql_insert):
    try:
        conn = get_conn('melondb')
        conn.autocommit = False
        cur = conn.cursor()
       
        cur.executemany(sql_insert, lst)
        print("Affected RowCount is", cur.rowcount, "/", len(lst))
        conn.commit()

    except Exception as err:
        conn.rollback()
        print("Error!!", err)

    finally:
        try:
            cur.close()
        except:
            print("Error on close cursor")
        try:
            conn.close()
            print ("OOKKKK")
        except Exception as err2:
            print("Fail to connect!!", err2)
