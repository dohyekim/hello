list(), set(), tuple(), enumerate()

# set() 집합구조로 바꾸는 것

min(), max(), sum(iter, start_value)

#sum은 math module만들 때 쓴다.

l = [1,2,3]
sum(l)
sum(l,10)  #기존값에 10을 더한다.

# math.fsum(l)로 쓸 수 있음.



all(iter), any(iter)

ll = [False, True, False]
lll = [False, False, False]
llll = [True, True, True, True]

all(ll)            # all(iter) 모든 게 True다

any(lll)           #하나라도 True다

l.append(0)          #0을 False
all(l)               #False
any(l)               #True

l.pop(3)             #3번째 있는 0을 뺌
all(l)               #True

iter(), next(it, after_last) # next(it) vs next(iter(t))

l = [1,2,3]
iter(l)                    # 객체로 바뀐다. iterator화함. iter는 next함수를 쓸 수 있다
it = iter(l)
next(it)         # 1
next(it)         # 2
next(it)         # 3 
#인덱스를 모르겠는데 하나씩 꺼내고 싶을 때

t = (1,2,3,4,5)
it5=iter(t)             # tuple이 iterator가 됨.
next(it5)               # >>>1
next(it5)
next(it5)
next(it5)
next(it5)
it6 = iter(t)
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

filter(), map(), sort() # ← 뒤에서 자세히

# 두 개의 x, y를 좌표로 만들고 싶을 때, 두 list를 하나씩 묶고 싶을 때

# zip(l1, l2) 

l1 = [1,2,3]
l2 = [4,5,6]
zip(l1, l2)
z=zip(l1, l2)
list(z)

l3 = [7,8]
#이렇게 하고 zip하면 세 번째 값은 날려버림 (data 유실 주의)

#iter는 불려지는 순간 datㅁ 사라짐
#it=iter(l)
#list(it) 한 후에 it(next)하면 error. 이미다 썼으니까