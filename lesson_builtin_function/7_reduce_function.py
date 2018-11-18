# reduce(reduce_fn, iter) : one result

# reduce는 내장함수가 아닌 functools라는 곳에 있는 reduce를 가져온 것
from functools import reduce      

lst = [1, 2, 3, 4]
product = lst[0]          #즉  product = 1

for num in lst:
    product = product * num

# 1, 2, 6, 24 중에서 마지막 값인 24만 취하는 게 reduce

print("product1>>", product) #>>> product1>> 24

# 위에 써둔 값을 한 줄로 표현한 것.
product2 = reduce(lambda x, y: x * y, lst)  # 두 개의 값을 어떻게 할 건지를 돌리면 마지막 값만 준다. 
print("product2>>", product2) #>>> product2>> 24


sig = lst[0]
for i, num in enumerate(lst):
    if i == 0: continue
    sig = sig + num

sigma = reduce(lambda x, y: x + y, lst)   # sigma i=1~4일 때 lst
print("sigma >>> ", sigma)                #>>> sigma >>>  10


# reduce에서 x의 초기값은 1
# x = 1, 들어가면 y에는 2(lst에 있는 두 번째 값)가 들어감. 결과는 3. 이 결과는 다시 x에 들어가고 y 에는 3이 들어감. 결과는 6. 
# 이 결과는 다시 x에 들어가고 y에는 4가 들어간다. x에는 다시 10이 들어간다. 10 출력

