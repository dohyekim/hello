# list를 변환할 때 반복을 적용할 수 있는 요소만 list로 변화하도록 했는데
# 이때 반복 적용할 수 있는 요소를 iterable이라고 하며
# iterable의 종류로는 string, list, dictionary, range, set

list(), set(), tuple(), enumerate()

# set() 집합구조로 바꾸는 것

min(), max()


l = [1,2,3]
sum(l)
sum(l,10)  #기존값에 10을 더한다. # sum(iter, start_value)

# math.fsum(l)로 쓸 수 있음.

all(iter), any(iter)

ll = [False, True, False]
lll = [False, False, False]
llll = [True, True, True, True]

all(ll)            # all(iter) 모든 게 True다

any(lll)           # 하나라도 True다

l.append(0)          #0은 False
all(l)               #False
any(l)               #True

l.pop(3)             #3번째 있는 0을 뺌
all(l)               #True


#iter()

l = [1,2,3] # type(l) = str
iter(l) #>>> 객체로 바뀐다 -> 주소값이 나온다. l이 iter화된 것 -> next()와 같은 함수를 쓸 수 있다.
it = iter(l) #type(it) = iterator # iterator화 하는 과정 필수!!

next(it)         # 1
next(it)         # 2
next(it)         # 3 
#인덱스를 모르겠는데 하나씩 꺼내고 싶을 때

next(it, after_last) # next(it) vs next(iter(t))

t = (1,2,3,4,5)
it5=iter(t)             # tuple이 iterator가 됨 -> 즉 next를 부를 수 있음.
next(it5)               # >>>1
next(it5)               # >>>2
next(it5)               # >>>3
next(it5)               # >>>4
next(it5)               # >>>5

it6 = iter(t)
next(it6, None)         # >>>1,2,3,4,5,' '(None)

list(it6)
next(it6,1)            #>>>반복해서 출력해도 1

it8 = iter(t)
next(it8, 1)  #1        #1,2,3,4,5 다 나온 후에 또 next를 누르면 1로 가라는 뜻 (계속 1111111)
next(it8, 1)  #2
next(it8, 1)  #3
next(it8, 1)  #4
next(it8, 1)  #5
next(it8, 1)  #1
next(it8, 1)  #1

it9 = iter(t)
next(iter9, None)      # 1,2,3,4,5 다 나온 후에 next를 누르면 끝났다는 의미로 none이 나옴. 즉 None이 나올 때까지 next해라

t = (1,2,3,4,5)
iter(t)
next(iter(t))

# zip(l1, l2) 
# 두 개의 x, y를 좌표로 만들고 싶을 때, 두 list를 하나씩 묶고 싶을 때

l1 = [1,2,3]
l2 = [4,5,6]
zip(l1, l2)
z = zip(l1, l2)
print(list(z)) #>> [(1,4),(2,5),(3,6)]

l3 = [7,8]
zip(l1, l3)
print(list(zip(l1,l3))) #>> [(1,7), (2,8)]
#이렇게 하고 zip하면 세 번째 값은 날려버림 (data 유실 주의)

#iter는 불려지는 순간 data 사라짐
