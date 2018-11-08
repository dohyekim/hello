# 1~100 사이 소수의 값 구하기

sum=0

for i in range(2,101):
    if(i == 2):
        sum += i

    for n in range(2,i):
        if(i % n == 0):
            break
        if(n == (i-1)):
            sum += i
                     
print(sum)

       

