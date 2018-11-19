# 플레이스토어 유료 게임 랭킹 60위 까지 게임의,
#   - 게임명
#   - 제조사
#   - 평점
#   - 가격
#   - 대표 아이콘 이미지 경로
# 를 스크래핑해서 csv 파일로 저장하시오.

from bs4 import BeautifulSoup
import requests

url = "https://play.google.com/store/apps/category/GAME/collection/topselling_paid"
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')