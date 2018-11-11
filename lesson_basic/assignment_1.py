# 1~100 사이 소수의 값 구하기

sum = 2

for i in range(1, 101):
    for n in range(2, i):
        if (i % n == 0):
            break

        if (i % n != 0 and n == (i - 1)):
            sum += i

print(sum)
       
# unsupported operand type(s) for +=: 'builtin_function_or_method' and 'int'