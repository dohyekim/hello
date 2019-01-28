import melon_function as mf
import tbl_album as album

def songsinger():
    url = "http://vlg.berryservice.net:8099/melon/list"
    sel = "#frm table tbody tr "
    get_song = mf.request(url).select(sel)
   
    # 노래 id와 가수 이름 가져오기
    lst = []

    for i in get_song:
        song_number = i.attrs["data-song-no"]
        singer = i.select_one('div.rank02 span').text
        lst.append([song_number, singer])

    # Singer Table에서 가수별 id와 이름 가져오기
    conn = mf.get_conn('melondb')
    cursor = conn.cursor()
    sql2 = '''select artist_id, name from Singer'''
    cursor.execute(sql2)
    lines = cursor.fetchall()

    # MS_Song에서 가져온 노래 제목과 가수 이름을 비교해서 같은 아티스트의 이름이 있는 가수 id와 노래 id을 append
    data = []
    for i in lst:
        for j in lines:
            if j[1] in i[1] :
                data.append([i[0], j[0]])
                print ("MS_Song===>>",i,"\nSinger====>>>",j)
    return data


