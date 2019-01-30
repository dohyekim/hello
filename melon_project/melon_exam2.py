from bs4 import BeautifulSoup
html = '''
    <dl>
        <dt>국적</dt>
        <dd>대한민국</dd>

        <dt>활동장르</dt>
        <dd>Dance, Ballad, Drama</dd>
    
        <dt>데뷔</dt>
        <dd class="debut_song">
            <span class="ellipsis">
                2016.05.05
                <span class="bar">
                    TTT
                </span>
                <a href="#">TTTTTTTTTTTTT</a>
            </span>
        </dd>
        
        <dt>수상이력</dt>
        <dd class="awarded">
            <span class="ellipsis">
                2018 하이원 서울가요대상
                <span class="bar">|</span>본상
            </span>
        </dd>
    </dl>
'''


col_names = {'국적': 'nation', '활동장르': 'genre', '데뷔': 'debut', '수상이력': 'award'}


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
for i in range(len(dt_text)):
    if dt_text[i] in col_names.keys():
        col_names[dt_text[i]] = dd_text[i]
print(col_names)