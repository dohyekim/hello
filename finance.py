import requests
from bs4 import BeautifulSoup
import urllib.parse as parse

url = "https://finance.naver.com/marketindex/"

ifr_html = requests.get(url).text
ifr_soup = BeautifulSoup(ifr_html, 'html.parser')
ifr = ifr_soup.select_one('iframe#frame_ex1')
ifr_src = ifr.get('src')

def getHostname(url, withProtocol = False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def urljoin(url, p):
    return parse.urljoin(url, p)

# url 만들기
host = getHostname(url, True)
ifr_url = urljoin(host,ifr_src)

# print(ifr_url)

html = requests.get(ifr_url).text
soup = BeautifulSoup(html, 'html.parser')
infos = soup.select_one('div.data div.head_info.point_up')
value = infos.select_one('span.value').text
won = infos.select_one('span.txt_krw span.bline').text
change = infos.select_one('span.txt_krw span.change').text
ups = infos.select_one('span.txt_krw span.blind').text

print(value, won, change, ups)