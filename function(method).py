#
def fn():
    print("fn called")

print(fn())


#
def exp(x):
    return x ** 2

print(exp(3))


#
def get_fruits():
    return ['오렌지','사과','귤']

fruits = get_fruits()
print(get_fruits()[1])
print(fruits[1])

print(type(get_fruits))
print(type(fruits))

#
def get_name():
    return 'Kent','Beck'

name = get_name()
print(get_name())
print(type(name))

#
def var_param(a,*vp):
    print(a, len(vp), vp[len(vp) - 1])

var_param(1,2,3,4)

#
def default_param(a, vp = 100):
    print(a, vp)

default_param(1)
default_param(1,2)


# error남
# default_param(1,2,3,,4,5)
