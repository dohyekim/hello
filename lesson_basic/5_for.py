# 사용량 for > while
# for "each"

for i in range(1, 100):        #100은 포함 X!
    print(1)

for i in range(10):
    print(1)

# each의 의미
fruits = ['orange', 'apple', 'banana']       # each : '오렌지'일 때 1번, '사과'일 때 1번, '바나나'일 때 한 1번
for x in fruits:
    print(x)

# index를 사용한 each 
for i in range(0,3):          # index0 '오렌지', index1 '사과'. index2 바나나
    print(fruits[i])