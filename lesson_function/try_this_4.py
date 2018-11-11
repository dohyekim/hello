# 두 수를 받아 사칙연산(+,-,*,/)을 수행하는 함수를 만들어 보세요.

def plus(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return a
    return a / b

while(True):
    cmd = input("put a and b usage: a op b >> ")

    if cmd == "quit":
        break

    cmds = cmd.split(' ')

    a = int(cmds[0])
    b = int(cmds[2])
    op = cmds[1]

    msg = "The answer is {:d}."
    
    if op == '+':
        r = plus(a, b)
    
    if op == '-':
        r = subtract(a, b)

    if op == '*':
        r = multiply(a, b)

    msg_2 = "The answer is {:+.1f}."
    
    if op == '/':
        r = divide(a, b)
        print(msg_2.format(r))

    print(msg.format(r))

