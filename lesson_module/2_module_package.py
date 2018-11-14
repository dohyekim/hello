#module을 모아둔 폴더가 package



from calcs import plus, minus, mul, div
print( plus(3, 5) )
import calcs
print( calcs.plus(3, 5) )
import sys, os

print("Path>>", sys.path )
print("cwd>>", os.getcwd())      #current working directory
os.chdir("..")       #change directory
print("cwd>>", os.getcwd())
# cf. from utils import *
# cf. import my_pkg.test_module.fn



# calcs.py
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return a
    return a / b