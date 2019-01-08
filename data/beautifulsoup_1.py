from bs4 import BeautifulSoup
import requests
url = "https://scontent-scl1-1.cdninstagram.com/vp/589b286cf969b3b6454c4a4dad270c1a/5CD9C7E7/t51.2885-15/e35/41099471_158721315036643_8429270955291504110_n.jpg?_nc_ht=scontent-scl1-1.cdninstagram.com"

img = requests.get(url).content

saveFile = "./images/moon.jpg"
with open(saveFile, mode="wb") as file:
    file.write(img)

print("ok")
