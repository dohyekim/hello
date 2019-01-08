# 날짜 범위를 입력받아 해당 기간의 국내 지진 발생 목록을 다운로드 하시오.
import urllib.request as ur

start_value = input("시작일 >>> usage:2018-01-01 \n")
end_value = input("종료일 >>> usage:2019-01-01 \n")

url = '''http://www.weather.go.kr/weather/earthquake_volcano/domesticlist_download.jsp?startSize=999&endSize=999&pNo=1&startLat=999.0&endLat=999.0
&startLon=999.0&endLon=999.0&lat=999.0&lon=999.0&dist=999.0&keyword=&startTm=''' + start_value + "&endTm=" + end_value

saveFile = "./earthquake_input.html"

ur.urlretrieve(url, saveFile)

with open (saveFile, mode="r") as file:
    for i in file:
        print(i)



