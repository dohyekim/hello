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
dds = soup.select('dl dd')

dttexts = []
ddtexts = []
for dt in dts:
    txt = dt.text
    dttexts.append(txt)
# print(dttexts) # ['국적', 활동장ㄹ, 데뷔, 수상이력]

for dd in dds:
    
    ddtxt = dd.text    
    ddtxt = ddtxt.replace('\n', '')
    ddtxt = ddtxt.strip()


    if 'T' in ddtxt:
        ddtxt = ddtxt.replace('T','')

    if '  ' in ddtxt:
        ddtxt = ddtxt.replace('  ', '')
        # ddtxt = ddtxt.strip()
    
    ddtexts.append(ddtxt)

# print(ddtexts)
for i in range(len(dttexts)):
    col_names[dttexts[i]] = ddtexts[i]
print(col_names)