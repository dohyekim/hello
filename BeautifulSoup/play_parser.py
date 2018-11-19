from bs4 import BeautifulSoup
import requests


class Game:
    def __init__(self, tag): # 여기 tag 자리에 card 하나가 들어온다.
        self.title = self.get_text(tag, 'a title')   # <-- title = c.select('a.title')[0].text.strip() 
        self.title = self.get_text
        self.comp = c.select('a.subtitle')[0].get('title')

    def get_text(self, parent_tag, selector):
        t = self.get_tag(parent_tag, selector)
        if t == None:
           return ""
        else:
            return t.text.strip()
        # return "" if t == None else t.text.strip    

    def get_tag(self, parent_tag, selector):      #parent_tag 는 caardd tag #selector = a.title
        return parent_tag.select(selector)
        


url = "https://play.google.com/store/apps/category/GAME/collection/topselling_paid"
res = requests.get(url)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
card_list = soup.select('div.card-list')         # list형태
# print(card_list)

print(">>>>>>>>>", type(card_list), type(card_list[0]))  # card_list[0] -> tag

for i in card_list:
    
    cards = i.select('.card')    # div.card로 써도 가능
    
    print("LLL>>", len(cards))
   
    for c in cards:
       
        title = c.select('a.title')[0].text.strip()
       
        # comp = c.select('a.subtitle')[0].text
       
        comp = c.select('a.subtitle')[0].get('title')
       
        print(">>", c.get('class'), [title, comp])