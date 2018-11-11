# input value is String Type

# 3 + 4를 입력했을 때 3+4 는 str
# 23을 입력했을 때 23은 str. *int 아님!!

cmd =  input("Input>>> ")
print(cmd)

# Usage는 예시를 의미 (a, b 형태로 입력하세요.)
a = input("Usage: width, height  ")
# 받은 input을 ','로 분리하겠다는 의미
a_s = a.split(',')
print(a_s)

# input을 받으면 Terminal은 엔터가 입력될 때까지 무한 loop를 돌고 있는 셈