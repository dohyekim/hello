from bs4 import BeautifulSoup
import requests
import time
import random
import json
import melon_function as mf




    
# 쿼리
sql_insert = "insert into Meltop (song_no, title, singer, song_genre, album_name) values (%s, %s, %s, %s, %s) "
isStart = True



songs = mf.crawl_data()
mf.save(songs)



