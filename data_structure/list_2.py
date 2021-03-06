# 정렬된 리스트에 원소 삽입
def solution(L, x):
    length = len(L)
    for idx, l in enumerate(L):
        # x가 가장 큰 수일 경우
        if idx == length-1:
            L.append(x)
            return L
        # x값이 원소의 값보다 더 클 경우 continue
        elif x > l:
            continue
        else:
            L.insert(idx, x)
            return L

# ==============================Refac==========================
def solution(L, x):
    length = len(L)
    for idx, l in enumerate(L):
        if x <= l:
            L.insert(idx, x)
            break
        else:
            if idx == (length - 1):
                L.append(x)
                break
    return L

# 혹은 

def solution(L, x):
    length = len(L)
    for idx, l in enumerate(L):
        if x <= l:
            L.insert(idx, x)
            break
    if len(L) == length:
        L.append(x)
    return L
    