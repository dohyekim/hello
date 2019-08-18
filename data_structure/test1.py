# 입력으로 주어지는 리스트 x의 첫 원소와 마지막 원소의 합을 리턴하는 solution() 함수 만들기

def solution():
    cmd= input("Put numbers with comma (ex) [,204,29,12,42] >>  ")
    first = int(cmd[2])
    last = int(cmd[-2])
    print(first + last)
    return first + last
solution()