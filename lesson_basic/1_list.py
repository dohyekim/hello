si, sf = "3", "3.5"
print(float(sf))
print(float(si))

#number를 str으로 바꾸고 싶을 때
str(23)
print(type(23))

#List
fruits = ['오렌지', '사과', '바나나']
print(fruits[1])
print(fruits[0:2])
print(fruits[-1])

prices = [300, 400, 500]
print([fruits[1], prices[1]])

things = ['오렌지', 90, '바나나', 30]

items = fruits + prices
print(items)

# 1차원 List
[fruits[1], prices[2]]
print([fruits[1], prices[2]])

# 2차원 array
[fruits, prices]
print([fruits, prices])

# append, extend, insert

# 하나를 추가하고 싶을 때(append)     -append한 순간 스스로 메모리 확보
fruits.append('체리')
print(fruits.append('체리'))

# 여러 개를 추가하고 싶을 때(extend)    - extend한 순간 스스로 메모리 확보 / 그러나 fruits 자체는 변하지 않음.
fruits.extend(['체리','귤','멜론'])
print(fruits.extend(['체리','귤','멜론']))

fruits.extend(things)
print(fruits.extend(things))

fruits.insert(1, '청포도')
print(fruits.insert(1, '청포도'))

# del, push, pop
del fruits[1]
print(fruits)

fruits.pop(1)
print(fruits.pop(1))

# a = del.fruits[1]           #del과 pop의 차이 : del은 아무 값도 리턴하지 않아서 이렇게 쓰면 error난다.
a = fruits.pop(1)

# remove : 내가 지우고자 하는 게 몇 번째 index인지 모를 경우에 쓸 수 있다.
fruits = ['오렌지', '체리', '딸기', '배']
fruits.remove('딸기')
print(fruits)

# clear
fruits.clear()
print(fruits)          #[] 나옴. memory의 주소는 잃어버린 상태가 아니기 때문에 null이 나오지는 않는다.

# in / not in 이게 있냐 ? 없냐 ?
fruits = ['딸기', '사과', '귤']  
print("has 사과", "사과" in fruits)


# len()
items = fruits + prices
len(items[0])
len(items)         # 2차원 array이기 때문에 2라고 나옴.

print(len(items[0]))
print(len(items))
