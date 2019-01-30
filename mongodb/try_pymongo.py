import requests
import json
from pymongo import MongoClient, DESCENDING
from pprint import pprint


url = "https://openapi.naver.com/v1/search/book.json"

title = "파이썬"
params = {
    "query": title,
    "display": 100,
    "start": 1,
    "sort": "date"
}

headers = {
    "X-Naver-Client-Id": "XEIkDv0Pg4Q3mxlju6Mx",
    "X-Naver-Client-Secret": "wxJddztfJH"
}

res = requests.get(url, params = params, headers = headers).text

jsonData = json.loads(res)


items = jsonData['items']
for item in items:
    item['price'] = int(item['price'])

# qq = dict((v,k) for k, v in dic.items())
# items['price'] = (int(i['price']) for i in items)
# pprint(items)

# # dic = json.dumps(items, ensure_ascii=False, indent=2)
# # print(dic)
mongo_client = MongoClient('localhost', 27017)
collection = mongo_client.dooodb.Books
collection.delete_many({})
result = collection.insert_many(items)
print('Affeccted docs is {}'.format(len(result.inserted_ids)))

# results = collection.find({"discount":''})
# for result in results:
#     print(result)
lst = collection.find().sort('price', DESCENDING).limit(10)


for idx, l in enumerate(lst):
    print(idx+1, '\n', l)

# item['price'] = (int(i['price']) for i in items)
