from pprint import pprint
from bs4 import BeautifulSoup

html = '''
    <dl class="info_02 clfix">
        <dt>국적</dt>
        <dd>대한민국</dd>

        <dt>활동유형</dt>
        <dd>여성, 솔로</dd>

        <dt>활동년대</dt>
        <dd>2010</dd>
        
        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
            </span>
        </dd>
        
        <dt>생일</dt>
        <dd>1996.02.09</dd>
    </dl>
    '''

# "데뷔, 소속사, 국적, 활동유형, 활동연대, 활동장르"


col_names = {'국적': 'nation', '활동유형': 'act_type', '활동연대': 'act_year', '활동장르': 'act_genre', '데뷔': 'debut', '생일': 'birth'}


soup = BeautifulSoup(html, 'html.parser')
dts = soup.select('dl dt')
dt_text = []
for dt in dts:
    dt_text.append(dt.text)
dds = soup.select('dl dd')
dd_text = []
for dd in dds:
    spans = dd.select('span')
    if spans != None:
        for span in spans:
            dd = span
    dd_text.append((dd.text).strip())
print(dd_text)
#         dd = span
#     # print(dd)
#     # else:
#     # print((dd.text).strip())
#     dd_text.append((dd.text).strip())
# # print(dd_text)
for i in range(len(dt_text)):
    if dt_text[i] in col_names.keys():
        col_names[dt_text[i]] = dd_text[i]
# print(col_names)        
print(col_names)