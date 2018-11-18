
# map(mapped_fn, iter) : map object

# filter는 iterator 중에서 True인 것만 취함, 
# map은 전부 다 처리하는데 make_double function 사용 :2배로), 그때그때 쓸 거면 lambda사용

def make_double(n):

	return n * 2

numbers = (1, 2, 3, 4)

double_numbers = map( make_double, numbers )
print( list(double_numbers) )

triple_nubmers = map(lambda x: x * 3, numbers)      # 실제 실무에서는 "숫자만 취하고 싶다" -> filter(데이터 유실 가능성   ㅊ     ) "int화, str화 등" -> map(데이터를 다 지킬 수 있음)
print( list(triple_nubmers) )

