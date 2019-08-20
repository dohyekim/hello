def combi(n,m):
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        answer =  combi(n-1,m) + combi(n-1,m-1)
        print(answer)
        return answer


