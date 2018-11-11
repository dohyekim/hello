# Tuple 은 Read Only List
# 즉 메모리를 확정해놓고 가기 때문에 성능이 list에 비해 월등하다
# 우선은 tuple을 고려하고 tuple로 안 되면 list를 고려



# list에서 불러오면 tuple로 나온다.
fruits = ['오렌지', '사과', '바나나']
print(fruits[0], fruits[1])   # 하면 ('오렌지', '사과') 즉 tuple이 된다.

# function을 쓸 때 주로 쓴다. 함수가 return하는 값의 개수가 1개보다 많을 때
q = fruits[0], fruits[2]
print(q)

fruits = ('오렌지', '사과', '바나나')

# 변수도 그 자리에서 tuple로 만들 수 있다.
x, y = 1, 2
(x,y)    
print(x, y)

# Tuple은 read는 가능
fruits[0:2]
b = fruits[0:2]
print(b)

#fruits[1] = 'aaa'   :error)Tuple은 read only list니까 수정 불가

#fruits.append('bbb') 