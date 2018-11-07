def plus(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiple(a,b):
    return a * b

def divide(a,b):
    return a / b

q = input("a op b>>> ")
print(q)

qs = q.split(' ')

a = int(qs[0])
b = int(qs[2])
op = qs[1]


if op == '+':
    r = plus(a,b)
elif op == '-':
    r = subtract(a,b)
elif op == '*':
    r = multiple(a,b)
elif op == '/':
    r = divide(a,b)

msg = "답은 {}입니다."

print(msg.format(r))


