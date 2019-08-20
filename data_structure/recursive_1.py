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
            print("iiii> ",i)
        else:
            c = a
            a = b
            b = (a + c)
            answer = b
    return answer

    def solution(x):
    answer = 0
    if x <= 1:
        answer = x
    else:
        answer = solution(x-1) + solution(x-2)
    return answer
