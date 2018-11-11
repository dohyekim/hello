
# 0부터 20-1까지 돌릴 건데 2씩 jump
#for i in range(0, 20, 2):
#    print(i)

# 1) 0~19까지 2씩 jump한 값이 i로 들어간다.
# 2) 구한 i를 2로 거듭제곱한다.
# 3) 그 값을 list로 싼 것

arr = [i ** 2 for i in range(0, 20, 2)]
print(arr)

lst = [] #초기화
for i in range(0, 20, 2):
    i = i ** 2
    lst.append(i)
    
print(lst)

# 최솟값, 최댓값 구하기
print("min:", min(arr))
print("max:", max(arr))

lst = ['apple', 'pear', 'strawberry']
# outs를 f로 채울 건데
# loop를 돌면서 f를 받아올 것이다
# 그 lst가 'apple'이 아닐 때만 줘 
outs = [f for f in lst if f != 'apple']
print(outs)