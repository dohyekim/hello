# Class에 존재하는 function을 method라고 함
# 반복되는 logic을 재사용할 수 있게 묶어두는 것이 Function(함수)

# def는 keyword. "얘는 함수야"라고 선언해주는 것
# ()는 argument. ".format()처럼" ()안에는 argument로 또다른 함수를 받을 수도 있다.
def fn():
    print("fn called")

# fn() 부르기
fn()
# fn() 안 부르면 아무것도 안 나옴.

# ()에 argument를 받는 경우
# 얘는 input(즉 x)도 있고 output도 있다.
def exp(x):
    return x ** 2

print(exp(3))

# 변수 만들기
exp = exp(3)
print(exp)

# list
def get_fruits():
    return ['orange', 'apple', 'banana']

print(get_fruits())

# 그 중에서 'apple'을 가져오고 싶은 경우
# get_fruits()를 가져오고 그 list에서 index[1] 불러와야 한다.
# 얘는 list가 하나이기 때문에 값을 하나만 return할 수 있다.
print(get_fruits()[1])

# 값을 여러 개(2개) return하고 싶은 경우
def get_name():
    return 'Kent', 'Beck'

print(get_name())           #>>> tuple로 return된다.

# name이라는 변수에는 tuple이 들어감
name = get_name()
# name[1] = "aaa"
# print(name)              >>>error

#full name 만들기
def full_name(first_name, last_name):
    return first_name + ' ' + last_name

name = get_name()
print(name, full_name("Ariana", "Grande"))
