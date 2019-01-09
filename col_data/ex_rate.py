from bs4 import BeautifulSoup
import requests
import urlss

# 각 국가의 매매기준율

url = "https://finance.naver.com/marketindex/"

ifr_html = requests.get(url).text
ifr_soup = BeautifulSoup(ifr_html, 'html.parser')
ifr = ifr_soup.select_one('iframe#frame_ex1')
ifr_src = ifr.get('src')

# url 만들기
host = urlss.getHostname(url, True)
ifr_url = urlss.urljoin(host,ifr_src)

# print(ifr_url)

html = requests.get(ifr_url).text
soup = BeautifulSoup(html, 'html.parser')

all_tr = soup.select('tr')
# print(len(all_tr))

# Answer

def toFloat(s):
    return float(s.text.strip().replace(',',''))


for tr in all_tr:
    tds = tr.select('td')
    if (len(tds) < 4):
        continue
    title = tds [0]
    rate = tds [1]
    buy = tds [2]
    sell = tds [3]
    diff = toFloat(buy) - toFloat(sell)
    print("{}, {}. {}".format(title.text.strip(), rate.text, diff))

# 나

for i in range(1,len(all_tr) - 1):
    tr = 'tr:nth-of-type({})'.format(i)
    country = soup.select_one('tbody > ' + tr + ' > td.tit').text
    ex_rate = soup.select_one('tbody > ' + tr + ' > td.sale').text
    ex_buy = soup.select_one('tbody > ' + tr + ' > td:nth-of-type(3)').text
    ex_buy_float = float(ex_buy.replace(',',''))
    ex_sell = soup.select_one('tbody > ' + tr + ' > td:nth-of-type(4)').text
    ex_sell_float = float(ex_sell.replace(',',''))
    print(country.strip(), ", " , ex_rate, ", ", "{:.02f}".format((ex_buy_float - ex_sell_float)))
    