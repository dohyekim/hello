# Dictionary (key와 value의 쌍, HashMap, JSON)

# list와 다른점 : list는 key가 없었기 떄문에 remove 등을 할 때 index(즉 value)값을 넣었어야 한다
# 'a'(key)를 주세요 하면 value값이 나온다. key = label이라고 봐도 됨.

#dictionary는 {} 사용

fruits = {'오렌지': 400, '사과': 200, '바나나': 300}

# key 내오기
fruits.keys()
print(fruits.keys())

# value 내오기
fruits.values()
print(fruits.values())

# fruits에 key를 주면 value값을 토해냄.
fruits['바나나']

'바나나' in fruits
print('바나나' in fruits)

# in은 key에서만 찾음. 메모리에는 key들로만 구성되고 긴 값(value)은 다른 곳에 있기 때문!
200 in fruits      # False
print(200 in fruits )

