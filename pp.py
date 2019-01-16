import requests
from bs4 import BeautifulSoup
import json

url = "https://www.melon.com/chart/index.htm"
headers = {
    'Referer': 'https://www.melon.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
html = requests.get(url, headers = headers).text
soup = BeautifulSoup(html, 'html.parser')

parameter = []
rank_50 = soup.select("table > tbody #lst50")
rank_100 = soup.select("table > tbody #lst100")

for i in rank_50:
    a = i.attrs['data-song-no']
    parameter.append(a)

for j in rank_100:
    b = j.attrs['data-song-no']
    parameter.append(b)
print(parameter)
param_ = ",".join(parameter)
print(param_)