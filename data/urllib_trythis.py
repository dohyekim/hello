import urllib.request as ur

url = "http://www.weather.go.kr/weather/earthquake_volcano/domesticlist_download.jsp?startSize=999&endSize=999&pNo=1&startLat=999.0&endLat=999.0&startLon=999.0&endLon=999.0&lat=999.0&lon=999.0&dist=999.0&keyword=&startTm=2018-01-08&endTm=2019-01-08"


saveFile = "./earthquake.html"


ur.urlretrieve(url, saveFile)

# mem = ur.urlopen(url).read()

# with open(saveFile, mode = "w") as file:
#     file.write(mem)


with open(saveFile, mode="r") as file:
    for i in file:
        print(i)