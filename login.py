import time
from selenium import webdriver



drvPath = 'C:\workspace\chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(drvPath)


driver.get("https://www.naver.com")
time.sleep(1)

driver.find_element_by_class_name('lg_local_btn').click()


driver.execute_script("document.getElementById('id').value='987564';")

driver.execute_script("document.getElementById('pw').value='12354';")


driver.find_element_by_class_name('btn_global').click()

time.sleep(10)              
driver.quit() 

# jQuery를 쓰고 싶으면 ==  (NAVER에서는 불가)
# driver.execute_script( open(‘./jquery.js’).read() )
