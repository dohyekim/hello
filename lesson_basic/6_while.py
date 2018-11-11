# while

i, sum = 0, 0

while(i >= 0):       # ()안의 조건을 만족한다면 영원히 돌린다. #(True)하면 무한loop
    i += 1
    if(i > 10 and i < 20):   # i = 1, 조건 충족 X, i = 10, i +=1 i = 20, i +=1 수행. i = 19, i+=1 i = 20, 조건충족 X
        continue              
                              #i>10 and i<15를 만족하지 못하면 밑의 줄로 넘어간다.
    sum += i                 #sum = 1 + 2+ 3+ ... + 10 + 20 + ... + 100
    if(i == 100):             #if절 만족 X 
        print("End!", sum)
        break


# continue: 뒤로 넘어가지 말고 계속 해라
# break: 그 loop을 벗어나라