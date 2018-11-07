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

