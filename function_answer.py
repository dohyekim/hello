def plus(a,b):
    return a + b
    
def subtract(a,b):
    return a - b

def multiple(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return a
    return a / b


cmd = input("수식을 입력하세요(usage: 2 + 3)> ")
cmds = cmd.split(' ')



# @ToDo cmds를 하나로 만들어보기!
# @붙이고 하면 나중에 코드가 길어졌을 때 찾아서 다시 확인할 수 있음.
a, op, b = int(cmds[0]), cmds[1], int(cmds[2])
#or a, b =int(a), int(b)

outType = "{:d}"

if op == '+':
    r = plus(a + b)
# if와 elif 사이는 띄어주는 게 매너
elif op == '-':
    r = minus(a + b)

elif op == 'x':
    r = 
#r은 초기화되지 않았기 때문에 else를 썼다.
else:

# print("answer is " + r) 이렇게 쓰면 ""(str)이랑 r이라는 것을 합하기 어려우니까 format쓰는 게 좋음.
# :f를 해서 float으로 나옴(ex.나누기했을 때 소수점이 나오는 경우)

if op = '/':
    print("Answer is {:.2f}".format(r))
else:
    print("Anwer is {:d}".format(r))