import pymysql
import requests
from bs4 import BeautifulSoup
import time
import re
import json 

# ------------------------------------------------------------------MySQL 함수 -----------------------------------------------------------------
# Mysql connection 함수
def get_conn(db):
   return pymysql.connect(
       host='35.243.112.23',
       user='root',
       password='eileen',
       port=3306,
       db=db,
       charset='utf8')

# Mysql save 함수
def save(lst, sql_insert):
    try:
        conn = get_conn('melondb')
        conn.autocommit = False
        cur = conn.cursor()
       
        cur.executemany(sql_insert, lst)
        print("Affected RowCount is", cur.rowcount, "/", len(lst))
        conn.commit()

    except Exception as err:
        conn.rollback()
        print("Error!!", err)

    finally:
        try:
            cur.close()
        except:
            print("Error on close cursor")
        try:
            conn.close()
            print ("OOKKKK")
        except Exception as err2:
            print("Fail to connect!!", err2)

# ----------------------------------------------------------------------------------------------------------------------------------------
# Requests 함수
def request(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def requestJson(url):
    rjson = requests.get(url).text
    jsonData = json.loads(rjson, encoding = "utf-8")
    return jsonData

