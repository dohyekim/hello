
#*vp : vp라는 값은 가변적이라는 의미
# vp 는 tuple
def var_param(a, *vp):
    print(type(vp))
    print(a, len(vp), vp[len(vp)-1])

# var_param() >>> var_param() missing 1 required positional argument: 'a'

# var_param("Aaa")  >>> vp 자리가 없다고 error

# vp[len(vp)-1] 에서 len(vp) = 2, vp[1] = "cc"
var_param("aa", "bb", "cc")
var_param(1, 2, 3, 4)

# def default_param(a, vp): 
#   print(a, b)
# default_param("Aaa") >>> vp 값이 없다고 error.
# 이 때 vp값이 없을 때는 기본값을 넣으라는 의미로 vp = 100
def default_param(a, vp = 100):
    print(a, vp)

default_param(1)