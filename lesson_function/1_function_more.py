
# 자료구조 : int, float, string, list, tuple, dictionary

# lst와 dic이라고 하는 변수를 잡음

lst = ['orange', 'apple', 'pear']
dic = {'orange': 400, 'apple': 200, 'banana': 300}

# 'orange': 400은 하나의 item
# 'apple': 200, 'banana': 300 각각 다 item

# in 뒤에는 list만 올 수 있지만 dictionary도 올 수 있음. 그 때는 key값을 준다
for key in dic:
    print("key=", key, dic[key])        #dic['orange']  >>> 400

# enumerate

print(enumerate(lst))     #>>> lst의 주소가 나옴

# list로 싸기
print(list(enumerate(lst)))    #>>> tuple이 나온다. # [(0, 'orange'), (1, 'apple'), (2, 'pear')]

# list는 key값이 없기 때문에 index와 그 값이 나온다.
# 활용: for loop을 돌릴 때 i(index)와 value로 찢어질 수 있다.
# i += 1 등의 작업을 할 필요가 없음

for i, value in enumerate(lst):
    print("tt=", i, value)
    print(lst[i])       #index값을 따로 변수로 지정하지 않아도 loop 돌릴 수 있음.

# dictionary는 items()라는 함수를 갖고 있다.
# items()는 '오렌지':400이라는 item을 key와 value로 찢는 것.
# 여기서는 element라는 변수에 value값을 담아냄.

for key, element in dic.items():
    print("items.key=", key, ", element =", element)

    print(dic[key]) #해야 값을 갖고 올 수 있는데key, element로 찢으면 한 번에 가져올 수 있음 (단, items()함수 써야 함)
