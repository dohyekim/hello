int_numbers = range(-5,6)

f = filter(lambda x: x < 0, int_numbers)
m = map(lambda x: x<0, int_numbers)

print("f=", list(f))

print("m=", list(m))

int_numbers = range(-5,6)

filter1 = filter(lambda x: x * 2, int_numbers)
print(list(filter1))           # [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5], false인 0만 빼고 나머지 값을 다 가져옴.

map1 = map(lambda x: x * 2, int_numbers)
print(list(map1))             # [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10] 

names = ['김가','김나','나나','다다']
n=filter(lambda x: x[0] == '김', names) #성(맨 앞 글자) == '김'인 경우
print(list(n))