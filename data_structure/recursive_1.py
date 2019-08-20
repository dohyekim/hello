#1. 재귀함수를 이용한 피보나치 순열

def solution(x):
    answer = 0
    if x == 0:
        answer = 0
    elif x == 1:
        answer = 1
    else:
        answer = solution(x-1) + solution(x-2)
    return answer

#2. 반복문을 이용한 피보나치 순열
def solution_for(x):
    answer = 0
    a = 0
    b = 1

    for i in range(x+1):
        if i < 2:
            answer = i
        else:
            c = a
            a = b
            b = (a + c)
            answer = b
    return answer

#  ===============Refac한 두 가지 코드=============
def solution(x):
    # answer = 0
    a = 0
    b = 1
    if x < 2:
        print(x)
        return x
    for i in range(2,x+1):
        a, b = b, a+b
    return b

def solution(x):
    answer = 0
    a = 0
    b = 1

    for i in range(x+1):
        if i < 2:
            b = i
        else:
            a, b = b, a+b
    return b