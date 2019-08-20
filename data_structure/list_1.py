
# 리스트에서 원소 찾아내기
# 1차 시도(틀린 답)
def solution(L, x):
    answer = []
    n = 0
    while True:
        try:
            idx = L.index(x)
            answer.append(idx + n)
            n += (idx + 1)
            L = L[n:]
        except:
            break
    if len(answer) == 0:
        answer = [-1]
    return answer

# 2차 시도(피드백 반영, 테스트 통과)
def solution(L, x):
    answer = []
    n = 0
    while True:
        try:
            idx = L.index(x)
            L = L[(idx+1):]
            answer.append(idx + n)
            n += (idx + 1)
        except:
            break
    if len(answer) == 0:
        answer = [-1]
    return answer