import os
import json
import requests

# with open("html/eng1.json", encoding='utf-8') as data_file:
#    data_loaded = json.load(data_file)
#    a = json.loads(data_loaded)
# print(a)
# print(type(a))
# # jjson = json.load("html/eng24.js", encoding='utf-8')
# # print(type(jjson))

# if os.path.exists("html/" + 'ko' + str(6) + ".json"):
#    print("html/" + 'ko' + str(6) + ".json")
#    with open("html/" + 'ko' + str(6) + ".json", encoding='utf-8') as kjson:
#          jjson = json.load(kjson)
#          print(type(jjson))
         
         
         # jjson = json.loads(prejson)
         # print(type(jjson))

# url = 'https://www.ted.com/talks/' + str(5) + '/transcript.json?language=' + 'en'
# stat_json = requests.get(url)
# # jjson = stat_json.text
# jjson = stat_json.json()
# print(type(jjson))
<<<<<<< HEAD


# with open("chart", "w", encoding="utf-8") as chartfile:
#     chartfile.write("D1 ,K1 ,E1  ,\n")

url = 'https://www.ted.com/talks/24/transcript.json?language=en'
stat_json = requests.get(url)
print(stat_json)
print(stat_json.status_code)
=======
# with open("chart", "w", encoding="utf-8") as chartfile:
#     chartfile.write("D1, \n")
# for k in range(2,190):
#     with open("chart", "a", encoding="utf-8") as chartfile:
#         chartfile.write("D{} \n".format(k))
# strs = ''
# a = ['a', 'b', 'c', 'd']
# for i in a:
#     strs += (i + ' ')

# print(strs)

a = 'Thank you'
print(a[1:])
s = a[0]
print(s.lower())
print(s.upper())
>>>>>>> 97e557429b08ffdb80f9227f2de91259c4e30523
