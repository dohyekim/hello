# 1부터 100까지의 합을 구하시오.

sum = 0

for i in range (1,101):
    sum += i

print(sum)


# 1부터 100까지 홀수의 합을 구하시오.

sum = 0

for i in range(1,101):
    if(i % 2 == 1):
        sum += i

print(sum)


# sum = 0 / print(sum) 기억해두기