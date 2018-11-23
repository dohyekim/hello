# map과 filter 차이

int_numbers = range(-5,6)

f = filter(lambda x: x < 0, int_numbers)
m = map(lambda x: x<0, int_numbers)

print("f=", list(f))  #f= [-5, -4, -3, -2, -1]

print("m=", list(m))  #m= [True, True, True, True, True, False, False, False, False, False, False]

# -------------------------------------------------------------------------------
int_numbers = range(-5,6)

filter1 = filter(lambda x: x * 2, int_numbers)
print(list(filter1))           # [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5], false인 0만 빼고 나머지 값을 다 가져옴.

map1 = map(lambda x: x * 2, int_numbers)
print(list(map1))             # [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10] 

#------------------------------------------------------------------------------------
names = ['김가','김나','나나','다다']
n=filter(lambda x: x[0] == '김', names) #성(맨 앞 글자) == '김'인 경우
print(list(n))

filter1 = filter(lambda x: x * 2, int_numbers)
print(list(filter1))           # [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5], false인 0만 빼고 나머지 값을 다 가져옴.
#filter는 값을 변화시키지는 않는다.

map1 = map(lambda x: x * 2, int_numbers)
print(list(map1))             # [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10] 

#filter의 logic

def filter(l):
    ret = []
    for i in l:
        if i == True:
            ret.append(i)
        return ret