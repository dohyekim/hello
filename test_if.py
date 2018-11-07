score=80
if score > 80:
    print("잘했어요")
    print("잘했습니다")
elif score == 80:
    print("아쉽네요")
    print("그래도 잘했어요")
else:
    print("열심히 하면 됩니다")
    print("그래도 잘했어요")

score=72
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >=70:
    print("B")
elif score >=60:
    print("B")
else:
    print("F")

for i in range(1,100):
    print(i)

for i in range(10):
    print(i)

fruits = ['오렌지','사과','바나나']
for x in fruits:
    print(x)

for i in range(0,3):
    print(fruits[i])

i, sum = 0, 0
while(i >= 0):
    i +=1
    if(i>10 and i<20):
        continue
    sum += i
    if (i == 100):
        print("End!!", sum)
        break
        

