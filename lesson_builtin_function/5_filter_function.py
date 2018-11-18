# filter(filter_fn, iter) : filter object

# iterator들을 돌릴 때 filter_fn해서만 나온다.


# filter된 object만 나온다.

int_numbers = range(-5, 6) 
print(list(int_numbers)) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]


negatives = filter(lambda x: x < 0, int_numbers) #negatives: 음수만 달라는 뜻 >>[-5, -4, -3, -2, -1]
print(negatives) # <filter object at 0x0000013287ECBDA0>
print(list(negatives)) # [-5, -4, -3, -2, -1]

# lambda는 일종의 함수, "함수를 한 줄로 표시한다"는 뜻

# x변수는 0보다 작은 것만 가능하다. int_numbers의 값(-5~5)이 하나씩 lambda에 들어오는데, 이 때 0보다 작은 값으로만 filtering한다.
# x는 매개변수 x<0은 logic


# lambda를 코드로 써보면
# def fn(x):
    #return x < 0
# filter: 이 함수가 True인 것만 출력한다.

def fn(x):
    return x<0
    
n2 = filter(fn, int_numbers) # 함수를 인자로 받는 것

print(list(n2))  # >>>> negative만 쓰면 object의 주소가 나옴. #실제 값을 보고싶으면 list(negative)을 치면 된다.