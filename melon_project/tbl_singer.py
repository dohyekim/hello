import melon_function as mf
import re

# Singer Table에 들어갈 data(가수 id, 가수 이름)을 가져오는 함수

def singer():
    url = "http://vlg.berryservice.net:8099/melon/list"
    singers = mf.request(url).select('tbody tr[data-song-no]')
    singer_info = []
    for singer in singers:
        singer_links = singer.select('td:nth-of-type(6) div.ellipsis.rank02 span a')
        for singer_link in singer_links:
            singer_name = singer_link.text
            singer_ids = singer_link.attrs['href']
            pattern = re.compile("\'(.*)\'")
            singer_id = re.findall(pattern, singer_ids)[0] 
            singer_info.append([singer_id, singer_name])
    return singer_info

