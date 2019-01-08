from bs4 import BeautifulSoup
import requests
import urllib.parse as parse
import os.path as path

def getFileName(url) :
    p = parse.urlparse(url).path
    return path.basename(p)

url = '''https://blog.naver.com/PostView.nhn?blogId=korea_diary&logNo=221433346994&redirect=Dlog&widgetTypeCall=true&directAccess=false'''
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')


sel = "img.se-image-resource"

image = soup.select(sel)
print("image>>", image)

print(len(image))

for i in range(0, len(image)):
    img = image[i]
    src = img.get('src')
    print("-----------------------------------------------\n", src)
    content = requests.get(src).content
    saveFile = "./images/" + getFileName(src)
    with open(saveFile, mode = "wb") as file:
        file.write(content)

