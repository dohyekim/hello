import openpyxl
from PIL import Image
import requests
import urllib.request as ur
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {
    'Referer': 'https://www.melon.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
html = requests.get(url, headers = headers).text
soup = BeautifulSoup(html, 'html.parser')
song_lsts = soup.select('div#tb_list table tbody tr[data-song-no]')


load_book = openpyxl.load_workbook("./meltop100.xlsx")
sheet2 = load_book.create_sheet()
sheet2.title = "Sheet 2"

n = 1
for song in song_lsts:
    src = song.select_one('td:nth-of-type(4) div.wrap a img[src]').text
    rank = song.select_one('td:nth-of-type(2) div.wrap.t_center span.rank').text
    src = song.select_one('td:nth-of-type(4) div.wrap a img[src]').attrs['src']
    saveFile = "./images/rank{}.png".format(rank)
    ur.urlretrieve(src, saveFile)
    img = Image.open(saveFile)
    resized_img = img.resize((139, 139))
    resized_img.save('new_rank{}.png'.format(rank))
    final_img = openpyxl.drawing.image.Image('new_rank{}.png'.format(rank))
    if n == 1:
        sheet2.add_image(final_img, 'A{}'.format(n))
        load_book.save("./meltop100.xlsx")
    else:
        sheet2.add_image(final_img, 'A{}'.format(n))
        load_book.save("./meltop100.xlsx")
    n = n + 7