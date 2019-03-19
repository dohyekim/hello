from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from pprint import pprint

drvPath = 'C:\workspace\chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(drvPath)




USER = ""
PASS = ""

# driver = webdriver.Chrome()
# driver.implicitly_wait(3)

url = "https://ticket.melon.com/performance/index.htm?prodId=203038"
driver.get(url)

driver.find_element_by_xpath('//*[@id="list_date"]/li[1]/button/span').click()
driver.find_element_by_xpath('//*[@id="ticketing_process_box"]/div/div[2]/div/div[2]/button').click()

driver.switch_to.window(driver.window_handles[1])

i = driver.find_element_by_xpath('//*[@id="id"]')
i.clear()
i.send_keys(USER)
i = driver.find_element_by_xpath('//*[@id="pwd"]')
i.clear()
i.send_keys(PASS)

driver.find_element_by_id('IMG_POP_LOGIN').click()

# driver.find_element_by_xpath('//*[@id="IMG_POP_LOGIN"]').click()
print('111')
driver.switch_to.window(driver.window_handles[0])
print('222')

driver.find_element_by_xpath('//*[@id="list_date"]/li[1]/button/span').click()
print("date")
driver.find_element_by_xpath('//*[@id="list_time"]/li/button/span').click()
print("time")



driver.find_element_by_xpath('//*[@id="ticketing_process_box"]/div/div[2]/div/div[2]/button').click()

standa = driver.find_element_by_xpath('//*[@id="gd10032"]/td[4]')
if standa:
    standa.click()

# ul = soup.select_one('tbody tr.box_list_area').text
# for li in ul:
#     if '0' in ul.select_one('li10032FloorA').text:
#         continue
#     else: 

standb = driver.find_element_by_xpath('//*[@id="gd10365"]/td[4]')
if standb:
    standb.click()

standc = driver.find_element_by_xpath('//*[@id="gd10366"]/td[4]')
if standc:
    standc.click()


# <li id="li103651B2" onclick="selectedBlock(this,'65','1,B2','1','층','B2','구역','SE0001');" onmouseover="viewGradeZone('1,B2')" onmouseout="viewLastGradeZone()" class="ck"><span class="area_tit">1 층 B2 구역</span><span class="seat_residual"> <strong>1</strong>석</span></li>

#<rect x="731.91" y="1105.75" width="11" height="11" rx="0" ry="0" fill="#9486f8" stroke="#000" stroke-width="0" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></rect>

# 좌석 선택 완료 버튼
driver.find_element_by_xpath('//*[@id="nextTicketSelection"]').click()

# 다음
driver.find_element_by_xpath('//*[@id="nextPayment"]').click()

#주문자 정보와 동일
driver.find_element_by_xpath('//*[@id="copyDelvyAddr"]').click

#우편 번호
driver.find_element_by_xpath('//*[@id="btnSearchAddress"]').click

#화면 전환
driver.switch_to.window(driver.window_handles[1])

# 찾아서 입력하기
'//*[@id="searchWord1"]'

#검색
driver.find_element_by_xpath('//*[@id="searchAddressPopup"]/div[2]/div/div/div[1]/div/button').click