

## 함수는 만들 때 주석을 달아야 한다.

def plus(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiple(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return a
    else:
        return a / b
            
while(True):
    
    # q.split(' ') 전에 나와야 "quit"이라는 str(split되지 않음)을 넣을 수 있다.

    q = input("숫자 op 숫자>>> ")
    
    # continue는 필요 없다. 어차피 while loop은 돌아가고 있고 여기서 continue하면 계속 input만 반복되기 때문.
    if q == "quit":
        break
    
    qs = q.split(' ')
# list에서 값을 가져왔기 때문에 int로 변환한 것
    a = int(qs[0])
    b = int(qs[2])
    op = qs[1]

    def operator(a,b):
        if op == '+':
            return plus(a,b)
        if op == "-":
            return minus(a,b)
        if op == "*":
            return multiple(a,b)
        if op == "/":
            return divide
    if op == '+':
        r = plus(a,b)
    elif op == '-':
        r = subtract(a,b)
    elif op == '*':
        r = multiple(a,b)
    elif op == '/':
        r = divide(a,b)

    msg1 = "답은 {:f}입니다."
    msg2 = "답은 {:d}입니다."

    if op == '/':
        print(msg1.format(r))
    else:
        print(msg2.format(r))
    
        
    #집에서 연습: 덩어리들을 함수로 빼서 만들어보기