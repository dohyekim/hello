
import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/apps/category/..."          # 주소를 변수화
res = requests.get(url)                #url을 갖고온다. #res에는 html, header, cookie등이 다 들어있다.
soup = BeautifulSoup(res.text, 'html.parser')       #soup은 객체, BeautifulSoup이 클래스 #parser해서 나온 값

# res.text는 html, __init(self, text, parser) text에 html을 주면 html.parser
# Parser라는 class, Html Parser(Parser)

card_list = soup.select('div.card-list') #soup에서 div.card-list를 골라낸다. <div class="----"에서 <를 tag, div를 element라고 한다. class를 attribute라고 한다. 
# 이 attribute를 가져오는 명령어가 get
# XML = extensive(확장 가능한) markup language
# html = hyper text markup language
# div tag에서 card-list를 찾아낸다.
# soup이라는 클래스 안의 select라는 함수를 불러내서 div.card-list로 시작되는 것들을 찾아낸다.

# html.parser의 종류는 2가지(DOM - SAX)
# DOM: 전부 다 로드 -> 찾을 때 더 빠름. SAX: (화면에 띄울 수 있는) 필요한 것만 로드 -> card-list를 먼저 찾고 거기서부터 card를 찾는다.

print(">>>>>>>>>", card_list[0].get('class'))
for i in card_list: # card_list에서
    cards = i.select('.card')   # card붙은 것만 <div class="card"인 것들만 찾는다.
    print(len(cards))                       # card가 몇 개인지
    for c in cards:  # card(60개)의 loop를 돈다.
        print(">>", c.get('class'), c.select('a.title')[0].text)   # a tag(<a)에서 class=title있는 걸 찾아낸다. #c.select('a.title')[0].text -> 제목 긁어온 것
        #<a 는 link로 이동시키는 tag
#c.select('a.title')[0] = tag

 # type(card_list[0]) = bs4.element.Tag
 # type(card_lsit) = list