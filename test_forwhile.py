#1 부터 100 까지의 합을 구하시오.

i, sum = 0, 0
while (i >= 0):
    i +=1
    
    sum +=i
    if(i >=100):
        print(sum)
        break


#for 사용( 1 부터 100 까지의 홀수의 합을 구하시오.)
sum = 0
for i in range(1,101):

    if(i%2==1):
        sum +=i    
    
print(sum)
    

#while 사용( 1 부터 100 까지의 홀수의 합을 구하시오.)

i=0; sum=0

while (i>=0):
    i +=1

    if(i%2==1):
        sum +=i

    if(i==100):
        print(sum)
        break

# 1~100 중에서 소수(약수가 1과 자기자신)의 합을 구하시오.
i = 0
n = 0

for i in range(2,101):
    
    n = i - 1
    n > 1 and n < i
    if(i % n ==0):
        continue
    if(i % n !=0):
        print(i)




    i += 1
while (i>=2)
    if(i%n=0) #나머지가 1과 자기자신을 제외한 정수로 나눴을 때 0이 나오면 정수 아님.