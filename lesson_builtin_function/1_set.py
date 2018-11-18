s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1 | s2

s1 & s2

s1 ^ s2

s1.union(s2)

ss = s1.union(s2)

s1.update(s2)

abs(-3)     #절댓값

divmod(5, 2)   #몫과 나머지 함께 오는 것

bin(7)    #binary #"0b"=2진수라는 뜻 111
oct #8 "0o" 8진수라는 뜻
hex #16진수 #"0x"=16진수라는 뜻
bin(oxd)

bool(0)             #==false
bool()                  #false
bool("sea;wle") #True (뭐라도 있어야됨)
bool(23) #TRue (1 이상의 숫자인 경우)

int(1.6)

float
str

pow(x, y)  #x의 y승
globals()  #현재 있는 전역 변수를 보여줌(이 파일 전체에 있는 변수)
help(min)  #min함수 쓰는법을 잊어버렸을 때, q누르면 빠져나옴

type(s1)

range(a, b, step)

round(1.5) #1.5의 반올림 ==2
round(2.5) # ==3 but 2가 나옴.
round(2.51) # ==3
round(2.3456, 3) #소수점 넷째자리에서 반올림 해서 셋째자리까지 올린다
round(0.5) ## ==0

format()
split()
len()
input()
print()

s = "abc"
list(s)  #str을 list로 만들기

s = ['aaa', 'bbb', ...]
"-".join(list(s))       #[aaa-bbb-ccc]형태로 잇겠다.



dir()       # 현재 이 파일에서 접근할 수 있는 내장 method
import random
dir(random) # random이 갖고 있는 method
import builtins
dir(builtins)        # 내장 함수들 다 나온다.

print("123")


eval("print("123")") #""안의 코드를 실행 (str을 code화한다/)


#user_1 = 23
#user-2 = 23
#user_1 == user_2 (hash가 같으면 같은 사람이라고 보는 것) # 같은 값인지 판단해주는 게 hash

hash(test)   # == memory 주소와 비슷하게 unique한 값을 만들어줌
id(test)     # == memory의 주소
             # == hash(test) / id(test)와 다른 값 나옴

test3 = test
#이 때는 test3이 새로 생기는 게 아님. test값을 참조하는 call by reference
# 따라서 hash/id(test)랑 같은 값이 나옴.