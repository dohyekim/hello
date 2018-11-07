# 1~100 중에서 소수(1과 자기자신)의 합을 구하시오.

for i in range(2,101):
    for n in range(2,i):
        if(i != 2 and n % i == 0):
            break
        if(n == (i-1) and i == 2):
            sum += i

print(sum)