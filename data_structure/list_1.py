
# 리스트에서 원소 찾아내기
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