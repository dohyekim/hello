# 1~100 중에서 소수(1과 자기자신)의 합을 구하시오.

sum=0


for i in range(3,101):
    for n in range(2, i):
        if(i % n == 0):
            break
        else:
            ## i 가지고있기
    sum += i
print(sum)
