import json

with open("html/eng1.json", encoding='utf-8') as data_file:
   data_loaded = json.load(data_file)
   a = json.loads(data_loaded)
print(a)
print(type(a))
# jjson = json.load("html/eng24.js", encoding='utf-8')
# print(type(jjson))