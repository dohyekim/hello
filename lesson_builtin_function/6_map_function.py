
# map(mapped_fn, iter) : map object

#filter는 True인 것만 취함, map은 전부 다 처리하는데 make_double function사용 :2배로), 그때그때 쓸 거면 lambda사용

def make_double(n):

	return n * 2

numbers = (1, 2, 3, 4)

double_numbers = map( make_double, numbers )
print( list(double_numbers) )

triple_nubmers = map(lambda x: x * 3, numbers)      # 실제 실무에서는 "숫자만 취하고 싶다" -> filter(데이터 유실 가능성   ㅊ     ) "int화, str화 등" -> map(데이터를 다 지킬 수 있음)
print( list(triple_nubmers) )

# map과 filter 차이
int_numbers = range(-5,6)

filter1 = filter(lambda x: x * 2, int_numbers)
print(list(filter1))           # [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5], false인 0만 빼고 나머지 값을 다 가져옴.

map1 = map(lambda x: x * 2, int_numbers)
print(list(map1))             # [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10] 

#filter의 logic

def filter(l):
    ret = []
    for i in l:
        if i == True:
            ret.append(i)
        return ret