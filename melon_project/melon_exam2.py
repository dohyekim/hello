from bs4 import BeautifulSoup
html = '''
<dl class="atist_info clfix">
    <dt>데뷔</dt>
    <dd>
        <span class="gubun">2015.05.29</span>
        <a href="javascript:;" onclick="javascript:melon.play.playSong('27120101',5712573);" title="아낀다 재생" class="btn_play_song">
            <span class="icon_play">곡재생</span>
            <span class="songname12">아낀다</span>
        </a>
    </dd>
    <dt>활동유형</dt>
    <dd>
        <span>그룹</span>
        <span>AOI</span>
    </dd>
    
    <dt>소속사</dt>
    <dd>플레디스 엔터테인먼트</dd>
    
    <dt>수상이력</dt>
    <dd class="awarded">
        <span class="ellipsis">
            2018 하이원 서울가요대상
            <span class="bar">|</span>본상
        </span>
        <a href="javascript:melon.link.goArtistDetail('861436', '2');" title="세븐틴 상세정보 더보기" class="btn_text arrow_r">
            <span class="text">더보기</span>
            <span class="icon"></span>
        </a>
    </dd>
</dl>
'''

col_names = {'국적': 'nation', '활동유형': 'act_type', '활동연대': 'act_year', '활동장르': 'act_genre', '데뷔': 'debut', '생일': 'birth'}

dic = {}
soup = BeautifulSoup(html, 'html.parser')
dts = soup.select('dl dt')
dt_text = []
for dt in dts:
    dt_text.append(dt.text)
dds = soup.select('dl dd')
dd_text = []
for dd in dds:
    span = dd.select_one('span')
    if span != None:
        dd = span.text
        print(dd)
    print(dd)        
    # dd_text.append((dd.text))
# print(dd_text)
#         dd = span
#     # print(dd)
#     # else:
#     # print((dd.text).strip())
#     dd_text.append((dd.text).strip())
# # print(dd_text)
for i in range(len(dt_text)):
    # dic[dt_text[i]] = dd_text[i]
    if dt_text[i] in col_names.keys():
        col_names[dt_text[i]] = dd_text[i]
    elif dt_text[i] not in col_names.keys():
        col_names[dt_text[i]] = dd_text[i]
print(col_names)        
# print(dic)