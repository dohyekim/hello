import requests
import melon_function as mf
import tbl_album as album
import datetime

# 매일 update되는 Song_Rank Table에 들어갈 data를 가져오는 함수

def song_rank():
    now = datetime.datetime.now()

    likecnt = []
    song_no = []
    rank = []
    lst = []

    b = 0
    url = "http://vlg.berryservice.net:8099/melon/list"
    top_list = mf.request(url)
    sel = "#frm table tbody tr "

    # song id, rank 가져오기
    get_song = top_list.select(sel)
    for i in get_song:
        song_number = i.attrs["data-song-no"]
        song_no.append(song_number)
        rank.append(i.select_one('div span.rank').text)
        

    url2 = "http://vlg.berryservice.net:8099/melon/likejson"
    jsonData = mf.requestJson(url2)

    # 좋아요
    for j in jsonData['contsLike']:
        if str(j['CONTSID']) == str((song_no)[b]):
            likecnt.append(j['SUMMCNT'])
            b = b+1
        
    
    # update 일자
    update_date = now.strftime('%Y%m%d')

    # data 모으기
    for i in range (0,100):
        lst.append([song_no[i], rank[i], update_date, likecnt[i]])
        print("Rank_lst ----->", (i + 1) , "record  --> done!")
    
    print ("Ranking has been downloaded!!!!")
        
    return (lst)

