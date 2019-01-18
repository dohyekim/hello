import random
from pprint import pprint

data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}

# pprint(data)

idx = ["A", "B", "C"]
sums = []
for i in idx:    
    a = data[i]
    # pprint(a)
    # print(a[0][0])
    n = 0
    m = 0
    for j in range(len(a)):
        n = n + a[j][j]
        m = m + a[j][-j-1]
    summed = n + m
    sums.append(summed)


dic = {}
lst = []
for i,j in enumerate(idx):
    dic[j] = sums[i] 
lst.append(dic)

# 출력 ---------------------------------------------------
print(lst[0])
minn = min(lst[0].values())

for k, v in dic.items():
    if v == minn:
        print(k)

# 단축 -------------------------------------------------
minn = min(dic, key = lambda x : dic[x])
# x를 받아서 dic[x]값을 dic의 형태로 return한다는 의미
# dic만 쓰면 default로 key를 준다. 따라서 실제로 return할 수 있는 건 key
# print(minn)




minn = min(dic.items(), key = lambda x : dic[1])[0]
# --> dic[1]이 value니까 여기서 loop를 돌려서 dic.items()의 형태로 나옴다.
# 걔의 [0]하면 key가 출력됨.

# key와 value를 바꿔버리기
qq = dict((v,k) for k, v in dic.items())
ww = ((min(v)) for v, k in qq.items())
print(ww)
